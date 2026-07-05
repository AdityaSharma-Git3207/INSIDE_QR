from matrix import QRMatrix
from encoder import QREncoder


class QRCodeBuilder:
    """
    Coordinates the entire QR Code generation pipeline.
    """

    def __init__(self):
        self.matrix = QRMatrix()
        self.encoder = QREncoder()

    def build_function_patterns(self):
        """
        Build all fixed QR structures.
        """

        self.matrix.add_finder_patterns()
        self.matrix.add_separator()
        self.matrix.add_timing_patterns()
        self.matrix.add_dark_module()
        self.matrix.reserve_format_information()
    
    def encode_data(self, text):
        return self.encoder.encode(text)

    def get_matrix(self):
        return self.matrix.matrix