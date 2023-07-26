# ocr_module.py

import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this if necessary)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def ocr_image(image_path):
    """
    Perform OCR on the given image and return the extracted text.

    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Extracted text from the image.
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text
