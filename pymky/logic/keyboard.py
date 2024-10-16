from hardware.led import Leds
from hardware.usbkey import UsbKey
from logic.actions.layer import Layer
from logic.eventmanager import EventManager
from logic.events import scan
from logic.events.switch import Switch


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
