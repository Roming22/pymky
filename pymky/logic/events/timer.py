from logic.eventmanager import EventManager
from logic.events.event import Event
from logic.events.time import Time


class Timer:
    _running: list["Timer"] = []

    def __init__(self, name: str, delay: float) -> None:
        # print("Timer:", name)
        self.end_at = Time.timeline + delay
        self.name = name
        Timer._running.append(self)

    def update(self) -> None:
        # print(f"    Timer: {self.name} updating")
        if Time.now <= self.end_at:
            return
        # print(f"    Timer: {self.name} triggered")
        Timer._running.remove(self)
        event = Event(Time.now, "timer", (self.name))
        EventManager.AddEvent(event)

    @classmethod
    def Scan(cls) -> None:
        for timer in list(cls._running):
            timer.update()
