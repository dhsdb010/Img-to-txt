from PIL import Image
import pytesseract
import cv2
import numpy as np

# Load the image
image_path = input('Enter image path: ')
image = cv2.imread(image_path)

# Preprocess the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
denoised_image = cv2.fastNlMeansDenoising(gray_image)
_, binary_image = cv2.threshold(denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Perform OCR
text = pytesseract.image_to_string(binary_image)

# Print the extracted text
print(text)