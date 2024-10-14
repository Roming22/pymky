from hardware.usbkey import UsbKey


class Key:

    @classmethod
    def Load(cls, key_definition: str) -> UsbKey:
        return UsbKey(key_definition)
