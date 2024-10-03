from time import sleep

from hardware.board import board
from hardware.keypad import Keypad
from hardware.led import Leds
from logic.scan import scan


def init() -> None:
    print("\n" * 5)
    print("#" * 120)
    print("# BOOTING")
    print("#" * 120)

    Leds.Init()
    Keypad.Init()


def main() -> None:
    init()
    while True:
        scan()


if __name__ == "__main__":
    main()
