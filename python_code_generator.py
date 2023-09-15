
import qrcode

# URL for the YouTube channel
url = "https://www.wikipedia.org/"

# Generate the QR code
img = qrcode.make(url)

# Save the QR code as a PNG file
img.save("wiki.png")
