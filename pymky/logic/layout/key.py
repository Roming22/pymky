from logic.actions.key import Key as KeyAction
from logic.quantum.timeline_keycode import TimelineKeycode


class Key:

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> list:
        # TODO: Add parsing of complex definitions
        timelines = [TimelineKeycode(switch_id, key_definition)]
        return timelines
