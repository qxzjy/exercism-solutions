PLAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text: str, key: int) -> str:
    """
    Translate a word or sentence using the Caesar cipher.
 
    :param text: str - the word or sentence to transalte.
    :param key: int - the Caesar cipher key.
    :return: str - the word or sentence transalted.
    """
    cipher_alphabet = PLAIN_ALPHABET[key:] + PLAIN_ALPHABET[:key]
    
    translation = str.maketrans(PLAIN_ALPHABET + PLAIN_ALPHABET.upper(),
                          cipher_alphabet + cipher_alphabet.upper())
    
    return text.translate(translation)