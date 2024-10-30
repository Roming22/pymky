from logic.events.event import Event
from utils.noop import no_op


class Switch:
    _press_actions = []
    _release_actions = []

    @classmethod
    def Init(cls, switch_count: int) -> None:
        cls._press_actions = [no_op for _ in range(switch_count)]
        cls._release_actions = [no_op for _ in range(switch_count)]

    @classmethod
    def SetAction(cls, switch_id: int, action: callable) -> None:
        # print(f"Setting press action for {switch_id}")
        cls._press_actions[switch_id] = action

    @classmethod
    def Process(cls, event: Event) -> None:
        switch_id, state = event.data
        print(f"Switch {switch_id} state: {state}")
        if state:
            actions = cls._press_actions
        else:
            actions = cls._release_actions
        actions[switch_id]()
