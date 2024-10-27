import re

from logic.quantum.timeline_keycode import TimelineKeycode
from logic.quantum.timeline_taphold import TimelineTapHold


class Key:
    _loader_map = {
        "KC": TimelineKeycode.Load,
        "TH": TimelineTapHold.Load,
    }

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> list:
        print(f"Loading timelines for Keycode {key_definition}")
        timelines = []
        if key_definition in ["NO", None]:
            return timelines
        loader, definition = cls.Parse(key_definition)
        timelines = loader(switch_id, definition)
        for timeline in timelines:
            print(f"{type(timeline)}")
        return timelines

    @classmethod
    def Parse(cls, key_definition: str) -> tuple(callable, tuple):
        m = re.match(r"([A-Z]*)\((.*)\)", key_definition)
        if m:
            func, data = m.groups()
            data = data.split(",")
        else:
            func = "KC"
            data = [
                key_definition,
            ]
        data = [d.strip(" ") for d in data]
        print(f"Definition: {func}{data}")
        loader = cls._loader_map[func]
        return (loader, data)
