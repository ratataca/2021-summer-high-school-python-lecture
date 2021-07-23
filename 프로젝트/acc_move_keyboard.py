## * 주제 *
## 햄스터 로봇의 속도를 줄여보자


## 과제 2 :  햄스터의 속도를 빠르게 감소하는 방법을 생각해보자


from roboid import *
import keyboard

hamster = Hamster()
count = 0
is_pressed_key = ""

while True:
    if keyboard.is_pressed("w"):
        if is_pressed_key != "w":
            count = 0
        if count < 200:
            count += 10
        hamster.wheels(count, count)
        is_pressed_key = "w"
        wait(30)

    elif keyboard.is_pressed("a"):
        if is_pressed_key != "a":
            count = 0
        if count < 200:
            count += 3
        hamster.wheels(-count, count)
        is_pressed_key = "a"
        wait(30)

    elif keyboard.is_pressed("d"):
        if is_pressed_key != "d":
            count = 0
        if count < 200:
            count += 3
        hamster.wheels(count, -count)
        is_pressed_key = "d"
        wait(30)

    else:
        count = 0
        hamster.wheels(0, 0)


hamster.stop()
