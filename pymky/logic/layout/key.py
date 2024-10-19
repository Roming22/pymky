from logic.actions.key import Key as KeyAction
from logic.quantum.timeline_key import TimelineKey


class Key:

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> list:
        # TODO: Add parsing of complex definitions
        action = KeyAction.Load(switch_id, key_definition)
        timelines = [TimelineKey(action)]
        return timelines
