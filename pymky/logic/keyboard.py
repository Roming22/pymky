from hardware.keypad import Keypad
from hardware.led import Leds
from hardware.usbkey import UsbKey
from logic.eventmanager import EventManager
from logic.events.scanner import scan
from logic.layout.layer import Layer


class Keyboard:
    @staticmethod
    def Init() -> None:
        UsbKey.Panic()
        Keypad.Init()
        Leds.Init()
        Layer.Init()

    @staticmethod
    def Tick() -> None:
        scan()
        EventManager.Process()
