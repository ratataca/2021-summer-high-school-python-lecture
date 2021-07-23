from roboid import *

hamster = Hamster()


for i in range(100, 0, -1):
    hamster.wheels(i, i)
    wait(30)



hamster.stop()
