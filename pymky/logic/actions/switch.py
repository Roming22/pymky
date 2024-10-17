class Switch:
    _press_actions = []
    _release_actions = []

    @classmethod
    def Init(cls, switch_count: int) -> None:
        cls._press_actions = [None for _ in range(switch_count)]
        cls._release_actions = [None for _ in range(switch_count)]

    @classmethod
    def SetAction(cls, switch_id: int, action: callable) -> None:
        # print(f"Setting press action for {switch_id}")
        cls._press_actions[switch_id] = action

    @classmethod
    def Process(cls, event: tuple) -> None:
        switch_id, state = event
        print(f"Switch {switch_id} state: {state}")
        if state:
            actions = cls._press_actions
        else:
            actions = cls._release_actions
        actions[switch_id]()
