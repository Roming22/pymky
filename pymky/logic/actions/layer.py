from hardware.led import Leds
from logic.actions.switch import Switch
from utils.noop import no_op


class Layer:
    _event_callbacks = {}
    _layers = {}
    _active_layers = []
    _switch_to_timeline = []
    _activated_switches = []

    @classmethod
    def RegisterLayer(cls, layer_name: str, layer: object) -> None:
        cls._layers[layer_name] = layer
        if layer.default:
            cls._switch_to_timeline = [[] for _ in layer.switch_to_timelines]
            cls._Change(layer)

    @classmethod
    def _Activate(cls) -> None:
        layer = cls._active_layers[-1]
        print(f"Layer: Activating {layer.uid}")
        for led_id in range(Leds.count):
            Leds.Set(led_id, layer.color)
        for switch_id in layer.switch_to_timelines.keys():
            for _layer in reversed(cls._active_layers):
                timelines = _layer.switch_to_timelines[switch_id]
                if timelines:
                    cls._switch_to_timeline[switch_id] = timelines
                    break

    @classmethod
    def _Change(cls, layer: object) -> None:
        cls._active_layers.append(layer)
        cls._Activate()
        # Once the layer has been activated and transparent
        # keys have been processed, the layer history can
        # be collapsed.
        cls._active_layers = [layer]

    @classmethod
    def _GetLayer(cls, layer_name: str) -> object:
        layer = cls._layers[layer_name].copy()
        return layer

    @classmethod
    def _Add(cls, layer: object) -> None:
        cls._active_layers.append(layer)
        cls._Activate()

    @classmethod
    def _Remove(cls, layer: object) -> None:
        try:
            cls._active_layers.remove(layer)
            cls._Activate()
        except ValueError:
            # A momentary layer may have disappear
            # if a layer change occured.
            pass

    @classmethod
    def LoadChange(cls, switch_id: str, layer_name: str) -> callable:
        print(f"Layers: {list(cls._layers.keys())}")

        def action() -> None:
            layer = cls._GetLayer(layer_name)
            Switch._press_actions[switch_id] = lambda: cls._Change(layer)
            Switch._release_actions[switch_id] = no_op

        return action

    @classmethod
    def LoadMomentary(cls, switch_id: str, layer_name: str) -> callable:
        print(f"Layers: {list(cls._layers.keys())}")

        def action() -> None:
            layer = cls._GetLayer(layer_name)
            Switch._press_actions[switch_id] = lambda: cls._Add(layer)
            Switch._release_actions[switch_id] = lambda: cls._Remove(layer)

        return action

    @classmethod
    def ActivateSwitch(cls, switch_id: int) -> None:
        print(f"Layer activate switch: {switch_id}")
        cls._activated_switches.append(switch_id)

    @classmethod
    def Process(cls, switch_id: int) -> list:
        print(f"Activated switches: {cls._activated_switches}")
        try:
            cls._activated_switches.remove(switch_id)
            print("Switch activated")
            return []
        except ValueError:
            pass

        # Return copy of the timeline list, so it can be
        # manipulated without impacting the reference.
        return cls._switch_to_timeline[switch_id].copy()
