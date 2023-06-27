"""
Morse code encoder/decoder
"""

MORSE_TABLE = {
    'A':".-",
    'B':"-...",
    'C':"-.-.",
    'D':"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",

    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",

    " ":"/"
    }



def encode_morse(text)->str:
    """
    Given a string, returns the morse code equivalent

    Args:
        text: string to encode
    
    Returns:
        morse: encoded string in morse code
    """
    chars = [char for char in text.upper()]
    morse = " ".join([MORSE_TABLE[char] for char in chars])
    return morse


def decode_morse(code)->str:
    """
    Given morse code, returns the original string

    Args:
        code: morse code to decode

    Returns:
        decoded: decoded morse code
    """
    morse_inverse = dict((morse, letter) for letter, morse in MORSE_TABLE.items())
    morse_inverse['/']=" "
    morse_inverse['']=''
    
    morse_list = code.split(" ")
    decoded = "".join([morse_inverse[code] for code in morse_list])
    return decoded