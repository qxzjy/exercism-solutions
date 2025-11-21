from re import sub

def decode(text):
    
    return sub(r"(\d+)(\D)", lambda c: c.group(2) * int(c.group(1)), text)
    
def encode(text):
    
    return sub(r"(.)\1+", lambda c: str(len(c.group(0))) + c.group(1), text)