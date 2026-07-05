from real_qr import RealQRCode

qr = RealQRCode()

text = input("Enter text or URL: ")

filename = input("Output filename (without extension): ")

qr.generate(
    text,
    f"output/{filename}.png",
)

print(f"\nQR Code saved as output/{filename}.png")