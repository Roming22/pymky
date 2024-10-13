import time

from logic.events.keypad import Keypad
from logic.events.timer import Timer


def scan() -> None:
    now = time.monotonic()
    Keypad.Scan(now)
