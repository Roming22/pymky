from logic.actions.layer import Layer as LayerAction
from logic.quantum.timeline import Timeline


class TimelineLayer(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        timelines = [cls(switch_id, key_definition[0])]
        return timelines

    def __init__(self, switch_id: int, key_definition: str) -> None:
        self.id = f"timeline.{switch_id}.layer-change.{key_definition}"
        self._forbidden_events = []
        self.commit = LayerAction.Load(switch_id, key_definition)

    def activate(self, now: float) -> None:
        pass
