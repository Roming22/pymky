from logic.actions.layer import Layer as LayerAction
from logic.quantum.timeline import Timeline


class TimelineLayerChange(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        timelines = [cls(switch_id, key_definition[0])]
        return timelines

    def __init__(self, switch_id: int, key_definition: str) -> None:
        super().__init__(f"timeline.{switch_id}.layer-change.{key_definition}")
        self._commit_funcs.append(LayerAction.LoadChange(switch_id, key_definition))

    def activate(self, now: float) -> None:
        pass


class TimelineLayerMomentary(Timeline):
    @classmethod
    def Load(cls, switch_id: int, key_definition: tuple) -> list:
        timelines = [cls(switch_id, key_definition[0])]
        return timelines

    def __init__(self, switch_id: int, key_definition: str) -> None:
        super().__init__(f"timeline.{switch_id}.layer-momentary.{key_definition}")
        self._commit_funcs.append(LayerAction.LoadMomentary(switch_id, key_definition))

    def activate(self, now: float) -> None:
        pass
