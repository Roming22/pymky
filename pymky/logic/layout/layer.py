from logic.layout.key import Key

from config.layout import layout as layout_definition
from logic.actions.layer import Layer as LayerAction

# from logic.layout.combo import Combo


class Layer:
    """Holds the layer definition"""

    @classmethod
    def Init(_) -> None:
        layers = {}
        for layer_name, layer_definition in layout_definition.items():
            layers[layer_name] = Layer(layer_name, layer_definition)

    # @memory_cost("Layer")
    def __init__(self, layer_name: str, layer_definition: dict) -> None:
        print("Loading layer:", layer_name)
        self.uid = f"layer.{layer_name}"
        self.default = layer_definition.get("default", False)
        self.switch_to_timelines = {}
        for switch_id, keycode in enumerate(layer_definition["keys"]):
            print(f"Switch {switch_id}: {keycode}")
            self.switch_to_timelines[switch_id] = Key.Load(switch_id, keycode)

        # Load layer color
        self.color = layer_definition.get("color")

        # Load combos
        # try:
        #     for switch_id, timelines in Combo.Load(layer_definition["combos"]):
        #        self.switch_to_timelines[switch_id] += timelines
        # except KeyError:
        #     print("No combo has been declared")

        LayerAction.RegisterLayer(layer_name, self)
