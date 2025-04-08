from pdf2image import convert_from_path
import pytesseract

# Make sure Tesseract is correctly configured (you might need to set the path on some systems)
# pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'  # For Windows, set path here

def convert_pdf_to_images(pdf_file):
    # Convert PDF to images using pdf2image
    images = convert_from_path(pdf_file)
    
    # Use pytesseract to extract text from each image
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    
    return text


print(convert_pdf_to_images("resume.pdf"))  # Replace with your PDF file path