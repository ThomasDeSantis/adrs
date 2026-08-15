from cargo import Cargo

cargo = Cargo(
    id="lambs",
    type_name="string(STR_CARGO_NAME_LAMBS)",
    unit_name="string(STR_CARGO_NAME_LAMBS)",
    type_abbreviation="string(STR_CID_LAMBS)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.1875",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="LAMB",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_ITEMS",
    items_of_cargo="string(STR_CARGO_UNIT_LAMBS)",
    penalty_lowerbound="0",
    single_penalty_length="0",
    price_factor=135,
    capacity_multiplier="1",
    icon_indices=(10, 5),
)
