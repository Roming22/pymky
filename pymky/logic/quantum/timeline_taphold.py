from logic.actions.key import Key as KeyAction
from logic.events.timer import Timer
from logic.quantum.timeline import Timeline


class TimelineTapHold(Timeline):
    _delay = 300 * 1e-3

    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        tap_timeline = cls(switch_id, key_definition[0], tap=True)
        hold_timeline = cls(switch_id, key_definition[1], tap=False)
        return [tap_timeline, hold_timeline]

    def __init__(self, switch_id: int, key_definition: str, tap: bool) -> None:
        if tap:
            self.id = f"timeline.{switch_id}.tap.{key_definition}"
            self._forbidden_events = [f"timer.taphold.{switch_id}"]
            self.activate = lambda now: Timer(
                f"taphold.{switch_id}",
                now,
                self._delay,
            )
        else:
            self.id = f"timeline.{switch_id}.hold.{key_definition}"
            self._forbidden_events = [f"switch.{switch_id}.False"]
        self.valid = True
        self.commit = KeyAction.Load(switch_id, key_definition)

    def activate(self, now: float) -> None:
        pass
