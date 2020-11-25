metadata = {'apiLevel': '2.0'}

def run(ctx):

    column_count = 12

    p20m = ctx.load_instrument('p20_multi_gen2', 'right', tip_racks=[ctx.load_labware("opentrons_96_filtertiprack_20ul", x) for x in ["2","3"]])
    p1000s = ctx.load_instrument('p1000_single_gen2', 'left', tip_racks=[])

    biorad_96_well = ctx.load_labware("opentrons_96_aluminumblock_biorad_wellplate_200ul","4")
    b_cols = biorad_96_well.rows()[0][:column_count]
    pcr_strip = ctx.load_labware("opentrons_96_aluminumblock_generic_pcr_strip_200ul", "5")

    for cols, target_well in zip([b_cols[:6], b_cols[6:]], [pcr_strip.wells_by_name()[x] for x in ["A1","A2"]]):
        for col in cols:
            print(target_well)
            p20m.transfer(20, col, target_well)

