from hardware.led import Leds
from logic.actions.switch import Switch
from logic.layout.layer import Layer as LayerDefinition


class Layer:
    _event_callbacks = {}
    _layers = []

    @classmethod
    def Init(cls) -> None:
        LayerDefinition.Init()
        cls.Activate(LayerDefinition.default)

    @classmethod
    def Activate(cls, layer: LayerDefinition) -> None:
        print("Activating:", layer.uid)
        cls._layers.append(layer)
        for led_id in range(Leds.count):
            Leds.Set(led_id, layer.color)
        for switch_id, action in layer.switch_to_action.items():
            if action:
                Switch.SetAction(switch_id, action)
