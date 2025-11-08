import string

PLAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHER_ALPHABET = PLAIN_ALPHABET[::-1]
SEQUENCE_LENGTH = 5

def cleanup(text: str) -> str:
    """
    Clean up a text by removing punctuation and converting it to lowercase.
 
    :param text: str - text to clean.
    :return: str - the texte cleaned.
    """
    
    return "".join(char.lower() for char in text if char.isalnum())

def encode(plain_text: str) -> str:
    """
    Encrypt a text using the Atbash cipher.

    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
 
    :param plain_text: str - text to encrypt.
    :return: str - the texte encrypted.
    """
    plain_text = cleanup(plain_text)

    cyphered_text = plain_text.translate(str.maketrans(PLAIN_ALPHABET, CIPHER_ALPHABET))

    return " ".join(cyphered_text[index:index+SEQUENCE_LENGTH] for index in range(0, len(cyphered_text), SEQUENCE_LENGTH))


def decode(ciphered_text: str) -> str:
    """
    Decrypt a ciphered text using the Atbash cipher.

    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
 
    :param ciphered_text: str - text to decrypt.
    :return: str - the texte decrypted.
    """
    
    return "".join(ciphered_text.split()).translate(str.maketrans(CIPHER_ALPHABET, PLAIN_ALPHABET))
