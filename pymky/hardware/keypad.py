from collections import deque

from hardware.board import board
from keypad import Event, KeyMatrix
from logic.eventmanager import EventManager


class Keypad:
    count = 0
    __keys = None
    __pool = deque([Event()] * 64, 64)

    @classmethod
    def Init(cls) -> None:
        cls.__keys = KeyMatrix(
            row_pins=board["pins"]["rows"],
            column_pins=board["pins"]["cols"],
            interval=0.001,
            debounce_threshold=25,
        )
        cls.count = cls.__keys.key_count

    @classmethod
    def Release(cls, event) -> None:
        cls.__pool.append(event)

    @classmethod
    def Reset(cls) -> None:
        cls.__keys.reset()

    @classmethod
    def Scan(cls) -> None:
        event = cls.__pool.pop()
        while cls.__keys.events.get_into(event):
            EventManager.AddEvent(event)
            event = cls.__pool.pop()
        cls.Release(event)
