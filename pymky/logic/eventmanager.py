from collections import deque

from logic.actions.switch import Switch
from logic.events.time import Time


class EventManager:
    _buffer = deque([], 32)

    @classmethod
    def AddEvent(cls, event: tuple) -> None:
        cls._buffer.append(event)

    @classmethod
    def Process(cls) -> None:
        while cls._buffer:
            Time.now, event_type, event_data = cls._buffer.popleft()
            if event_type == "switch":
                Switch.Process(event_data)
