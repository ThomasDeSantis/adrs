from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="mint",
    accept_cargo_types=[
        "GOLD",
        "COPR",
    ],
    prob_in_game="0",
    prob_map_gen="12",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    special_flags=["IND_FLAG_ONLY_IN_TOWNS"],
    prospect_chance="0.75",
    name="string(STR_IND_MINT)",
    nearby_station_name="string(STR_STATION_BANK_TOP)",
    fund_cost_multiplier="4",
    provides_snow=True,
)

industry.enable_in_economy("TRADE_AND_WAVES")

industry.add_tile(
    id="mint_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
# base-set temperate Bank halves (industry gfx 58/59); OpenTTD has no mint of its own
sprite_bank_left = industry.add_sprite(
    sprite_number=2180,
    zextent=25,
)
sprite_bank_right = industry.add_sprite(
    sprite_number=2181,
    zextent=25,
)

industry.add_spritelayout(
    id="mint_spritelayout_left",
    tile="mint_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_bank_left],
)
industry.add_spritelayout(
    id="mint_spritelayout_right",
    tile="mint_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[sprite_bank_right],
)

industry.add_industry_layout(
    id="mint_industry_layout_1",
    layout=[
        (0, 0, "mint_spritelayout_left"),
        (1, 0, "mint_spritelayout_right"),
    ],
)
