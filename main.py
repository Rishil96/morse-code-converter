# Text to Morse Code Converter

"""
Instructions to build International Morse Code
    1. The length of the dot is 1 unit.
    2. A dash is 3 units.
    3. The space between parts of the same letter is 1 unit.
    4. The space between letters is 3 units.
    5. The space between words is 7 units.
"""

DOT = "."
DASH = "-"

MORSE_CODE_MAP = {
    "a": f"{DOT}{DASH} ",
    "b": f"{DASH}{DOT}{DOT}{DOT} ",
    "c": f"{DASH}{DOT}{DASH}{DOT} ",
    "d": f"{DASH}{DOT}{DOT} ",
    "e": f"{DOT} ",
    "f": f"{DOT}{DOT}{DASH}{DOT} ",
    "g": f"{DASH}{DASH}{DOT} ",
    "h": f"{DOT}{DOT}{DOT}{DOT} ",
    "i": f"{DOT}{DOT} ",
    "j": f"{DOT}{DASH}{DASH}{DASH} ",
    "k": f"{DASH}{DOT}{DASH} ",
    "l": f"{DOT}{DASH}{DOT}{DOT} ",
    "m": f"{DASH}{DASH} ",
    "n": f"{DASH}{DOT} ",
    "o": f"{DASH}{DASH}{DASH} ",
    "p": f"{DOT}{DASH}{DASH}{DOT} ",
    "q": f"{DASH}{DASH}{DOT}{DASH} ",
    "r": f"{DOT}{DASH}{DOT} ",
    "s": f"{DOT}{DOT}{DOT} ",
    "t": f"{DASH} ",
    "u": f"{DOT}{DOT}{DASH} ",
    "v": f"{DOT}{DOT}{DOT}{DASH} ",
    "w": f"{DOT}{DASH}{DASH} ",
    "x": f"{DASH}{DOT}{DOT}{DASH} ",
    "y": f"{DASH}{DOT}{DASH}{DASH} ",
    "z": f"{DASH}{DASH}{DOT}{DOT} ",
    "1": f"{DOT}{DASH}{DASH}{DASH}{DASH} ",
    "2": f"{DOT}{DOT}{DASH}{DASH}{DASH} ",
    "3": f"{DOT}{DOT}{DOT}{DASH}{DASH} ",
    "4": f"{DOT}{DOT}{DOT}{DOT}{DASH} ",
    "5": f"{DOT}{DOT}{DOT}{DOT}{DOT} ",
    "6": f"{DASH}{DOT}{DOT}{DOT}{DOT} ",
    "7": f"{DASH}{DASH}{DOT}{DOT}{DOT} ",
    "8": f"{DASH}{DASH}{DASH}{DOT}{DOT} ",
    "9": f"{DASH}{DASH}{DASH}{DASH}{DOT} ",
    "0": f"{DASH}{DASH}{DASH}{DASH}{DASH} ",
    ".": f"{DOT}{DASH}{DOT}{DASH}{DOT}{DASH} ",
    ",": f"{DASH}{DASH}{DOT}{DOT}{DASH}{DASH} ",
    "?": f"{DOT}{DOT}{DASH}{DASH}{DOT}{DOT} ",
    "'": f"{DOT}{DASH}{DASH}{DASH}{DASH}{DOT} ",
    "!": f"{DASH}{DOT}{DASH}{DOT}{DASH}{DASH} ",
    "/": f"{DASH}{DOT}{DOT}{DASH}{DOT} ",
    "(": f"{DASH}{DOT}{DASH}{DASH}{DOT} ",
    ")": f"{DASH}{DOT}{DASH}{DASH}{DOT}{DASH} ",
    "&": f"{DOT}{DASH}{DOT}{DOT}{DOT} ",
    ":": f"{DASH}{DASH}{DASH}{DOT}{DOT}{DOT} ",
    ";": f"{DASH}{DOT}{DASH}{DOT}{DASH}{DOT} ",
    "=": f"{DASH}{DOT}{DOT}{DOT}{DASH} ",
    "+": f"{DOT}{DASH}{DOT}{DASH}{DOT} ",
    "-": f"{DASH}{DOT}{DOT}{DOT}{DOT}{DASH} ",
    "_": f"{DOT}{DOT}{DASH}{DASH}{DOT}{DASH} ",
    "\"": f"{DOT}{DASH}{DOT}{DOT}{DASH}{DOT} ",
    "$": f"{DOT}{DOT}{DOT}{DASH}{DOT}{DOT}{DASH} ",
    "@": f"{DOT}{DASH}{DASH}{DOT}{DASH}{DOT} ",
    " ": " " * 7
}

is_encoding = True

while is_encoding:
    sentence = input("Please type your sentence: ").lower()
    morse_coded_sentence = "".join([MORSE_CODE_MAP.get(character, character) for character in sentence])
    print(f"Morse Code of your input sentence:- \n{morse_coded_sentence}")
    continue_encoding = input("Press 'q' to quit encoding or any other key to continue: ").lower()
    if continue_encoding == "q":
        is_encoding = False

print("Exiting Morse Code Converter app!")
