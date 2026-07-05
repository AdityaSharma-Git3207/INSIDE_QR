from patterns import FINDER_PATTERN
from constants import Module


class QRMatrix:
    """
    Represents a Version 1 QR Code matrix.

    Version 1 QR Codes are always 21 × 21 modules.
    """

    SIZE = 21

    def __init__(self):
        self.matrix = [
            [Module.EMPTY for _ in range(self.SIZE)]
            for _ in range(self.SIZE)
        ]

    def set(self, row, col, value):
        """
        Set a module value if it's inside the matrix.
        """
        if 0 <= row < self.SIZE and 0 <= col < self.SIZE:
            self.matrix[row][col] = value

    def get(self, row, col):
        """
        Get the value of a module.
        """
        return self.matrix[row][col]

    def draw_pattern(self, pattern, start_row, start_col):
        """
        Draw any reusable QR pattern into the matrix.
        """
        rows = len(pattern)
        cols = len(pattern[0])

        for r in range(rows):
            for c in range(cols):
                self.set(
                    start_row + r,
                    start_col + c,
                    pattern[r][c],
                )

    def add_finder_pattern(self, start_row, start_col):
        """
        Draw a single finder pattern.
        """
        self.draw_pattern(
            FINDER_PATTERN,
            start_row,
            start_col,
        )

    def add_finder_patterns(self):
        """
        Draw all three finder patterns.
        """
        self.add_finder_pattern(0, 0)
        self.add_finder_pattern(0, 14)
        self.add_finder_pattern(14, 0)

    def add_separator(self):
        """
        Draw the mandatory white separator around
        each finder pattern.
        """

        positions = [
            (0, 0),
            (0, 14),
            (14, 0),
        ]

        for start_row, start_col in positions:

            # Top & Bottom
            for c in range(-1, 8):
                self.set(
                    start_row - 1,
                    start_col + c,
                    Module.WHITE,
                )
                self.set(
                    start_row + 7,
                    start_col + c,
                    Module.WHITE,
                )

            # Left & Right
            for r in range(-1, 8):
                self.set(
                    start_row + r,
                    start_col - 1,
                    Module.WHITE,
                )
                self.set(
                    start_row + r,
                    start_col + 7,
                    Module.WHITE,
                )

    def add_timing_patterns(self):
        """
        Draw the horizontal and vertical timing patterns.
        """

        for i in range(8, 13):

            value = (
                Module.BLACK
                if i % 2 == 0
                else Module.WHITE
            )

            self.set(6, i, value)
            self.set(i, 6, value)
    
    def add_dark_module(self):
        """
        Add the fixed dark module required by
        the QR code specification.
        """

        self.set(
            13,
            8,
            Module.BLACK
        )
    
    def reserve_format_information(self):
        """
        Reserve the modules used for format information.
        """

        # Around top-left finder

        for col in range(9):
            if col != 6:
                if self.get(8, col) == Module.EMPTY:
                    self.set(8, col, Module.RESERVED)

        for row in range(9):
            if row != 6:
                if self.get(row, 8) == Module.EMPTY:
                    self.set(row, 8, Module.RESERVED)

        # Top-right

        for col in range(13, 21):
            self.set(
                8,
                col,
                Module.RESERVED,
            )

        # Bottom-left

        for row in range(13, 21):
            self.set(
                row,
                8,
                Module.RESERVED,
            )