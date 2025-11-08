import string

PLAIN_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHER_ALPHABET = PLAIN_ALPHABET[::-1]
SEQUENCE_LENGTH = 5

def encode(plain_text: str) -> str:
    """
    Encrypt a text using the Atbash cipher.

    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
 
    :param plain_text: str - text to encrypt.
    :return: str - the texte encrypted.
    """
    encode = str.maketrans(PLAIN_ALPHABET + PLAIN_ALPHABET.upper(),
                           CIPHER_ALPHABET + CIPHER_ALPHABET)
    
    plain_text = "".join(plain_text.translate(str.maketrans("", "", string.punctuation)).split())

    cyphered_text = "".join(plain_text.translate(encode).split())

    return " ".join([cyphered_text[index:index+SEQUENCE_LENGTH] for index in range(0, len(cyphered_text), SEQUENCE_LENGTH)])


def decode(ciphered_text: str) -> str:
    """
    Decrypt a ciphered text using the Atbash cipher.

    Plain:  abcdefghijklmnopqrstuvwxyz
    Cipher: zyxwvutsrqponmlkjihgfedcba
 
    :param ciphered_text: str - text to decrypt.
    :return: str - the texte decrypted.
    """
    decode = str.maketrans(CIPHER_ALPHABET + CIPHER_ALPHABET.upper(),
                           PLAIN_ALPHABET + PLAIN_ALPHABET)
    
    return "".join(ciphered_text.split()).translate(decode)