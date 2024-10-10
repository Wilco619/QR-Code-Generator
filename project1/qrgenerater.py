import qrcode
from PIL import Image

def create_qr_with_logo(data, logo_path, output_path, scale=8):
    # Create QR code
    qr = qrcode.make(data)
    qr = qr.convert('RGBA')

    # Open the logo image
    logo = Image.open(logo_path).convert('RGBA')

    # Calculate the size of the logo (e.g., 1/4 of the QR code size)
    logo_size = qr.size[0] // 4
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to place the logo
    position = ((qr.size[0] - logo.size[0]) // 2, (qr.size[1] - logo.size[1]) // 2)

    # Paste the logo onto the QR code
    qr.paste(logo, position, logo)

    # Save the QR code with the logo
    qr.save(output_path, scale=scale)

# Example usage
data = "the quick brown fox jumps over the lazy dog, these are all the alphabets in a single sentence"
logo_path = "project1/file.png"  # Replace with your logo path
output_path = "myqr_with_logo.png"
create_qr_with_logo(data, logo_path, output_path, scale=8)