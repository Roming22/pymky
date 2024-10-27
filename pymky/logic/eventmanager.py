from logic.events.event import Event
from logic.quantum.timeline_manager import TimelineManager


class EventManager:
    @classmethod
    def Process(cls) -> None:
        while Event.events:
            event = Event.events.pop()
            TimelineManager.Process(event)
