from logic.eventmanager import EventManager


class Switch:
    _debounce_delay = 5 * 1e-3
    _scan_func = None
    _switch_debounce = []
    _switch_value = []

    @classmethod
    def Init(cls, switch_count: int, scan_func: callable) -> None:
        cls._scan_func = scan_func
        cls._switch_debounce = [0 for _ in range(switch_count)]
        cls._switch_value = [False for _ in range(switch_count)]

    @classmethod
    def Scan(cls, now: float) -> None:
        for index, value in cls._scan_func():
            if value != cls._switch_value[index] and now > cls._switch_debounce[index]:
                cls._switch_debounce[index] = now + cls._debounce_delay
                cls._switch_value[index] = value
                event = (
                    now,
                    "switch",
                    (
                        index,
                        value,
                    ),
                )
                EventManager.AddEvent(event)
