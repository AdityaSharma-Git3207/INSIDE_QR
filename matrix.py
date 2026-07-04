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
    
    def add_separator(self):
        """
            Adds the mandatory white border around finder patterns.
        """

        positions = [
            (0, 0),
            (0, 14),
            (14, 0),
        ]

        for start_row, start_col in positions:

            # Top & Bottom
            for c in range(-1, 8):
                self.set(start_row - 1, start_col + c, 0)
                self.set(start_row + 7, start_col + c, 0)

            # Left & Right
            for r in range(7):
                self.set(start_row + r, start_col - 1, 0)
                self.set(start_row + r, start_col + 7, 0)

    def add_timing_patterns(self):
        """
            Draw alternating timing patterns.
        """

        for i in range(8, 13):

            value = 1 if i % 2 == 0 else 0

            self.set(6, i, value)
            self.set(i, 6, value)