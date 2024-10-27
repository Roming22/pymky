from hardware.usbkey import UsbKey
from logic.actions.switch import Switch


class Key:

    @classmethod
    def Load(cls, switch_id: int, key_definition: str) -> callable:
        key = UsbKey.Load(key_definition)

        def action() -> None:
            Switch._press_actions[switch_id] = key.press
            Switch._release_actions[switch_id] = key.release

        return action
