from logic.quantum.timeline import Timeline


class TimelineKey(Timeline):
    def __init__(self, action: callable) -> None:
        self._forbidden_events = []
        self.valid = True
        self.activate = action
