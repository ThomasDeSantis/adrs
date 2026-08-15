from cargo import Cargo

cargo = Cargo(
    id="tanks",
    type_name="string(STR_CARGO_NAME_TANKS)",
    unit_name="string(STR_CARGO_NAME_TANKS)",
    type_abbreviation="string(STR_CID_TANKS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS, CC_OVERSIZED)",
    cargo_label="TANK",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_TANKS)",
    penalty_lowerbound="15",
    single_penalty_length="128",
    capacity_multiplier="1",
    price_factor=166,
    icon_indices=(13, 5),
)
