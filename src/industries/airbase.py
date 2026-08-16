from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="airbase",
    accept_cargo_types=[
        "ACFT",
    ],
    prob_in_game="0",
    prob_map_gen="6",
    map_colour="155",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    prospect_chance="0.75",
    town_industry_for_cargoflow=False,
    name="string(STR_IND_AIRBASE)",
    nearby_station_name="string(STR_STATION_AIRBASE)",
    fund_cost_multiplier="7",
)

industry.enable_in_economy("TRADE_AND_WAVES", intro_year=1930)

industry.add_tile(
    id="airbase_tile_1",
    location_checks=TileLocationChecks(require_effectively_flat=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_hangar = industry.add_spriteset(
    sprites=[(10, 20, 64, 48, -32, -17)],
)
spriteset_apron = industry.add_spriteset(
    sprites=[(90, 20, 64, 31, -32, 0)],
)

industry.add_spritelayout(
    id="airbase_spritelayout_hangar",
    tile="airbase_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_hangar],
)
industry.add_spritelayout(
    id="airbase_spritelayout_apron",
    tile="airbase_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_apron],
)

industry.add_industry_layout(
    id="airbase_industry_layout_1",
    layout=[
        (0, 0, "airbase_spritelayout_hangar"),
        (0, 1, "airbase_spritelayout_hangar"),
        (0, 2, "airbase_spritelayout_hangar"),
        (1, 0, "airbase_spritelayout_apron"),
        (1, 1, "airbase_spritelayout_apron"),
        (1, 2, "airbase_spritelayout_apron"),
    ],
)
