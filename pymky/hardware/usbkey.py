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
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
        "-": "KEYPAD_MINUS",
        "/": "KEYPAD_FORWARD_SLASH",
        "=": "KEYPAD_EQUALS",
        ".": "KEYPAD_PERIOD",
    }
    _state = {}

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
        keycodes = [getattr(Keycode, kc) for kc in keycodes]
        for kc in keycodes:
            UsbKey._state[kc] = 0
        return keycodes

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
            for kc in keycodes:
                if not UsbKey._state[kc]:
                    print(f"Press {key_definition}")
                    _kbd.press(kc)
                UsbKey._state[kc] += 1

        # Release key(s)
        def release() -> None:
            for kc in reversed(keycodes):
                UsbKey._state[kc] -= 1
                if not UsbKey._state[kc]:
                    print(f"Release {key_definition}")
                    _kbd.release(kc)

        return (press, release)
