# QR-Code-Generator
This script generates a QR code from user-provided input (URL, text, etc.) and saves it as an image.

 Requirements
qrcode library
pip install qrcode[pil]

import qrcode

# Function to create QR code from data
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the QR code image
    img = qr.make_image(fill='black', back_color='white')
    img.save("qrcode.png")
    print("QR Code generated and saved as 'qrcode.png'")

# Example usage
if __name__ == "__main__":
    data = input("Enter the data (URL, text, etc.): ")
    generate_qr(data)
