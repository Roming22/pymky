from logic.eventmanager import EventManager


class Timer:
    _now = 0
    _running: list["Timer"] = []

    def __init__(self, name: str, delay: float) -> None:
        # print("Timer:", name)
        self.end_at = Timer.now + delay
        self.name = name
        Timer._running.append(self)

    def update(self) -> None:
        # print(f"    Timer: {self.name} updating")
        if Timer._now < self.end_at:
            return
        # print(f"    Timer: {self.name} triggered")
        Timer._running.remove(self)
        EventManager.AddEvent((Timer._now, "timer", (self.name)))

    @classmethod
    def Scan(cls, now: float) -> None:
        cls._now = now
        for timer in list(cls._running):
            timer.update()
