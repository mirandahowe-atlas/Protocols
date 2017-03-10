from opentrons import robot, containers, instruments

tiprack = containers.load('tiprack-200ul', 'A1','tiprack')
tiprack2 = containers.load('tiprack-200ul', 'A2','tiprack2')
DNA_plate = containers.load('96-flat', 'C1','DNA_plate') 
PCR_plate = containers.load('96-flat', 'C2','PCR_plate') 
trough = containers.load('trough-12row', 'D1', 'trough')
trash = containers.load('point','A3','trash')

p50 = instruments.Pipette(
        axis="a",
        max_volume=50,
        min_volume=5,
        tip_racks=[tiprack, tiprack2],
        trash_container=trash,
        channels=8,
        name="p50"
)

combined_MM = trough['A1']
# add combined gene master mix from all rows to pcr plate
p50.pick_up_tip()
for i in range(12):
	if p50.current_volume < 20:
		p50.aspirate(combined_MM)
	p50.dispense(20, PCR_plate.rows[i])
p50.drop_tip()

# map samples from DNA plate to PCR plate
for i in range(12):
	p50.pick_up_tip()
	p50.aspirate(5, DNA_plate.rows[i]).dispense(PCR_plate.rows[i])
	p50.drop_tip()