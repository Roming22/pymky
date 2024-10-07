from time import sleep

from hardware.keypad import Keypad
from hardware.led import Leds
from logic.context import Context
from logic.eventmanager import EventManager


def blink() -> None:
    red = 255 if Context.count else 0
    for led_id in range(Leds.count):
        Leds.Set(led_id, (red, 0, 0))
    Leds.Write()


def scan() -> None:
    Keypad.Scan()
    EventManager.Process()
    blink()
