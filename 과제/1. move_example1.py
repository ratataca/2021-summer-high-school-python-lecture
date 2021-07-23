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
