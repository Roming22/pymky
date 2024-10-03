from time import sleep

from hardware.keypad import Keypad
from hardware.led import Leds
from logic.context import Context
from logic.eventmanager import EventManager


def blink() -> None:
    if not Context.count:
        return
    for led_id in range(Leds.count):
        Leds.Set(led_id, (255, 0, 0))
        Leds.Write()
        sleep(0.05)
        Leds.Set(led_id, (0, 0, 0))
        Leds.Write()
        sleep(0.05)


def scan() -> None:
    Keypad.Scan()
    EventManager.Process()
    blink()
