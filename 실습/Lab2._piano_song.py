# Melody
# author: Kwang-Hyun Park (akaii@kw.ac.kr)

from roboid import *

hamster = Hamster()

for i in range(2):
    for j in range(2):
        hamster.note("C4", 0.5)
        hamster.note("E4", 0.5)
        hamster.note("G4", 0.5)

    for j in range(3):
        hamster.note("A4", 0.5)

    hamster.note("G4", 1)
    hamster.note("off", 0.5)

    for j in range(3):
        hamster.note("F4", 0.5)

    for j in range(3):
        hamster.note("E4", 0.5)

    for j in range(3):
        hamster.note("D4", 0.5)

    hamster.note("C4", 1)
    hamster.note("off", 0.5)

    hamster.tempo(120) # speed up
