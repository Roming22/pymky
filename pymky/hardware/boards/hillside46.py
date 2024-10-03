import board as mcu

board = {
    "pins": {
        "cols": (
            mcu.D26,
            mcu.D22,
            mcu.D20,
            mcu.D23,
        ),
        "rows": (mcu.D6, mcu.D7, mcu.D9),
    },
    "leds": {
        "pin": mcu.D0,
        "count": 4,
    },
}
