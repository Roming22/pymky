from logic.actions.key import Key as KeyAction
from logic.events.timer import Timer
from logic.quantum.timeline import Timeline


class TimelineTapHold(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        tap_timeline = TimelineTap(switch_id, key_definition[0])
        hold_timeline = TimelineHold(switch_id, key_definition[1])
        return [tap_timeline, hold_timeline]


class TimelineTap(Timeline):
    _delay = 300 * 1e-3

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> Timeline:
        timelines = [cls(switch_id, key_definition)]
        return timelines

    def __init__(self, switch_id: int, key_definition: str) -> None:
        super().__init__(f"timeline.{switch_id}.tap.{key_definition}")
        self._forbidden_events.append(f"timer.taphold.{switch_id}")
        self._commit_funcs.append(KeyAction.Load(switch_id, key_definition))

    def activate(self, now: float) -> None:
        switch_id = self.id.split(".")[1]
        self._timers.append(
            Timer(
                f"taphold.{switch_id}",
                now,
                self._delay,
                self.id,
            )
        )


class TimelineHold(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> Timeline:
        timelines = [cls(switch_id, key_definition)]
        return timelines

    def __init__(self, switch_id: int, key_definition: str) -> None:
        super().__init__(f"timeline.{switch_id}.hold.{key_definition}")
        self._forbidden_events.append(f"switch.{switch_id}.False")
        self._commit_funcs.append(KeyAction.Load(switch_id, key_definition))

    def activate(self, now: float) -> None:
        pass
