## * 주제 *
## 햄스터 로봇의 속도를 줄여보자


## 과제 2 :  햄스터의 속도를 빠르게 감소하는 방법을 생각해보자


from roboid import *

hamster = Hamster()


for i in range(100, 0, -1):
    hamster.wheels(i, i)
    wait(30)



hamster.stop()
