from hardware.board import board
from keypad import KeyMatrix


class Keypad:
    count = 0
    events = None
    __km = None

    @classmethod
    def Init(cls):
        cls.__km = KeyMatrix(
            row_pins=board["pins"]["rows"],
            column_pins=board["pins"]["cols"],
            interval=0.001,
            debounce_threshold=16,
        )
        cls.count = cls.__km.key_count
        cls.events = cls.__km.events

    @classmethod
    def Reset(cls, pixel_id, rgb):
        cls.__km.reset()
