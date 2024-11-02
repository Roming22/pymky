class Event:
    events = []

    def __init__(
        self, time: float, type: str, data: tuple, timeline_ids: list[str] = []
    ) -> None:
        self.time = time
        self.type = type
        self.data = data
        self.id = f"{type}.{".".join([str(d) for d in data])}"
        self.timeline_ids = timeline_ids
        Event.events.append(self)
