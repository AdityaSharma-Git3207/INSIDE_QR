from matrix import QRMatrix


class QRCodeBuilder:
    """
    Coordinates the entire QR Code generation pipeline.
    """

    def __init__(self):
        self.matrix = QRMatrix()

    def build_function_patterns(self):
        """
        Build all fixed QR structures.
        """

        self.matrix.add_finder_patterns()
        self.matrix.add_separator()
        self.matrix.add_timing_patterns()
        self.matrix.add_dark_module()
        self.matrix.reserve_format_information()

    def get_matrix(self):
        return self.matrix.matrix