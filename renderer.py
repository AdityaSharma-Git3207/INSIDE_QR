from PIL import Image
from constants import Module


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)


class QRRenderer:
    """
    Renders a QR matrix as a PNG image.
    """

    CELL_SIZE = 20

    def render(self, matrix, filename):
        size = len(matrix)

        image = Image.new(
            "RGB",
            (
                size * self.CELL_SIZE,
                size * self.CELL_SIZE,
            ),
            WHITE,
        )

        pixels = image.load()

        for row in range(size):
            for col in range(size):

                value = matrix[row][col]

                if value == Module.BLACK:
                    color = BLACK

                elif value == Module.RESERVED:
                    color = GRAY

                else:
                    continue

                for y in range(self.CELL_SIZE):
                    for x in range(self.CELL_SIZE):
                        pixels[
                            col * self.CELL_SIZE + x,
                            row * self.CELL_SIZE + y,
                        ] = color

        image.save(filename)