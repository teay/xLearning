import pytesseract
from PIL import Image

# Open your image as an instance of the Pillow Image library
#im = Image.open("your_image.tif")
#im = Image.open(r"C:\path\to\file\your_image.tif")
#im = Image.open(r"C:\path\to\file\your_image.tif")
im = Image.open(r"C:\GitHub\xLearning\Python\OCR\your_image.tif")

# Get rid of alpha channel (only if present)
im = im.convert()

# Save the image as a JPEG
with open("your_image.jpeg", mode="wb") as f:
        im.save(f, format='JPEG',quality=85)

# Use OCR on the converted jpeg image
text = pytesseract.image_to_string(Image.open(f"{im._getexif().get('Make', 'unknown')}_{im._getexif().get('Model', 'unknown')}_ocr.jpg"))
print(text.strip()) # this line prints any extracted text