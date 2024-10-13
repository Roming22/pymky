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


def get_keycodes_for(keycode: str) -> list[Keycode]:
    if keycode in _KC.keys():
        keycodes = _KC[keycode]
        if not isinstance(keycodes, list):
            keycodes = [keycodes]
    else:
        keycodes = [keycode]
    return keycodes


def panic() -> None:
    print("!!! PANIC !!!")
    _kbd.release_all()


def get_actions(key_name: str) -> tuple[callable, callable]:
    keycodes = get_keycodes_for(key_name)

    # Validate keycodes
    def no_op() -> None:
        pass

    for kc in keycodes:
        try:
            getattr(Keycode, kc)
        except AttributeError:
            print(f"[ERROR] Unknown Keycode: {kc} in {key_name} definition")
            return (no_op, no_op)

    # Press key(s)
    def press() -> None:
        print(f"Press {key_name}")
        for kc in keycodes:
            _kbd.press(getattr(Keycode, kc))

    # Release key(s)
    def release() -> None:
        print(f"Release {key_name}")
        for kc in keycodes:
            _kbd.release(getattr(Keycode, kc))

    return (press, release)
