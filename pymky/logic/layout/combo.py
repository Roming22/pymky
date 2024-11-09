from logic.quantum.timeline_combo import TimelineCombo


class Combo:
    @classmethod
    def Load(cls, switch_ids: list[int], key_definition: str) -> list:
        print(f"Loading timelines for Combo {key_definition}")
        timelines = TimelineCombo.Load(switch_ids, key_definition)
        return timelines
