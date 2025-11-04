def is_pangram(sentence: str) -> bool:

    stack = set()

    for char in sentence.lower():
        if char.isalpha():
            stack.add(char)           
    
    return len(stack) == 26