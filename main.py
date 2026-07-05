from builder import QRCodeBuilder

builder = QRCodeBuilder()

bits = builder.encode_data("HELLO")

print(bits)