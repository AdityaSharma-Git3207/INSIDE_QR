from matrix import QRMatrix
from renderer import QRRenderer

matrix = QRMatrix()

matrix.add_finder_patterns()
matrix.add_separator()
matrix.add_timing_patterns()

renderer = QRRenderer()

renderer.render(
    matrix.matrix,
    "output/step3_timing_patterns.png",
)

print("Timing patterns added!")