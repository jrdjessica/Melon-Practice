############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    # melon types: Muskmelon, Casaba, Crenshaw, Yellow Watermelon
    # code, name, first_harvest, color, is_seedless, is_bestseller

    musk = MelonType(
        "musk",
        "Muskmelon",
        1998,
        "green",
        True,
        True
    )
    musk.add_pairing("mint")

    casaba = MelonType(
        "cas",
        "Casaba",
        2003,
        "orange",
        False,
        False
    )
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")

    crenshaw = MelonType(
        "cren",
        "Crenshaw",
        1996,
        "green",
        False,
        False
    )
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType(
        "yw",
        "Yellow Watermelon",
        2013,
        "yellow",
        False,
        True
    )
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types = [musk, casaba,
                       crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with:")
        for pairing in melon.pairings:
            print(f"- {pairing}")


melon_list = make_melon_types()
# print_pairing_info(melon_list)
# print()
# print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code.

    ex:
    {self.code : objectname} --> {cas : casaba}

    """

    melon_code_dict = {}

    for melon in melon_types:
        melon_code_dict[melon.code] = melon
    return melon_code_dict


# print(make_melon_type_lookup(melon_list))
melons_by_id = make_melon_type_lookup((melon_list))


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, field, harvester):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):

        is_sellable = False

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            is_sellable = True

        return is_sellable


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon1 = Melon(
        melons_by_id["yw"],
        8,
        7,
        2,
        "Sheila"
    )

    melon2 = Melon(
        melons_by_id["yw"],
        3,
        4,
        2,
        "Sheila"
    )

    melon3 = Melon(
        melons_by_id["yw"],
        9,
        8,
        3,
        "Sheila"
    )

    melon4 = Melon(
        melons_by_id["cas"],
        10,
        6,
        35,
        "Sheila"
    )

    melon5 = Melon(
        melons_by_id["cren"],
        8,
        9,
        35,
        "Michael"
    )

    melon6 = Melon(
        melons_by_id["cren"],
        8,
        2,
        35,
        "Michael"
    )

    melon7 = Melon(
        melons_by_id["cren"],
        2,
        3,
        4,
        "Michael"
    )

    melon8 = Melon(
        melons_by_id["musk"],
        6,
        7,
        4,
        "Michael"
    )

    melon9 = Melon(
        melons_by_id["yw"],
        7,
        10,
        3,
        "Sheila"
    )

    melon_harvest_list = [melon1, melon2, melon3,
                          melon4, melon5, melon6, melon7, melon8, melon9]

    return melon_harvest_list


melon_harvest_list = make_melons(melon_list)
# print(melon_harvest_list)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable() == True:
            sellable = "(CAN BE SOLD)"
        else:
            sellable = "(NOT SELLABLE)"
        print(
            f"Harvested by {melon.harvester} from Field {melon.field} {sellable}")


get_sellability_report(melon_harvest_list)
