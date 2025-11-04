IGNORED_CHAR = [" ", "-"]
def is_isogram(sentence: str) -> bool:
    
    stack = []

    for char in sentence.lower():
        if char not in stack:
            if char not in IGNORED_CHAR:
                stack.append(char)
        else:
            return False

    return True