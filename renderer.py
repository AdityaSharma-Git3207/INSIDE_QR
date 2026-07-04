from PIL import Image


class QRRenderer:
    CELL_SIZE = 20

    def render(self, matrix, filename):
        size = len(matrix)

        image = Image.new(
            "RGB",
            (
                size * self.CELL_SIZE,
                size * self.CELL_SIZE,
            ),
            "white",
        )

        pixels = image.load()

        for row in range(size):
            for col in range(size):

                value = matrix[row][col]

                if value:

                    for y in range(self.CELL_SIZE):
                        for x in range(self.CELL_SIZE):

                            pixels[
                                col * self.CELL_SIZE + x,
                                row * self.CELL_SIZE + y,
                            ] = (0, 0, 0)

        image.save(filename)