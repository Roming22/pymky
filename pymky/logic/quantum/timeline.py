class Timeline:
    def __init__(self) -> None:
        self._forbidden_events = []
        self._timers = []

    def activate(self, now: float) -> None:
        raise NotImplementedError("Timeline.activate not implemented")

    def commit(self) -> None:
        raise NotImplementedError("Timeline.commit not implemented")

    def process(self, event_id: str) -> bool:
        # _not = " not" if event_id not in self._forbidden_events else ""
        # print(f"{self.id}: {event_id}{_not} in {self._forbidden_events}")
        is_valid = event_id not in self._forbidden_events
        if not is_valid:
            for timer in self._timers:
                timer.stop()
        return is_valid
