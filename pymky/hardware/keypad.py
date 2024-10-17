import digitalio
from config.board import board
from logic.actions.switch import Switch as SwitchAction
from logic.events.switch import Switch as SwitchEvent


class Keypad:
    count = 0
    __cols = []
    __rows = []

    @classmethod
    def Init(cls) -> None:
        def init_col(pin: int) -> None:
            io = digitalio.DigitalInOut(pin)
            io.direction = digitalio.Direction.INPUT
            io.pull = digitalio.Pull.UP
            return io

        def init_row(pin: int) -> None:
            io = digitalio.DigitalInOut(pin)
            io.direction = digitalio.Direction.OUTPUT
            io.drive_mode = digitalio.DriveMode.PUSH_PULL
            io.value = 0
            return io

        cls.__cols = [init_col(pin) for pin in board["pins"]["cols"]]
        cls.__rows = [init_row(pin) for pin in board["pins"]["rows"]]
        cls.count = len(cls.__cols) * len(cls.__rows)

        SwitchAction.Init(cls.count)
        SwitchEvent.Init(cls.count, cls.Matrix_Scan)

    @classmethod
    def Matrix_Scan(cls) -> Generator[tuple[int, bool]]:
        index = -1
        for row in cls.__rows:
            row.value = 0
            for col in cls.__cols:
                index += 1
                yield index, not col.value
            row.value = 1
