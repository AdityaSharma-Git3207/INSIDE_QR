from builder import QRCodeBuilder

builder = QRCodeBuilder()

bits = builder.encode_data("HELLO")

print(bits)
print()
print("Length:", len(bits))