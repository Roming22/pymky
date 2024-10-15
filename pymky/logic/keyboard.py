from hardware.led import Leds
from logic.eventmanager import EventManager
from logic.events import scan
from logic.events.switch import Switch
from logic.layout.layer import Layer


class Keyboard:
    @staticmethod
    def Init() -> None:
        Switch.Init()
        Leds.Init()
        Layer.Init()

    @staticmethod
    def Tick() -> None:
        scan()
        EventManager.Process()
