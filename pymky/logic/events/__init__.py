import time

from logic.events.switch import Switch
from logic.events.timer import Timer


def scan() -> None:
    now = time.monotonic()
    Switch.Scan(now)
    Timer.Scan(now)
