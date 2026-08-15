from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="blood_wizard_tower",
    accept_cargos_with_input_ratios=[
        ("LAMB", 8),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("GOLD", 2),
    ],
    closes_when_starved=False,
    prob_in_game="0",
    prob_map_gen="1",
    map_colour="162",
    name="string(STR_IND_BLOOD_WIZARD_TOWER)",
    nearby_station_name="string(STR_STATION_FORGE)",
    fund_cost_multiplier="18",
    pollution_and_squalor_factor=1,
    provides_snow=True,
)

industry.enable_in_economy("TRADE_AND_WAVES")

industry.add_tile(
    id="blood_wizard_tower_tile_1",
    location_checks=TileLocationChecks(),
)

spriteset_ground = industry.add_spriteset(
    type="slab",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_0_0 = industry.add_spriteset(sprites=[(224, 0, 64, 218, -31, -202)])
spriteset_0_1 = industry.add_spriteset(sprites=[(288, 0, 32, 234, 1, -218)])
spriteset_0_2 = industry.add_spriteset(sprites=[(320, 0, 32, 250, 1, -234)])
spriteset_0_3 = industry.add_spriteset(sprites=[(352, 0, 32, 266, 1, -250)])
spriteset_0_4 = industry.add_spriteset(sprites=[(384, 0, 32, 282, 1, -266)])
spriteset_0_5 = industry.add_spriteset(sprites=[(416, 0, 32, 298, 1, -282)])
spriteset_0_6 = industry.add_spriteset(sprites=[(448, 0, 32, 314, 1, -298)])
spriteset_0_7 = industry.add_spriteset(sprites=[(480, 0, 32, 345, 1, -314)])
spriteset_1_0 = industry.add_spriteset(sprites=[(192, 0, 32, 234, -31, -218)])
spriteset_1_1 = industry.add_spriteset(sprites=[(224, 218, 64, 32, -31, -16)])
spriteset_1_2 = industry.add_spriteset(sprites=[(288, 234, 32, 32, 1, -16)])
spriteset_1_3 = industry.add_spriteset(sprites=[(320, 250, 32, 32, 1, -16)])
spriteset_1_4 = industry.add_spriteset(sprites=[(352, 266, 32, 32, 1, -16)])
spriteset_1_5 = industry.add_spriteset(sprites=[(384, 282, 32, 32, 1, -16)])
spriteset_1_6 = industry.add_spriteset(sprites=[(416, 298, 32, 32, 1, -16)])
spriteset_1_7 = industry.add_spriteset(sprites=[(448, 314, 32, 47, 1, -16)])
spriteset_2_0 = industry.add_spriteset(sprites=[(160, 0, 32, 250, -31, -234)])
spriteset_2_1 = industry.add_spriteset(sprites=[(192, 234, 32, 32, -31, -16)])
spriteset_2_2 = industry.add_spriteset(sprites=[(224, 250, 64, 32, -31, -16)])
spriteset_2_3 = industry.add_spriteset(sprites=[(288, 266, 32, 32, 1, -16)])
spriteset_2_4 = industry.add_spriteset(sprites=[(320, 282, 32, 32, 1, -16)])
spriteset_2_5 = industry.add_spriteset(sprites=[(352, 298, 32, 32, 1, -16)])
spriteset_2_6 = industry.add_spriteset(sprites=[(384, 314, 32, 32, 1, -16)])
spriteset_2_7 = industry.add_spriteset(sprites=[(416, 330, 32, 47, 1, -16)])
spriteset_3_0 = industry.add_spriteset(sprites=[(128, 0, 32, 266, -31, -250)])
spriteset_3_1 = industry.add_spriteset(sprites=[(160, 250, 32, 32, -31, -16)])
spriteset_3_2 = industry.add_spriteset(sprites=[(192, 266, 32, 32, -31, -16)])
spriteset_3_3 = industry.add_spriteset(sprites=[(224, 282, 64, 32, -31, -16)])
spriteset_3_4 = industry.add_spriteset(sprites=[(288, 298, 32, 32, 1, -16)])
spriteset_3_5 = industry.add_spriteset(sprites=[(320, 314, 32, 32, 1, -16)])
spriteset_3_6 = industry.add_spriteset(sprites=[(352, 330, 32, 32, 1, -16)])
spriteset_3_7 = industry.add_spriteset(sprites=[(384, 346, 32, 47, 1, -16)])
spriteset_4_0 = industry.add_spriteset(sprites=[(96, 0, 32, 282, -31, -266)])
spriteset_4_1 = industry.add_spriteset(sprites=[(128, 266, 32, 32, -31, -16)])
spriteset_4_2 = industry.add_spriteset(sprites=[(160, 282, 32, 32, -31, -16)])
spriteset_4_3 = industry.add_spriteset(sprites=[(192, 298, 32, 32, -31, -16)])
spriteset_4_4 = industry.add_spriteset(sprites=[(224, 314, 64, 32, -31, -16)])
spriteset_4_5 = industry.add_spriteset(sprites=[(288, 330, 32, 32, 1, -16)])
spriteset_4_6 = industry.add_spriteset(sprites=[(320, 346, 32, 32, 1, -16)])
spriteset_4_7 = industry.add_spriteset(sprites=[(352, 362, 32, 47, 1, -16)])
spriteset_5_0 = industry.add_spriteset(sprites=[(64, 0, 32, 298, -31, -282)])
spriteset_5_1 = industry.add_spriteset(sprites=[(96, 282, 32, 32, -31, -16)])
spriteset_5_2 = industry.add_spriteset(sprites=[(128, 298, 32, 32, -31, -16)])
spriteset_5_3 = industry.add_spriteset(sprites=[(160, 314, 32, 32, -31, -16)])
spriteset_5_4 = industry.add_spriteset(sprites=[(192, 330, 32, 32, -31, -16)])
spriteset_5_5 = industry.add_spriteset(sprites=[(224, 346, 64, 32, -31, -16)])
spriteset_5_6 = industry.add_spriteset(sprites=[(288, 362, 32, 32, 1, -16)])
spriteset_5_7 = industry.add_spriteset(sprites=[(320, 378, 32, 47, 1, -16)])
spriteset_6_0 = industry.add_spriteset(sprites=[(32, 0, 32, 314, -31, -298)])
spriteset_6_1 = industry.add_spriteset(sprites=[(64, 298, 32, 32, -31, -16)])
spriteset_6_2 = industry.add_spriteset(sprites=[(96, 314, 32, 32, -31, -16)])
spriteset_6_3 = industry.add_spriteset(sprites=[(128, 330, 32, 32, -31, -16)])
spriteset_6_4 = industry.add_spriteset(sprites=[(160, 346, 32, 32, -31, -16)])
spriteset_6_5 = industry.add_spriteset(sprites=[(192, 362, 32, 32, -31, -16)])
spriteset_6_6 = industry.add_spriteset(sprites=[(224, 378, 64, 32, -31, -16)])
spriteset_6_7 = industry.add_spriteset(sprites=[(288, 394, 32, 47, 1, -16)])
spriteset_7_0 = industry.add_spriteset(sprites=[(0, 0, 32, 345, -31, -314)])
spriteset_7_1 = industry.add_spriteset(sprites=[(32, 314, 32, 47, -31, -16)])
spriteset_7_2 = industry.add_spriteset(sprites=[(64, 330, 32, 47, -31, -16)])
spriteset_7_3 = industry.add_spriteset(sprites=[(96, 346, 32, 47, -31, -16)])
spriteset_7_4 = industry.add_spriteset(sprites=[(128, 362, 32, 47, -31, -16)])
spriteset_7_5 = industry.add_spriteset(sprites=[(160, 378, 32, 47, -31, -16)])
spriteset_7_6 = industry.add_spriteset(sprites=[(192, 394, 32, 47, -31, -16)])
spriteset_7_7 = industry.add_spriteset(sprites=[(224, 410, 64, 47, -31, -16)])

industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_0_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_0_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_1_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_2_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_3_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_4_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_5_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_6_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6_7],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_0",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_0],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_1",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_1],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_2",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_2],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_3",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_3],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_4",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_4],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_5",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_5],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_6",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_6],
)
industry.add_spritelayout(
    id="blood_wizard_tower_spritelayout_7_7",
    tile="blood_wizard_tower_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7_7],
)

