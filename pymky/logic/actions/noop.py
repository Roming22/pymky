from logic.actions.switch import Switch
from utils.noop import no_op


class NoOp:
    @classmethod
    def Load(cls, switch_id: int) -> callable:
        def action() -> None:
            Switch._press_actions[switch_id] = no_op
            Switch._release_actions[switch_id] = no_op

        return action
