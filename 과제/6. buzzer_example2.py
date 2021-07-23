

## * 주제 *
## 버저를 통해 여러 주파수의 소리를 내보자
## 소리 범위는 Hamster.NOTE_A_0 ~ Hamster.NOTE_C_8(0옥타브 라~8옥타브 도)

## 과제 1 :  버저의 값을 바꿔 자신 가청 주파수는 얼마인지 측정해보자
## 과제 2 :  버저의 음정을 이용하여 악기 연주를 해보자

from roboid import *

hamster = Hamster()

hamster.note(Hamster.NOTE_C_1)
wait(1000)

hamster.note(Hamster.NOTE_C_2)
wait(1000)

hamster.note(Hamster.NOTE_C_3)
wait(1000)

hamster.note(Hamster.NOTE_C_4)
wait(1000)

hamster.note(Hamster.NOTE_C_5)
wait(1000)

hamster.note(Hamster.NOTE_C_6)
wait(1000)

hamster.note(Hamster.NOTE_C_7)
wait(1000)

# 실행 종료 후 멈추기
hamster.stop()




