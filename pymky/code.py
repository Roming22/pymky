from logic import init, tick


def boot() -> None:
    print("\n" * 5)
    print("#" * 120)
    print("# BOOTING")
    print("#" * 120)
    init()


def main() -> None:
    boot()

    print()
    print("#" * 120)
    print("# LOOP")
    print("#" * 120)
    while True:
        tick()


if __name__ == "__main__":
    main()
