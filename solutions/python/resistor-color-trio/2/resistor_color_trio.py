RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

UNITS = ["ohms", "kiloohms", "megaohms", "gigaohms"]

def label(colors: list[str]) -> str:
    """ For a resistor, determine the resistance associate to the colors
    with the metric prefix added.
 
    :param color: str - the colors.
    :return: int - the associate resistance.
    """
    if len(colors) > 3:
        *values, multiplier = colors[0], colors[1], RESISTOR_COLORS[0], colors[-1]
    else:
        *values, multiplier = colors
    
    # Add the bands, apply the multiplier.
    val = 0.0
    for value in values:
        val = val * 10 + RESISTOR_COLORS.index(value)
    val *= 10 ** RESISTOR_COLORS.index(multiplier)
    
    # Shift numbers over to get the proper prefix.
    power = 0
    while val >= 1000:
        val /= 1000
        power += 1
        
    # Add a tolerance, if one is supplied.
    result = f"{val:n} {UNITS[power]}"
    
    return result