industry.add_industry_layout(
    id="blood_wizard_tower_industry_layout",
    layout=[
        (0, 0, "blood_wizard_tower_spritelayout_0_0"),
        (0, 1, "blood_wizard_tower_spritelayout_0_1"),
        (0, 2, "blood_wizard_tower_spritelayout_0_2"),
        (0, 3, "blood_wizard_tower_spritelayout_0_3"),
        (0, 4, "blood_wizard_tower_spritelayout_0_4"),
        (0, 5, "blood_wizard_tower_spritelayout_0_5"),
        (0, 6, "blood_wizard_tower_spritelayout_0_6"),
        (0, 7, "blood_wizard_tower_spritelayout_0_7"),
        (1, 0, "blood_wizard_tower_spritelayout_1_0"),
        (1, 1, "blood_wizard_tower_spritelayout_1_1"),
        (1, 2, "blood_wizard_tower_spritelayout_1_2"),
        (1, 3, "blood_wizard_tower_spritelayout_1_3"),
        (1, 4, "blood_wizard_tower_spritelayout_1_4"),
        (1, 5, "blood_wizard_tower_spritelayout_1_5"),
        (1, 6, "blood_wizard_tower_spritelayout_1_6"),
        (1, 7, "blood_wizard_tower_spritelayout_1_7"),
        (2, 0, "blood_wizard_tower_spritelayout_2_0"),
        (2, 1, "blood_wizard_tower_spritelayout_2_1"),
        (2, 2, "blood_wizard_tower_spritelayout_2_2"),
        (2, 3, "blood_wizard_tower_spritelayout_2_3"),
        (2, 4, "blood_wizard_tower_spritelayout_2_4"),
        (2, 5, "blood_wizard_tower_spritelayout_2_5"),
        (2, 6, "blood_wizard_tower_spritelayout_2_6"),
        (2, 7, "blood_wizard_tower_spritelayout_2_7"),
        (3, 0, "blood_wizard_tower_spritelayout_3_0"),
        (3, 1, "blood_wizard_tower_spritelayout_3_1"),
        (3, 2, "blood_wizard_tower_spritelayout_3_2"),
        (3, 3, "blood_wizard_tower_spritelayout_3_3"),
        (3, 4, "blood_wizard_tower_spritelayout_3_4"),
        (3, 5, "blood_wizard_tower_spritelayout_3_5"),
        (3, 6, "blood_wizard_tower_spritelayout_3_6"),
        (3, 7, "blood_wizard_tower_spritelayout_3_7"),
        (4, 0, "blood_wizard_tower_spritelayout_4_0"),
        (4, 1, "blood_wizard_tower_spritelayout_4_1"),
        (4, 2, "blood_wizard_tower_spritelayout_4_2"),
        (4, 3, "blood_wizard_tower_spritelayout_4_3"),
        (4, 4, "blood_wizard_tower_spritelayout_4_4"),
        (4, 5, "blood_wizard_tower_spritelayout_4_5"),
        (4, 6, "blood_wizard_tower_spritelayout_4_6"),
        (4, 7, "blood_wizard_tower_spritelayout_4_7"),
        (5, 0, "blood_wizard_tower_spritelayout_5_0"),
        (5, 1, "blood_wizard_tower_spritelayout_5_1"),
        (5, 2, "blood_wizard_tower_spritelayout_5_2"),
        (5, 3, "blood_wizard_tower_spritelayout_5_3"),
        (5, 4, "blood_wizard_tower_spritelayout_5_4"),
        (5, 5, "blood_wizard_tower_spritelayout_5_5"),
        (5, 6, "blood_wizard_tower_spritelayout_5_6"),
        (5, 7, "blood_wizard_tower_spritelayout_5_7"),
        (6, 0, "blood_wizard_tower_spritelayout_6_0"),
        (6, 1, "blood_wizard_tower_spritelayout_6_1"),
        (6, 2, "blood_wizard_tower_spritelayout_6_2"),
        (6, 3, "blood_wizard_tower_spritelayout_6_3"),
        (6, 4, "blood_wizard_tower_spritelayout_6_4"),
        (6, 5, "blood_wizard_tower_spritelayout_6_5"),
        (6, 6, "blood_wizard_tower_spritelayout_6_6"),
        (6, 7, "blood_wizard_tower_spritelayout_6_7"),
        (7, 0, "blood_wizard_tower_spritelayout_7_0"),
        (7, 1, "blood_wizard_tower_spritelayout_7_1"),
        (7, 2, "blood_wizard_tower_spritelayout_7_2"),
        (7, 3, "blood_wizard_tower_spritelayout_7_3"),
        (7, 4, "blood_wizard_tower_spritelayout_7_4"),
        (7, 5, "blood_wizard_tower_spritelayout_7_5"),
        (7, 6, "blood_wizard_tower_spritelayout_7_6"),
        (7, 7, "blood_wizard_tower_spritelayout_7_7"),
    ],
)
