from logic.actions.layer import Layer
from logic.actions.switch import Switch
from logic.events.event import Event
from logic.events.timer import Timer


class TimelineManager:
    _timelines = []
    _buffered_events = []

    @classmethod
    def IsResolved(cls) -> bool:
        return not cls._timelines

    @classmethod
    def Process(cls, event: Event) -> None:
        print(f"Timeline: received event {event.id} @{event.time}")
        cls.ToLayer(event)
        cls.ToTimelines(event)
        if event.type == "switch":
            cls._buffered_events.append(event)
        if cls._buffered_events:
            cls.Resolve()

    @classmethod
    def Resolve(cls) -> None:
        if not cls.IsResolved():
            print(f"Timeline: Unresolved; event count: {len(cls._buffered_events)}")
            return
        print(f"Timeline: Resolved; event count: {len(cls._buffered_events)}")

        cls.ToSwitch(cls._buffered_events.pop(0))
        print(f"Timeline: After event count: {len(cls._buffered_events)}")

        replay_events = list(cls._buffered_events)
        cls._buffered_events.clear()
        for index, event in enumerate(replay_events):
            print(
                f"Timeline: Replaying event {index+1}/{len(replay_events)}: {event.id}"
            )
            cls.Process(event)

    @classmethod
    def ToLayer(cls, event: Event) -> None:
        if not cls.IsResolved():
            # New timelines can be created only on a switch pressed event
            return

        if event.type != "switch":
            return

        switch_id, state = event.data
        if state:
            cls._timelines = Layer.Process(switch_id)
            for timeline in cls._timelines:
                timeline.activate(event.time)

    @classmethod
    def ToSwitch(cls, event: Event) -> None:
        print(f"Timeline: Send {event.id} to Switch")
        Switch.Process(event)

    @classmethod
    def ToTimelines(cls, event: Event) -> None:
        for index, timeline in enumerate(reversed(cls._timelines)):
            if not timeline.process(event.id):
                cls._timelines.pop(-1 - index)
                print(f"Timeline: {timeline.id} deleted")

        if len(cls._timelines) == 1:
            timeline = cls._timelines.pop()
            print(
                f"Timeline: Resolving to {timeline.id}; event count: {len(cls._buffered_events)}"
            )
            timeline.commit()
            Timer.Clear()
