import qrcode

# Function to create QR code from data
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Thickness of the border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    img.save("qrcode.png")
    print("QR Code generated and saved as 'qrcode.png'")

# Example usage
if __name__ == "__main__":
    data = input("Enter the data (URL, text, etc.): ")
    generate_qr(data)
