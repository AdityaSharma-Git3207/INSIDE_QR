import qrcode


class RealQRCode:
    """
    Generates production-grade QR codes.
    """

    def generate(self, text, filename):

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=4,
        )

        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color="black",
            back_color="white",
        )

        img.save(filename)

        print(f"\n✅ QR Version : {qr.version}")
        print(f"✅ Saved to   : {filename}")