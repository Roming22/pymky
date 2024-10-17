from logic.actions.key import Key as KeyAction


class Key:

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> callable:
        # TODO: Add parsing of complex definitions
        action = KeyAction.Load(switch_id, key_definition)
        return action
