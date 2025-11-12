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

RESISTOR_TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

UNITS = ["ohms", "kiloohms", "megaohms", "gigaohms"]

def resistor_label(colors: list[str]) -> str:
    """ For a resistor, determine the resistance associate to the colors
    with the metric prefix and tolerance added.
 
    :param color: str - the colors.
    :return: int - the associate resistance.
    """
    
    # Unpack or set up variables.
    if len(colors) > 3:
        *values, multiplier, tolerance = colors
    else:
        values, multiplier, tolerance = colors, RESISTOR_COLORS[0], None
        
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
    
    if tolerance:
        result += f" ±{RESISTOR_TOLERANCES[tolerance]}%"
        
    return result