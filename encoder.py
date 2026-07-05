class QREncoder:
    """
    QR Version 1-L Byte Mode Encoder
    """

    MODE_INDICATOR = "0100"
    MAX_BITS = 152

    PAD_BYTES = [
        "11101100",
        "00010001",
    ]

    def encode(self, text):

        bits = ""

        # Mode
        bits += self.MODE_INDICATOR

        # Character Count
        bits += format(len(text), "08b")

        # Data
        for char in text:
            bits += format(ord(char), "08b")

        # Terminator
        bits += "0000"

        # Byte Alignment
        while len(bits) % 8 != 0:
            bits += "0"

        # Alternate Pad Bytes
        pad_index = 0

        while len(bits) < self.MAX_BITS:

            bits += self.PAD_BYTES[pad_index]

            pad_index ^= 1

        return bits[:self.MAX_BITS]