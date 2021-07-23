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
