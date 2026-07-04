from matrix import QRMatrix
from renderer import QRRenderer

matrix = QRMatrix()

matrix.add_finder_patterns()

renderer = QRRenderer()

renderer.render(
    matrix.matrix,
    "output/step2_finder_patterns.png",
)

print("Finder patterns created!")