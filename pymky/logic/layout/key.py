import re

from logic.quantum.timeline_keycode import TimelineKeycode
from logic.quantum.timeline_layer import TimelineLayerChange, TimelineLayerMomentary
from logic.quantum.timeline_noop import TimelineNoOp
from logic.quantum.timeline_taphold import TimelineTapHold


class Key:
    _loader_map = {
        "KC": TimelineKeycode.Load,
        "LC": TimelineLayerChange.Load,
        "LM": TimelineLayerMomentary.Load,
        "NO": TimelineNoOp.Load,
        "TH": TimelineTapHold.Load,
    }

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> list:
        # print(f"Loading timelines for Keycode {key_definition}")
        if key_definition == "____":
            return []
        elif key_definition is None:
            key_definition = "NO"
        loader, definition = cls.Parse(key_definition)
        timelines = loader(switch_id, definition)
        return timelines

    @classmethod
    def Parse(cls, key_definition: str) -> tuple(callable, tuple):
        m = re.match(r"([A-Z]*)\((.*)\)", key_definition)
        if m:
            func, data = m.groups()
            data = data.split(",")
        elif key_definition == "NO":
            func = "NO"
            data = []
        else:
            func = "KC"
            data = [
                key_definition,
            ]
        data = [d.strip(" ") for d in data]
        # print(f"Definition: {func}{data}")
        loader = cls._loader_map[func]
        return (loader, data)
