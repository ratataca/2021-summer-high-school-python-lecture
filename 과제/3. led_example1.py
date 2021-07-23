## * 주제 *
## 햄스터 로봇의 LED를 켜보자(방향 : 로봇과 정면으로 마주는 보는 방향)

## 과제 1 :  해당 코드를 실행해보자
## 과제 2 :  7가지 색을 출력하며 앞으로 이동해보자

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
