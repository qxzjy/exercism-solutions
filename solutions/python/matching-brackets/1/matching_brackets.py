BRACKETS = {"(": ")",
            "{": "}",
            "[": "]"}

def is_paired(input_string: str) -> bool:
    """
    Determine if a string input have correctly paired brackets.
 
    :param input_string: str - input string to be analyzed.
    :return bool - is the input string brackets are correctly paired ?
    """
    brackets_stack = []
    
    for char in input_string:
    	if char in BRACKETS.keys():
    		brackets_stack.append(BRACKETS[char])
    	elif char in BRACKETS.values():
    		if not brackets_stack or char != brackets_stack.pop():
    			return False
                
    return not brackets_stack