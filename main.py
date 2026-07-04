from matrix import QRMatrix
from renderer import QRRenderer

matrix = QRMatrix()

renderer = QRRenderer()

renderer.render(
    matrix.matrix,
    "output/step1_blank_matrix.png",
)
print("Done!")