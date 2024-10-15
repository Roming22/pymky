from collections import deque

from logic.layout.layer import Layer


class EventManager:
    __buffer = deque([], 32)
    __options = []
    __now = 0

    @classmethod
    def AddEvent(cls, event: tuple) -> None:
        options = []
        for option in cls.__options:
            if option.process(event):
                options.append(option)
        cls.__options = options
        cls.__buffer.append(event)

    @classmethod
    def Process(cls) -> None:
        while len(cls.__options) <= 1 and cls.__buffer:
            cls.__now, event_data = cls.__buffer.popleft()
            print(f"# [{cls.__now}] Event: {".".join([str(d) for d in event_data])}")
            if event_data[0] == "switch":
                cls.__options = Layer.Process(event_data[1], event_data[2])
            if len(cls.__options) > 1:
                options = []
                for option in cls.__options:
                    for event in cls.__buffer:
                        if option.process(event):
                            options.append(option)
                cls.__options = options
