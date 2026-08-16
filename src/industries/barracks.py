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
    location_checks=TileLocationChecks(disallow_slopes=True),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_block_a = industry.add_spriteset(
    sprites=[(10, 20, 64, 57, -32, -26)],
)
spriteset_block_b = industry.add_spriteset(
    sprites=[(86, 20, 64, 57, -32, -26)],
)
spriteset_shelter_a = industry.add_spriteset(
    sprites=[(162, 20, 64, 45, -32, -14)],
)
spriteset_shelter_b = industry.add_spriteset(
    sprites=[(238, 20, 64, 45, -32, -14)],
)
spriteset_parade = industry.add_spriteset(
    sprites=[(314, 20, 64, 34, -32, -3)],
)

industry.add_spritelayout(
    id="barracks_spritelayout_block_a",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_block_a],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_block_b",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_block_b],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_block_c",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_block_a],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_yard_a",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_yard_b",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_yard_c",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_shelter_a",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shelter_a],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_shelter_b",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_shelter_b],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="barracks_spritelayout_parade",
    tile="barracks_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_parade],
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="barracks_industry_layout_1",
    layout=[
        (0, 0, "barracks_spritelayout_block_a"),
        (0, 1, "barracks_spritelayout_block_b"),
        (0, 2, "barracks_spritelayout_block_c"),
        (1, 0, "barracks_spritelayout_yard_a"),
        (1, 1, "barracks_spritelayout_yard_b"),
        (1, 2, "barracks_spritelayout_yard_c"),
        (2, 0, "barracks_spritelayout_shelter_a"),
        (2, 1, "barracks_spritelayout_shelter_b"),
        (2, 2, "barracks_spritelayout_parade"),
    ],
)
