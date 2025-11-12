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

def label(colors: list[str]) -> str:
    """ For a resistor, determine the resistance associate to the colors
    with the metric prefix added.
 
    :param color: str - the colors.
    :return: int - the associate resistance.
    """
    ohms = (10 * RESISTOR_COLORS.index(colors[0]) + RESISTOR_COLORS.index(colors[1])) * (10 ** RESISTOR_COLORS.index(colors[2]))
    
    if ohms > 1_000_000_000:
        prefix = "giga"
        ohms //= 1_000_000_000
    elif ohms > 1_000_000:
        prefix = "mega"
        ohms //= 1_000_000
    elif ohms > 1_000:
        prefix = "kilo"
        ohms //= 1_000
    else:
        prefix = ""
    
    return f"{ohms} {prefix}ohms"
