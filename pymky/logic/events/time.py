from time import monotonic


class Time:
    now = 0
    timeline = 0

    @classmethod
    def Now(cls) -> float:
        cls.now = monotonic()
        return cls.now
