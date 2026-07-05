from builder import QRCodeBuilder
from renderer import QRRenderer


builder = QRCodeBuilder()

builder.build_function_patterns()

renderer = QRRenderer()

renderer.render(
    builder.get_matrix(),
    "output/step5_function_patterns.png",
)

print("QR function patterns complete!")