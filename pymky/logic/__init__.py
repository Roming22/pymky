from hardware.led import Leds
from logic.eventmanager import EventManager
from logic.events import scan
from logic.events.keypad import Keypad


def init() -> None:
    Keypad.Init()
    Leds.Init()


def tick() -> None:
    scan()
    EventManager.Process()
    blink()


from logic.context import Context


def blink() -> None:
    red = 255 if Context.count else 0
    for led_id in range(Leds.count):
        Leds.Set(led_id, (red, 0, 0))
    Leds.Write()
