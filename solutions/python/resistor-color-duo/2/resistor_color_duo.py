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

def value(colors: list[str]) -> int:
    """ For a resistor, determine the resistance associate to the colors.
 
    :param color: str - the colors.
    :return: int - the associate resistance.
    """
    
    return int(str(RESISTOR_COLORS.index(colors[0])) + str(RESISTOR_COLORS.index(colors[1])))
