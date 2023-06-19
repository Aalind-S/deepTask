#import PyPDF2 as pypdf
from pdf2image import convert_from_path
import csv
from PIL import Image
import pytesseract
import sys
#import fitz

def extract_kv_pairs(file_name):
    # checking if the file is pdf or image
    if file_name.lower().endswith('.pdf'):
        return extract_kv_pairs_pdf(file_name)
    else:
        return extract_kv_pairs_img(file_name)
    

def extract_kv_pairs_pdf(file_name):
        # now extracting text using extractText method
        # referred to documentation
        text = ""
        images = convert_from_path(file_name)
        extracted_image_text = []
        for image in images:
            image_text = pytesseract.image_to_string(image)
            extracted_image_text += image_text

        text += ''.join(extracted_image_text)
        return extract_text(text)
    

def extract_kv_pairs_img(file_name):
    extracted_text = pytesseract.image_to_string(Image.open(file_name))
    return extract_text(extracted_text)




def extract_text(text):
    map_of_pairs = {}
    lines = text.split('\n') #creates a list of lines from the text
    for line in lines:
        line = line.strip()
        if not line:
            continue

        if ':' in line:
            key, value = line.split(":", 1)
            key, value = key.strip(), value.strip()

            if value is not None:
                map_of_pairs[key] = value
    
    return map_of_pairs



"""def write_to_csv(data, csv_file):
    with open(csv_file, 'w', newline='') as csv_data:
        writer = csv.writer(csv_data)

        writer.writerow(['Key', 'Value'])
        for key, value in data.items():
            writer.writerow([key, value])

    return csv_file"""

#extracted_data = extract_kv_pairs('sample2.pdf')
#write_to_csv(extracted_data, "csv_file")
