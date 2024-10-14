from hardware.led import Leds
from logic.eventmanager import EventManager
from logic.events import scan
from logic.events.switch import Switch
from logic.layout.layer import Layer


class Keyboard:
    @classmethod
    def Init(_) -> None:
        Switch.Init()
        Leds.Init()
        Layer.Init()

    @classmethod
    def Tick(_) -> None:
        scan()
        EventManager.Process()
