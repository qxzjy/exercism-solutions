ENDING = "ay"
VOWELS = "aeiou"

def pig(word: str) -> str:
    """
    Translate a word from English to Pig Latin.
 
    :param word: str - word to transalte.
    :return str - word translated in Pig Latin.
    """
    while not word[0] in VOWELS:
        if word[0] in "xy" and not word[1] in VOWELS:
            break
        word = word[1:] + word[0]
        if word[-1] == "q" and word[0] == "u":
            word = word[1:] + "u"
        
    return word + ENDING

def translate(sentence: str) -> str:
    """
    Translate a sentence from English to Pig Latin.
 
    :param sentence: str - sentence to transalte.
    :return str - sentence translated in Pig Latin.
    """        
    
    return " ".join([pig(word) for word in sentence.split()])
