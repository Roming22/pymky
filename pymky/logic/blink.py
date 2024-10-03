from time import sleep

from hardware.led import Leds


def blink() -> None:
    for led_id in range(Leds.count):
        Leds.Set(led_id, (255, 0, 0))
        Leds.Write()
        print("# ON")
        sleep(0.125)
        Leds.Set(led_id, (0, 0, 0))
        Leds.Write()
        print("# OFF")
        sleep(0.125)
