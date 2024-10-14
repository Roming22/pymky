from config.layout import layout as layout_definition
from hardware.led import Leds


class Layer:
    """Holds the layer definition"""

    __layers = {}
    __active = None

    @classmethod
    def Init(cls):
        for layer_name, layer_definition in layout_definition.items():
            cls.__layers[layer_name] = Layer(layer_name, layer_definition)

    @classmethod
    def Process(cls, event_data) -> list:
        return cls.__active.process(event_data)

    # @memory_cost("Layer")
    def __init__(self, layer_name: str, layer_definition: dict) -> None:
        print("Loading layer:", layer_name)
        self.uid = f"layer.{layer_name}"
        self.__switch_to_keycode = {}
        for switch_id, keycode in enumerate(layer_definition["keys"]):
            switch_id += 1
            print(f"Switch {switch_id}: {keycode}")
            self.__switch_to_keycode[switch_id] = [keycode]
            # self.switch_to_keycode[switch_id] = Key.Load(keycode)

        # Load layer color
        self.__color = layer_definition.get("color")

        # Load combos
        # try:
        #     self.combos = Combo.Load(layer_definition["combos"])
        # except KeyError:
        #     print("No combo has been declared")
        #     self.combos = []

        if self.__active is None or layer_definition.get("default", False):
            self.activate()

    def activate(self) -> None:
        print("Activating:", self.uid)
        Layer.__active = self
        for led_id in range(Leds.count):
            Leds.Set(led_id, self.__color)

    def process(self, switch_id) -> list:
        print(f"Layer {self.uid}: {switch_id} = {self.__switch_to_keycode[switch_id]}")
        return []
