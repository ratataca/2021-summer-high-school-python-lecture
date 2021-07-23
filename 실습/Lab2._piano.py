# Keyboard Piano
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

# Ctrl + C to terminate

from roboid import *

hamster = Hamster()
notes = {
    " ": "off",
    "a": "C4",
    "w": "C#4",
    "s": "D4",
    "e": "Eb4",
    "d": "E4",
    "f": "F4",
    "t": "F#4",
    "g": "G4",
    "y": "G#4",
    "h": "A4",
    "u": "Bb4",
    "j": "B4",
    "k": "C5",
    "o": "C#5",
    "l": "D5",
    "p": "Eb5",
    ";": "E5",
    "'": "F5"
}

while True:
    key = input()
    if key and key in notes:
        hamster.note("off", 0.05) # break for the same notes
        hamster.note(notes[key])
    wait(10) # 10 msec
