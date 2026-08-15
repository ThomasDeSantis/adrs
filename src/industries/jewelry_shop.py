from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="jewelry_shop",
    accept_cargos_with_input_ratios=[
        ("GOLD", 6),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("GOOD", 8),
    ],
    prob_in_game="0",
    prob_map_gen="5",
    map_colour="177",
    name="string(STR_IND_JEWELRY_SHOP)",
    nearby_station_name="string(STR_STATION_MARKET)",
    fund_cost_multiplier="14",
    pollution_and_squalor_factor=1,
    provides_snow=True,
)

industry.enable_in_economy("TRADE_AND_WAVES")

industry.add_tile(
    id="jewelry_shop_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 44, -31, -13)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 74, -31, -43)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 88, -31, -57)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 85, -31, -54)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 76, -31, -45)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 63, -31, -32)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 98, -31, -68)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(500, 10, 64, 54, -31, -32)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(570, 10, 64, 76, -31, -54)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(640, 10, 64, 28, -31, 3)],
)
spriteset_11 = industry.add_spriteset(
    sprites=[(710, 10, 64, 49, -31, -27)],
)

industry.add_spritelayout(
    id="jewelry_shop_spritelayout_1",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_2",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_3",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_4",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_5",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5, spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_6",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6, spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_7",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_8",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8, spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_9",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_10",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_11, spriteset_10],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_11",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2, spriteset_11],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_empty",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="jewelry_shop_industry_layout_1",
    layout=[
        (0, 0, "jewelry_shop_spritelayout_9"),
        (0, 1, "jewelry_shop_spritelayout_4"),
        (1, 0, "jewelry_shop_spritelayout_7"),
        (1, 1, "jewelry_shop_spritelayout_6"),
    ],
)
industry.add_industry_layout(
    id="jewelry_shop_industry_layout_2",
    layout=[
        (0, 0, "jewelry_shop_spritelayout_empty"),
        (0, 1, "jewelry_shop_spritelayout_5"),
        (1, 0, "jewelry_shop_spritelayout_10"),
        (1, 1, "jewelry_shop_spritelayout_11"),
    ],
)
industry.add_industry_layout(
    id="jewelry_shop_industry_layout_3",
    layout=[
        (0, 0, "jewelry_shop_spritelayout_3"),
        (0, 1, "jewelry_shop_spritelayout_9"),
        (0, 2, "jewelry_shop_spritelayout_2"),
        (1, 0, "jewelry_shop_spritelayout_8"),
        (1, 1, "jewelry_shop_spritelayout_7"),
        (1, 2, "jewelry_shop_spritelayout_1"),
    ],
)
