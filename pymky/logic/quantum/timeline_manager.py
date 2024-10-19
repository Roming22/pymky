from logic.actions.layer import Layer
from logic.actions.switch import Switch
from logic.events.event import Event
from logic.events.time import Time


class TimelineManager:
    _timelines = []

    @classmethod
    def IsResolved(cls) -> bool:
        return not cls._timelines

    @classmethod
    def Process(cls, event: Event) -> None:
        print(f"Event: {event.id} @{event.time}")
        if cls.IsResolved() and event.type == "switch":
            switch_id, state = event.data
            if state:
                cls._timelines = Layer.Process(switch_id)
        else:
            cls.ToTimelines(event.id)
        cls.Resolve(event.time)
        if cls.IsResolved() and event.type == "switch":
            Switch.Process(event)

    @classmethod
    def Resolve(cls, timestamp: float) -> None:
        if len(cls._timelines) == 1:
            Time.timeline = timestamp
            cls._timelines[0].activate(timestamp)
            cls._timelines.clear()

    @classmethod
    def ToTimelines(cls, event_id) -> None:
        for index, timeline in enumerate(reversed(cls._timelines)):
            if not timeline.process(event_id):
                cls._timelines.pop(-1 - index)
