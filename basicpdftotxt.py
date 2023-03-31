import os
!pip install PyMuPDF
!pip install fitz
import fitz

# Create the static directory if it doesn't exist
if not os.path.exists('static'):
    os.mkdir('static')

# OCR the PDF using the default 'text' parameter
with fitz.open('GI_LIVER.pdf') as doc:
    # Save the text to file
    text = ""
    for page in doc:
        text += page.get_text()
    with open('static/GI_LIVER.txt', 'w') as f:
        f.write(text)
