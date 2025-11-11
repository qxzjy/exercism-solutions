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
        
    
    return int(str(RESISTOR_COLORS.index(colors[0])) + str(RESISTOR_COLORS.index(colors[1])))
