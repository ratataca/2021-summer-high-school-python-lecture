
from roboid import *

hamster = Hamster()

buzzer_hz = 0
while True:
    #proximity = hamster.left_proximity()
    proximity = hamster.right_proximity()

    if proximity < 10:
        proximity = 0
    buzzer_hz = (buzzer_hz * 5 + proximity * 70) / 10.0
    hamster.buzzer(buzzer_hz)

    wait(20)



