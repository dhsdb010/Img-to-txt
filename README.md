# OCR Image Text Extractor

This Python script performs Optical Character Recognition (OCR) on an input image to extract text content. It uses OpenCV for image preprocessing and Tesseract for OCR.

## Features

- Image preprocessing: grayscale conversion, denoising, and binarization
- Text extraction using Tesseract OCR
- Option to save the preprocessed image for debugging

## Requirements

- Python 3.6+
- OpenCV
- NumPy
- Pytesseract
- Tesseract OCR engine

See `requirements.txt` for specific version information.

## Installation

1. Clone this repository or download the script.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Place your input image in a known location.
2. Enter the `image_path` variable in the script with the path to your image.
3. Run the script:
   ```
   python main.py
   ```
4. The extracted text will be printed to the console.
5. A preprocessed version of the image will be saved as 'preprocessed_image.png' in the same directory.
