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
