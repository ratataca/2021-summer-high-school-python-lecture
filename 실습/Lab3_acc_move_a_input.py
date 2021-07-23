from roboid import *
import keyboard

hamster = Hamster()
count = 0


while True:
    if keyboard.is_pressed("w"):

        if count < 200:
            count += 10

        hamster.wheels(count, count)

        wait(30)

    else:
        count = 0
        hamster.wheels(0, 0)


hamster.stop()
