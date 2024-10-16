from hardware.led import Leds
from hardware.usbkey import UsbKey
from logic.eventmanager import EventManager
from logic.events import scan
from logic.events.switch import Switch
from logic.layout.layer import Layer


class Keyboard:
    @staticmethod
    def Init() -> None:
        UsbKey.Panic()
        Switch.Init()
        Leds.Init()
        Layer.Init()

    @staticmethod
    def Tick() -> None:
        scan()
        EventManager.Process()
