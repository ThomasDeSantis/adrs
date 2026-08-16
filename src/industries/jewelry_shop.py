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
# base-set tropic/arctic Bank halves (industry gfx 89/90) - a complete building,
# unlike the donor sheet's jigsaw fragments
sprite_shop_left = industry.add_sprite(
    sprite_number=2186,
    zextent=25,
)
sprite_shop_right = industry.add_sprite(
    sprite_number=2187,
    zextent=25,
)

industry.add_spritelayout(
    id="jewelry_shop_spritelayout_left",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_shop_left],
)
industry.add_spritelayout(
    id="jewelry_shop_spritelayout_right",
    tile="jewelry_shop_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_shop_right],
)

industry.add_industry_layout(
    id="jewelry_shop_industry_layout_1",
    layout=[
        (0, 0, "jewelry_shop_spritelayout_left"),
        (1, 0, "jewelry_shop_spritelayout_right"),
    ],
)
