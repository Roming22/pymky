import board as mcu

board = {
    "pins": {
        "cols": (
            mcu.D27,
            mcu.D26,
            mcu.D22,
            mcu.D20,
            mcu.D23,
            mcu.D21,
        ),
        "rows": (mcu.D5, mcu.D6, mcu.D7, mcu.D9),
    },
    "leds": {
        "pin": mcu.D0,
        "count": 4,
    },
}
