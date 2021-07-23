## * 주제 *
## 햄스터 로봇의 LED를 켜보자(방향 : 로봇과 정면으로 마주는 보는 방향)

## 과제 1 :  해당 코드를 실행해보자
## 과제 2 :  7가지 색을 출력하며 앞으로 이동해보자

from roboid import *

hamster = Hamster()

hamster.wheels(50)
hamster.left_led(Hamster.LED_BLUE)
wait(500)
hamster.right_led(Hamster.LED_GREEN)
wait(500)

hamster.wheels(-50, -50)
hamster.left_led(Hamster.LED_CYAN)
wait(500)
hamster.right_led(Hamster.LED_RED)
wait(500)

hamster.wheels(-50, 50)
hamster.left_led(Hamster.LED_MAGENTA)
wait(500)
hamster.right_led(Hamster.LED_YELLOW)
wait(500)

hamster.wheels(50, -50)
hamster.leds(Hamster.LED_WHITE, Hamster.LED_WHITE)
wait(500)

# 실행 종료 후 멈추기
hamster.stop()
