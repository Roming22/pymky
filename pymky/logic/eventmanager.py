from collections import deque

from logic.context import Context


class EventManager:
    __blocker = None
    __buffer = deque([], 32)
    __event_index = -1

    @classmethod
    def AddEvent(cls, event):
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
            event = cls.__buffer.popleft()
            if event.pressed:
                print("# Pressed")
                Context.count += 1
            else:
                print("# Released")
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
