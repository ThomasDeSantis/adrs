from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="naval_yard",
    accept_cargo_types=[
        "STEL",
        "ARMS",
        "POWR",
    ],
    prob_in_game="0",
    prob_map_gen="6",
    map_colour="170",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_BUILT_ON_WATER"],
    prospect_chance="0.75",
    town_industry_for_cargoflow=False,
    name="string(STR_IND_NAVAL_YARD)",
    nearby_station_name="string(STR_STATION_INDUSTRY_HARBOUR_3)",
    fund_cost_multiplier="7",
)

industry.enable_in_economy("TRADE_AND_WAVES", intro_year=1895)

industry.add_tile(
    id="naval_yard_tile_1",
    foundations="return CB_RESULT_NO_FOUNDATIONS",
    location_checks=TileLocationChecks(always_allow_founder=False, require_coast=True),
)

sprite_ground = industry.add_sprite(sprite_number="GROUNDSPRITE_WATER")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 100, -31, -67)],
)
spriteset_slipway = industry.add_spriteset(
    sprites=[(10, 70, 64, 40, -31, -7)],
)
spriteset_shed = industry.add_spriteset(
    sprites=[(80, 10, 64, 39, -31, -8)],
)
spriteset_crane = industry.add_spriteset(
    sprites=[(150, 10, 64, 64, -31, -33)],
)
industry.add_spritelayout(
    id="naval_yard_spritelayout",
    tile="naval_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="naval_yard_spritelayout_slipway",
    tile="naval_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slipway],
)
industry.add_spritelayout(
    id="naval_yard_spritelayout_shed",
    tile="naval_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_slipway, spriteset_shed],
)
industry.add_spritelayout(
    id="naval_yard_spritelayout_crane",
    tile="naval_yard_tile_1",
    ground_sprite=sprite_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_crane],
)
industry.add_industry_layout(
    id="naval_yard_industry_layout",
    layout=[(0, 0, "naval_yard_spritelayout")],
)
industry.add_industry_layout(
    id="naval_yard_industry_layout_2",
    layout=[
        (0, 0, "naval_yard_spritelayout_shed"),
        (0, 1, "naval_yard_spritelayout"),
        (0, 2, "naval_yard_spritelayout_crane"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "spritelayout_null_water"),
        (1, 2, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="naval_yard_industry_layout_3",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "spritelayout_null_water"),
        (0, 2, "spritelayout_null_water"),
        (1, 0, "naval_yard_spritelayout_crane"),
        (1, 1, "naval_yard_spritelayout"),
        (1, 2, "naval_yard_spritelayout_shed"),
    ],
)
industry.add_industry_layout(
    id="naval_yard_industry_layout_4",
    layout=[
        (0, 0, "naval_yard_spritelayout_shed"),
        (0, 1, "spritelayout_null_water"),
        (1, 0, "naval_yard_spritelayout"),
        (1, 1, "spritelayout_null_water"),
        (2, 0, "naval_yard_spritelayout_slipway"),
        (2, 1, "spritelayout_null_water"),
    ],
)
industry.add_industry_layout(
    id="naval_yard_industry_layout_5",
    layout=[
        (0, 0, "spritelayout_null_water"),
        (0, 1, "naval_yard_spritelayout_slipway"),
        (1, 0, "spritelayout_null_water"),
        (1, 1, "naval_yard_spritelayout"),
        (2, 0, "spritelayout_null_water"),
        (2, 1, "naval_yard_spritelayout_crane"),
    ],
)
