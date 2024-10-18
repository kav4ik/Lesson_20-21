import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Відкриття зображення
image = Image.open('text_image.png')

# Використання Tesseract для розпізнавання тексту
text = pytesseract.image_to_string(image, lang='ukr')

print(text)
