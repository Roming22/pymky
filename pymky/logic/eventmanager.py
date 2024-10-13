from collections import deque

from logic.context import Context


class EventManager:
    __blocker = None
    __buffer = deque([], 32)
    __event_index = -1
    __now = 0

    @classmethod
    def AddEvent(cls, event) -> None:
        if cls.__blocker and cls.__blocker.Process(event):
            cls.__blocker = None
        cls.__buffer.append(event)

    @classmethod
    def Process(cls) -> None:
        # Test code
        if cls.__blocker:
            cls.__event_index
            return
        while cls.__buffer:
            cls.__now, event_data = cls.__buffer.popleft()
            event_type = event_data[0]
            print(f"# [{cls.__now}] Event: {".".join([str(d) for d in event_data])}")
            if event_type == "switch":
                if event_data[2]:
                    Context.count += 1
                else:
                    Context.count -= 1
        return

        # True code
        for event in cls.__blocker[cls.__event_index :]:
            if cls.__blocker and cls.__blocker.Process(event):
                cls.__blocker = None
                cls.__event_index = -1
            if cls.__blocker:
                break
            for cls.__event_index, event in enumerate(cls.__buffer):
                cls.__blocker = event.Process()
                if cls.__blocker:
                    break
