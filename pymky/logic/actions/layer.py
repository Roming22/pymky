from hardware.led import Leds
from logic.actions.switch import Switch
from utils.noop import no_op


class Layer:
    _event_callbacks = {}
    _layers = {}
    _active_layers = {}
    _switch_to_timeline = []

    @classmethod
    def RegisterLayer(cls, layer_name, layer) -> None:
        cls._layers[layer_name] = layer
        if layer.default:
            cls._switch_to_timeline = [[] for _ in layer.switch_to_timelines]
            cls.Change(layer_name)

    @classmethod
    def Change(cls, layer_name: str) -> None:
        layer = cls._layers[layer_name]
        print(f"Layer: Activating {layer.uid}")
        cls._active_layers = [layer]
        for led_id in range(Leds.count):
            Leds.Set(led_id, layer.color)
        for switch_id, timelines in layer.switch_to_timelines.items():
            if timelines:
                cls._switch_to_timeline[switch_id] = timelines

    @classmethod
    def Load(cls, switch_id: str, layer_name: str) -> callable:
        print(f"Layers: {list(cls._layers.keys())}")

        def action() -> None:
            Switch._press_actions[switch_id] = lambda: cls.Change(layer_name)
            Switch._release_actions[switch_id] = no_op

        return action

    @classmethod
    def Process(cls, switch_id: int) -> list:
        # Return copy of the timeline list, so it can be
        # manipulated without impacting the reference.
        return list(cls._switch_to_timeline[switch_id])
