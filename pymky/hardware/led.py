from hardware.board import board
from neopixel import NeoPixel


class Leds:
    count = 0
    __pixels = None
    __refresh = True

    @classmethod
    def Init(cls):
        cls.count = board["leds"]["count"]
        cls.__pixels = NeoPixel(board["leds"]["pin"], cls.count)
        cls.__refresh = True
        for i in range(cls.count):
            cls.Set(i, (0, 0, 0))
        cls.Write()

    @classmethod
    def Set(cls, pixel_id, rgb):
        cls.__pixels[pixel_id] = rgb
        cls.__refresh = True

    @classmethod
    def Write(cls):
        if cls.__refresh:
            cls.__pixels.write()
            cls.__refresh = False
