from time import sleep

from hardware.board import board
from hardware.led import Leds
from logic.blink import blink


def init() -> None:
    print("\n" * 5)
    print("#" * 120)
    print("# BOOTING")
    print("#" * 120)

    Leds.Init()


def main() -> None:
    init()
    while True:
        blink()


if __name__ == "__main__":
    main()
