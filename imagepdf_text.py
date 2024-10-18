from pdf2image import convert_from_path
import pytesseract

# тільки для користувачів Віндоуз, якщо ні, то видаліть цю строку
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Конвертуємо PDF у зображення
pages = convert_from_path('document.pdf', 300)

# Обробляємо кожну сторінку PDF
for page_number, page_image in enumerate(pages):
    text = pytesseract.image_to_string(page_image, lang='ukr')
    print(f"Текст зі сторінки {page_number + 1}:")
    print(text)
