try:
    import usb_hid
    from adafruit_hid.keyboard import Keyboard as USB_Keyboard
    from adafruit_hid.keycode import Keycode

    _kbd = USB_Keyboard(usb_hid.devices)
except ModuleNotFoundError as ex:
    # Test mode
    import sys

    if "pytest" not in sys.modules:
        raise ex
    _kbd = None
    Keycode = None

from utils.noop import no_op


class UsbKey:
    _keys = {}
    _KC = {
        "DOLLAR": ["LEFT_SHIFT", "FOUR"],
        "DOT": "PERIOD",
        "EQUAL": "EQUALS",
        "ESC": "ESCAPE",
        "EXCLAIM": ["LEFT_SHIFT", "ONE"],
        "GRAVE": "GRAVE_ACCENT",
        "HASH": ["LEFT_SHIFT", "THREE"],
        "LALT": "LEFT_ALT",
        "LCTL": "LEFT_CONTROL",
        "LGUI": "LEFT_GUI",
        "LSFT": "LEFT_SHIFT",
        "MEH": ["LEFT_ALT", "LEFT_CONTROL", "LEFT_SHIFT"],
        "NO": [],
        "RALT": "RIGHT_ALT",
        "RCTL": "RIGHT_CONTROL",
        "RGUI": "RIGHT_GUI",
        "RSFT": "RIGHT_SHIFT",
        "SLASH": "FORWARD_SLASH",
        "UNDERSCORE": ["LEFT_SHIFT", "MINUS"],
    }

    @classmethod
    def Load(cls, key_definition: str) -> "UsbKey":
        try:
            return cls._keys[key_definition]
        except KeyError:
            key = cls(key_definition)
            cls._keys[key_definition] = key
            return key

    @staticmethod
    def Panic() -> None:
        print("!!! PANIC !!!")
        _kbd.release_all()

    @classmethod
    def _get_keycodes_for(cls, keycode: str) -> list[Keycode]:
        if keycode in cls._KC.keys():
            keycodes = cls._KC[keycode]
            if not isinstance(keycodes, list):
                keycodes = [keycodes]
        else:
            keycodes = [keycode]
        return [getattr(Keycode, kc) for kc in keycodes]

    def __init__(self, key_definition: str) -> None:
        self.definition = key_definition
        self.press, self.release = self._get_actions(key_definition)

    @classmethod
    def _get_actions(cls, key_definition: str) -> tuple[callable, callable]:
        try:
            keycodes = cls._get_keycodes_for(key_definition)
        except AttributeError:
            print(f"[ERROR] Unknown Keycode in '{key_definition}' definition")
            return (no_op, no_op)

        # Press key(s)
        def press() -> None:
            print(f"Press {key_definition}")
            for kc in keycodes:
                _kbd.press(kc)

        # Release key(s)
        def release() -> None:
            print(f"Release {key_definition}")
            for kc in reversed(keycodes):
                _kbd.release(kc)

        return (press, release)
