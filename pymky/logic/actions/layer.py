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
        for switch_id, timelines in layer.switch_to_timelines.items():
            if timelines:
                cls._switch_to_timeline[switch_id] = timelines

    @classmethod
    def Process(cls, switch_id: int) -> list:
        # Return copy of the timeline list, so it can be
        # manipulated without impacting the reference.
        return list(cls._switch_to_timeline[switch_id])
