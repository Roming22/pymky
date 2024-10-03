from time import sleep

from hardware.keypad import Keypad
from hardware.led import Leds
from logic.context import Context


def blink() -> None:
    for led_id in range(Leds.count):
        Leds.Set(led_id, (255, 0, 0))
        Leds.Write()
        print("# ON")
        sleep(0.125)
        Leds.Set(led_id, (0, 0, 0))
        Leds.Write()
        print("# OFF")
        sleep(0.125)


def scan() -> None:
    e = Keypad.events.get()
    if e:
        if e.pressed:
            Context.count += 1
        else:
            Context.count -= 1
        print(Context.count)
    if Context.count:
        blink()
