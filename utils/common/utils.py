import pytesseract
from pdfminer.high_level import extract_text as extract_text_from_pdf
from io import BytesIO
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sanje\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_data_from_file(attached_file):
    extracted_data = {}
    
    if attached_file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        try:
            image = Image.open(attached_file)
            text = pytesseract.image_to_string(image)
            
            extracted_data['text'] = text
            
        except Exception as e:
            print("Error while extracting text from image:", e)
            return None
    
    # Check if the attached file is a PDF
    elif attached_file.name.lower().endswith('.pdf'):
        try:
            text = extract_text_from_pdf(attached_file)
            extracted_data['text'] = text
            
        except Exception as e:
            print("Error while extracting text from PDF:", e)
            return None
    
    else:
        print("Unsupported file type")
        return None
    
    return extracted_data