from logic.keyboard import Keyboard


def boot() -> None:
    print("\n" * 5)
    print("#" * 120)
    print("# BOOTING")
    print("#" * 120)
    Keyboard.Init()


def main() -> None:
    boot()

    print()
    print("#" * 120)
    print("# LOOP")
    print("#" * 120)
    while True:
        Keyboard.Tick()


if __name__ == "__main__":
    main()
