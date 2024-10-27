from logic.events.event import Event
from logic.events.time import Time


class Switch:
    _debounce_delay = 20 * 1e-3
    _scan_func = None
    _switch_debounce = []
    _switch_value = []

    @classmethod
    def Init(cls, switch_count: int, scan_func: callable) -> None:
        cls._scan_func = scan_func
        cls._switch_debounce = [0 for _ in range(switch_count)]
        cls._switch_value = [False for _ in range(switch_count)]

    @classmethod
    def Scan(cls) -> None:
        now = Time.now
        for index, value in cls._scan_func():
            if value != cls._switch_value[index] and now > cls._switch_debounce[index]:
                cls._switch_debounce[index] = now + cls._debounce_delay
                cls._switch_value[index] = value
                Event(
                    now,
                    "switch",
                    (
                        index,
                        bool(value),
                    ),
                )
