
## * 주제 *
## 각 2초동안 직진, 후진, 좌우로 햄스터 로봇 이동하자!

## 과제 1 :  해당 코드를 실행해보자
## 과제 2 :  50 숫자를 증가시켜 어떤 변화가 있는지 살펴보자.


from roboid import *

hamster = Hamster()


hamster.wheels(-50, 0)
wait(2000)

# 1. 직진하기
hamster.wheels(50, 50)
wait(2000)

# 2. 뒤로가기
hamster.wheels(-50, -50)
wait(2000)


# 3. 오른쪽 회전하기
hamster.wheels(50, -50)
wait(2000)


# 4. 왼쪽 회전하기
hamster.wheels(-50, 50)
wait(2000)


# 실행 종료 후 멈추기
hamster.stop()
