from time import monotonic as get_time

from logic.events.switch import Switch
from logic.events.timer import Timer


def scan() -> None:
    now = get_time()
    Switch.Scan(now)
    Timer.Scan(now)
