from collections import deque

from logic.events.time import Time
from logic.quantum.timeline_manager import TimelineManager


class EventManager:
    _buffer = deque([], 32)

    @classmethod
    def AddEvent(cls, event: tuple) -> None:
        # print(f"Event: {event.id}")
        cls._buffer.append(event)

    @classmethod
    def Process(cls) -> None:
        while cls._buffer:
            event = cls._buffer.popleft()
            TimelineManager.Process(event)
