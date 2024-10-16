from hardware.led import Leds
from logic.layout.layer import Layer as LayerDefinition


class Layer:
    _event_callbacks = {}
    _layers = []

    @classmethod
    def Init(cls):
        LayerDefinition.Init()
        cls.Activate(LayerDefinition.default)

    @classmethod
    def Activate(cls, layer):
        print("Activating:", layer.uid)
        cls._layers.append(layer)
        for led_id in range(Leds.count):
            Leds.Set(led_id, layer.color)
