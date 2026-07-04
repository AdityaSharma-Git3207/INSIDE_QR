class QRMatrix:
    """
    Represents a Version 1 QR Code matrix.
    """

    SIZE = 21

    def __init__(self):
        self.matrix = [
            [None for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def set(self, row, col, value):
        if 0 <= row < self.SIZE and 0 <= col < self.SIZE:
            self.matrix[row][col] = value

    def get(self, row, col):
        return self.matrix[row][col]

    def add_finder_pattern(self, start_row, start_col):
        """
        Draws a standard 7×7 finder pattern.
        """

        pattern = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1],
        ]

        for r in range(7):
            for c in range(7):
                self.set(start_row + r, start_col + c, pattern[r][c])

    def add_finder_patterns(self):
        self.add_finder_pattern(0, 0)
        self.add_finder_pattern(0, 14)
        self.add_finder_pattern(14, 0)