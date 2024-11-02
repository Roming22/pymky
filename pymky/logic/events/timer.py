from logic.events.event import Event
from logic.events.time import Time


class Timer:
    _running: list["Timer"] = []

    def __init__(self, name: str, now: float, delay: float, timeline_id: str) -> None:
        # print("Timer:", name)
        self.end_at = now + delay
        self.name = name
        self.timeline_id = timeline_id
        Timer._running.append(self)

    def update(self) -> None:
        # print(f"    Timer: {self.name} updating")
        if Time.now <= self.end_at:
            return
        # print(f"    Timer: {self.name} triggered")
        Timer._running.remove(self)
        Event(Time.now, "timer", (self.name,), [self.timeline_id])

    def stop(self) -> None:
        try:
            Timer._running.remove(self)
        except ValueError:
            pass

    @classmethod
    def Scan(cls) -> None:
        for timer in list(cls._running):
            timer.update()
