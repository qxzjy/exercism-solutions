def is_valid(isbn: str) -> bool: 
    isbn = isbn.replace("-", "")
    sum = 0
    
    if len(isbn) != 10 or not isbn[:9].isdigit() or (isbn[-1].isalpha() and not isbn.endswith("X")):
        return False

    for index, digit in enumerate(reversed(isbn)):
        if digit == "X":
            digit = 10
        sum += (index+1)*int(digit)

    return not sum % 11
