from logic.actions.noop import NoOp as NoOpAction
from logic.quantum.timeline import Timeline


class TimelineNoOp(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        timelines = [cls(switch_id)]
        return timelines

    def __init__(self, switch_id: int) -> None:
        self.id = f"timeline.{switch_id}.no-op"
        self._forbidden_events = []
        self.commit = NoOpAction.Load(switch_id)

    def activate(self, now: float) -> None:
        pass
