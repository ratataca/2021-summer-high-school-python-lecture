
## * 주제 *
## 각 2초동안 직진, 후진, 좌우로 햄스터 로봇 이동하자!

## 과제 1 :  해당 코드를 실행해보자
## 과제 2 :  move_example1에서 사용한 hamster.wheels(50, 50)와 비교하여 생각해보자

from roboid import *

hamster = Hamster()


# 1. 직진하기
hamster.move_forward(2, 50)


# 2. 뒤로가기
hamster.move_backward(2, 60)


# 3. 오른쪽 회전하기
hamster.turn_right(2, 60)


# 4. 왼쪽 회전하기
hamster.turn_left(2, 60)



# 실행 종료 후 멈추기
hamster.stop()
