from logic.actions.layer import Layer as LayerAction
from logic.layout.combo import Combo
from logic.layout.key import Key

from config.layout import layout as layout_definition


class Layer:
    """Holds the layer definition"""

    @classmethod
    def Init(_) -> None:
        layers = {}
        for layer_name, layer_definition in layout_definition.items():
            layer = Layer()
            layer._load(layer_name, layer_definition)
            layers[layer_name] = layer

    def __init__(self) -> None:
        self.name = ""
        self.uid = ""
        self.color = (0, 0, 0)
        self.switch_to_timelines = {}

    # @memory_cost("Layer")
    def _load(self, layer_name: str, layer_definition: dict) -> None:
        print("Loading layer:", layer_name)
        self.name = layer_name
        self.uid = f"layer.{layer_name}"
        self.default = layer_definition.get("default", False)

        # Load layer color
        self.color = layer_definition.get("color")

        # Load switches
        self.switch_to_timelines = {}
        for switch_id, keycode in enumerate(layer_definition["keys"]):
            print(f"Switch {switch_id}: {keycode}")
            self.switch_to_timelines[switch_id] = Key.Load(switch_id, keycode)

        # Load combos
        for switch_ids, keycode in layer_definition["combos"].items():
            timelines = Combo.Load(switch_ids, keycode)
            for switch_id in switch_ids:
                self.switch_to_timelines[switch_id].extend(timelines)

        LayerAction.RegisterLayer(layer_name, self)

    # @memory_cost("Layer")
    def copy(self):
        instance = Layer()
        instance.name = self.name
        instance.uid = self.uid
        instance.color = self.color
        instance.switch_to_timelines = self.switch_to_timelines
        return instance
