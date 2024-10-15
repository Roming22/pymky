from logic.eventmanager import EventManager


class Timer:
    now = 0
    running: list["Timer"] = []

    def __init__(self, name: str, delay: float) -> None:
        # print("Timer:", name)
        self.end_at = Timer.now + delay
        self.name = name
        Timer.running.append(self)

    def update(self) -> None:
        # print(f"    Timer: {self.name} updating")
        if Timer.now < self.end_at:
            return
        # print(f"    Timer: {self.name} triggered")
        Timer.running.remove(self)
        EventManager.AddEvent((Timer.now, ("timer", self.name)))

    @classmethod
    def Scan(cls, now: float) -> None:
        cls.now = now
        for timer in list(cls.running):
            timer.update()
