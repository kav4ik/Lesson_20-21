import pytesseract
from PIL import Image

# Відкриття зображення
image = Image.open('text_image.png')

# Використання Tesseract для розпізнавання тексту
text = pytesseract.image_to_string(image, lang='ukr')

print(text)
