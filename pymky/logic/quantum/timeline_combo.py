from logic.actions.key import Key as KeyAction
from logic.events.event import Event
from logic.events.time import Time
from logic.events.timer import Timer
from logic.quantum.timeline import Timeline


class TimelineCombo(Timeline):
    _delay = 40 * 1e-3

    @classmethod
    def Load(cls, switch_ids: tuple[int], key_definition: str) -> list:
        timeline = cls(switch_ids, key_definition)
        return [timeline]

    def __init__(self, switch_ids: tuple[int], key_definition: str) -> None:
        id = "-".join([str(s) for s in switch_ids])
        super().__init__(f"timeline.combo.{id}.{key_definition}")
        self._valid_events.extend([f"switch.{s}.True" for s in switch_ids])
        for switch_id in switch_ids:
            self._commit_funcs.append(KeyAction.Load(switch_id, key_definition))

    def activate(self, now: float) -> None:
        id = self.id.split(".")[2]
        self._pending_events = self._valid_events.copy()
        self._timers.append(
            Timer(
                f"combo.{id}",
                now,
                self._delay,
                self.id,
            )
        )

    def process(self, event_id: str) -> bool:
        is_valid = super().process(event_id)
        if is_valid and self._pending_events:
            self._pending_events.remove(event_id)
            if not self._pending_events:
                Event(Time.now, "combo", ("activated",))
                for timer in self._timers:
                    timer.stop()
        return is_valid
