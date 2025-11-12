ACTIONS = [
    "jump",
    "close your eyes",
    "double blink",
    "wink"
]

def commands(binary_str: str) -> list[str]:
    """ Convert binary number into a sequence of actions.
 
    :param binary_str: str - the binary number in string format.
    :return: list[str] - the sequence of actions.
    """
    handshake = list()

    for index, digit in enumerate(binary_str[1:]):
        if int(digit) == 1:
            handshake.append(ACTIONS[index])
    
    return list(reversed(handshake)) if int(binary_str[0]) != 1 else handshake
