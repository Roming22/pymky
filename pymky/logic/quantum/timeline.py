class Timeline:
    def __init__(self, id: str) -> None:
        self.id = id
        self._forbidden_events = []
        self._timers = []
        self._commit_funcs = []

    def activate(self, now: float) -> None:
        raise NotImplementedError("Timeline.activate not implemented")

    def commit(self) -> None:
        for func in self._commit_funcs:
            func()

    def process(self, event_id: str) -> bool:
        print()
        print(f"## {self.id}: {event_id}")
        is_valid = True
        if self._forbidden_events:
            is_valid = event_id not in self._forbidden_events
        if not is_valid:
            for timer in self._timers:
                timer.stop()
        return is_valid
