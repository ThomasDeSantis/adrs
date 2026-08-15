from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(
    id="barracks",
    accept_cargo_types=[
        "FOOD",
        "ARMS",
        "TANK",
    ],
    prob_in_game="0",
    prob_map_gen="12",
    map_colour="168",
    life_type="IND_LIFE_TYPE_BLACK_HOLE",
    town_industry_for_cargoflow=False,
    prospect_chance="0.75",
    name="string(STR_IND_BARRACKS)",
    nearby_station_name="string(STR_STATION_BASE)",
    fund_cost_multiplier="4",
    provides_snow=True,
)

industry.enable_in_economy("TRADE_AND_WAVES")

industry.add_tile(
    id="barracks_tile_1",
    location_checks=TileLocationChecks(require_road_adjacent=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(
    sprites=[(10, 10, 64, 31, -31, 0)],
)
spriteset_1 = industry.add_spriteset(sprites=[(10, 60, 64, 48, -31, -18)])
industry.add_spritelayout(
    id="barracks_spritelayout",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_industry_layout(
    id="barracks_industry_layout",
    layout=[(0, 0, "barracks_spritelayout")],
)
