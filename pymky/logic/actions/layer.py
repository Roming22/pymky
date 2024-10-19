from hardware.led import Leds
from logic.layout.layer import Layer as LayerDefinition


class Layer:
    _event_callbacks = {}
    _layers = []
    _switch_to_timeline = []

    @classmethod
    def Init(cls) -> None:
        LayerDefinition.Init()
        if not cls._switch_to_timeline:
            cls._switch_to_timeline = [
                None for _ in LayerDefinition.default.switch_to_timelines
            ]
        cls.Activate(LayerDefinition.default)

    @classmethod
    def Activate(cls, layer: LayerDefinition) -> None:
        print("Activating:", layer.uid)
        cls._layers.append(layer)
        for led_id in range(Leds.count):
            Leds.Set(led_id, layer.color)
        for switch_id, timeline in layer.switch_to_timelines.items():
            if timeline:
                cls._switch_to_timeline[switch_id] = timeline

    @classmethod
    def Process(cls, switch_id: int) -> list:
        return cls._switch_to_timeline[switch_id]
