from roboid import *

hamster = Hamster()


# 1. 왼쪽 LED 켜기
hamster.left_led("blue")
wait(500)

hamster.left_led("off")
wait(500)


# 2. 오른쪽 LED 켜기
hamster.right_led("yellow")
wait(500)

hamster.right_led("off")
wait(500)


# 3. 양쪽 LED 모두 켜기
hamster.leds("red", "green")
wait(500)


hamster.leds("off")


# 실행 종료 후 멈추기
hamster.stop()
