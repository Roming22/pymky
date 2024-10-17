from logic.eventmanager import EventManager
from logic.events.time import Time


class Timer:
    _running: list["Timer"] = []

    def __init__(self, name: str, delay: float) -> None:
        # print("Timer:", name)
        self.end_at = Time.now + delay
        self.name = name
        Timer._running.append(self)

    def update(self) -> None:
        # print(f"    Timer: {self.name} updating")
        if Timer.now < self.end_at:
            return
        # print(f"    Timer: {self.name} triggered")
        Timer._running.remove(self)
        EventManager.AddEvent((Time.now, "timer", (self.name)))

    @classmethod
    def Scan(cls, now: float) -> None:
        Time.now = now
        for timer in list(cls._running):
            timer.update()
