import pytesseract
from PIL import Image

# тільки для користувачів Віндоуз, якщо ні, то видаліть цю строку
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Відкриття зображення
image = Image.open('text_image.png')

# Використання Tesseract для розпізнавання тексту
text = pytesseract.image_to_string(image, lang='ukr')

# Збереження тексту у файл
with open('recognized_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("Текст було збережено у файл recognized_text.txt")
