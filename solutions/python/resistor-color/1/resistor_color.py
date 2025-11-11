RESISTOR_COLORS = ["black",
                   "brown",
                   "red",
                   "orange",
                   "yellow",
                   "green",
                   "blue",
                   "violet",
                   "grey",
                   "white"]

def color_code(color: str) -> int:
    """ For a resistor, determine the resistance associate to the color.
 
    :param color: str - the color.
    :return: int - the associate resistance.
    """
    
    return RESISTOR_COLORS.index(color)


def colors() -> list[str]:
    """ For a resistor, return every possible colors for a resistance.

    :return: list[str] - every possible colors for a resistance.
    """
    
    return RESISTOR_COLORS
