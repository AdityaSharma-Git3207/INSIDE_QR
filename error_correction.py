from reedsolo import RSCodec


class QRErrorCorrection:
    """
    Generates Reed-Solomon error correction codewords
    for Version 1-L.
    """

    ECC_BYTES = 7

    def generate(self, data_codewords):

        rs = RSCodec(self.ECC_BYTES)

        encoded = rs.encode(bytes(data_codewords))

        return list(encoded[-self.ECC_BYTES:])