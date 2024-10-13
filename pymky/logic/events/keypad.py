from hardware.keypad import Keypad as HwKeypad
from logic.eventmanager import EventManager


class Keypad:
    __debounce_delay = 5 * 1e-3
    __switch_debounce = []
    __switch_value = []

    @classmethod
    def Init(cls) -> None:
        HwKeypad.Init()
        cls.__switch_debounce = [0 for _ in range(HwKeypad.count)]
        cls.__switch_value = [False for _ in range(HwKeypad.count)]

    @classmethod
    def Scan(cls, now) -> None:
        for index, value in HwKeypad.Matrix_Scan():
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
