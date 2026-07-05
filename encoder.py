class QREncoder:
    """
    Encodes text into the QR Code bit stream.
    Currently supports Version 1 Byte Mode.
    """

    MODE_INDICATOR = "0100"

    def encode(self, text):
        bits = ""

        # Mode Indicator
        bits += self.MODE_INDICATOR

        # Character Count (8 bits)
        bits += format(len(text), "08b")

        # ASCII bytes
        for char in text:
            bits += format(ord(char), "08b")

        return bits