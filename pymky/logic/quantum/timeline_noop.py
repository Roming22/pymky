from logic.actions.noop import NoOp as NoOpAction
from logic.quantum.timeline import Timeline


class TimelineNoOp(Timeline):
    @classmethod
    def Load(cls, switch_id: int, _: tuple) -> list:
        timelines = [cls(switch_id)]
        return timelines

    def __init__(self, switch_id: int) -> None:
        super().__init__(f"timeline.{switch_id}.no-op")
        self._forbidden_events.append("combo.activated")
        self._commit_funcs.append(NoOpAction.Load(switch_id))

    def activate(self, now: float) -> None:
        pass
