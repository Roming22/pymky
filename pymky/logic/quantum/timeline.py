class Timeline:
    def __init__(self, forbidden_events: list[str], activate_func: callable) -> None:
        self._forbidden_events = forbidden_events
        self.valid = True
        self.activate = activate_func

    def activate(self, now: float) -> None:
        raise NotImplemented("Timeline.activate not implemented")

    def commit(self) -> None:
        raise NotImplemented("Timeline.commit not implemented")

    def process(self, event_id: str) -> bool:
        # _not = " not" if event_id not in self._forbidden_events else ""
        # print(f"{self.id}: {event_id}{_not} in {self._forbidden_events}")
        return event_id not in self._forbidden_events
