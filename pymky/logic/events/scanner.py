from logic.events.switch import Switch
from logic.events.time import Time
from logic.events.timer import Timer


def scan() -> None:
    Time.Now()
    Switch.Scan()
    Timer.Scan()
