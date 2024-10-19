class Timeline:
    def __init__(self, forbidden_events: list[str], activate_func: callable) -> None:
        self._forbidden_events = forbidden_events
        self.valid = True
        self.activate = activate_func

    def activate(self, timestamp: float) -> None:
        raise NotImplemented("Timeline.activate not implemented")

    def process(self, event_id: str) -> bool:
        return event_id not in self._forbidden_events
