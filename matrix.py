class QRMatrix:
    """
    Represents a Version 1 QR Code matrix.

    Version 1 = 21 x 21 modules.
    """

    SIZE = 21

    def __init__(self):
        self.matrix = [
            [None for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def set(self, row, col, value):
        self.matrix[row][col] = value

    def get(self, row, col):
        return self.matrix[row][col]