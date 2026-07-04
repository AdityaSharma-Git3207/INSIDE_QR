from PIL import Image
from constants import Module


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


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

                if matrix[row][col] == Module.BLACK:

                    for y in range(self.CELL_SIZE):
                        for x in range(self.CELL_SIZE):

                            pixels[
                                col * self.CELL_SIZE + x,
                                row * self.CELL_SIZE + y,
                            ] = BLACK

        image.save(filename)