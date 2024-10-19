class Event:
    def __init__(self, time: float, type: str, data: tuple) -> None:
        self.time = time
        self.type = type
        self.data = data
        self.id = f"{type}.{".".join([str(d) for d in data])}"
