import time

import digitalio
from hardware.board import board
from logic.eventmanager import EventManager


class Keypad:
    count = 0
    __cols = []
    __rows = []
    __debounce_delay = 5 * 1e-3
    __switch_debounce = []
    __switch_value = []

    @classmethod
    def Init(cls) -> None:
        def init_col(pin):
            io = digitalio.DigitalInOut(pin)
            io.direction = digitalio.Direction.INPUT
            io.pull = digitalio.Pull.UP
            return io

        def init_row(pin):
            io = digitalio.DigitalInOut(pin)
            io.direction = digitalio.Direction.OUTPUT
            io.drive_mode = digitalio.DriveMode.PUSH_PULL
            io.value = 0
            return io

        cls.__cols = [init_col(pin) for pin in board["pins"]["cols"]]
        cls.__rows = [init_row(pin) for pin in board["pins"]["rows"]]
        cls.count = len(cls.__cols) * len(cls.__rows)
        cls.__switch_debounce = [0 for _ in range(cls.count)]
        cls.__switch_value = [False for _ in range(cls.count)]

    @classmethod
    def _Matrix_Scan(cls):
        index = -1
        for row in cls.__rows:
            row.value = 0
            for col in cls.__cols:
                index += 1
                yield index, not col.value
            row.value = 1

    @classmethod
    def Scan(cls) -> None:
        now = time.monotonic()
        for index, value in cls._Matrix_Scan():
            if (
                value != cls.__switch_value[index]
                and now > cls.__switch_debounce[index]
            ):
                cls.__switch_debounce[index] = now + cls.__debounce_delay
                cls.__switch_value[index] = value
                event = (
                    now,
                    (
                        "switch",
                        index + 1,
                        value,
                    ),
                )
                EventManager.AddEvent(event)
