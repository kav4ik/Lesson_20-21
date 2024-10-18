import pdfx
import re
import os
from pprint import pprint

def parse_pdf(pdfFile, regexStrings, region):
    relation = {}  # Словник для збереження розпарсеної інформації
    pdf = pdfx.PDFx(pdfFile)  # Створення об'єкта PDFx для взаємодії з PDF
    text = pdf.get_text()  # Витягнення тексту з PDF
    
    # Цикл по кожному регулярному виразу
    for i in range(len(regexStrings)):
        try:
            # Компіляція регулярного виразу з прапорами DOTALL та MULTILINE
            regex = re.compile(regexStrings[i][1], re.DOTALL | re.MULTILINE)
            regexVar = regex.search(text)  # Пошук шаблону в тексті
            
            if regexVar:
                # Витягнення знайденої групи та видалення символів нового рядка
                stringStripN = regexVar.group(regexStrings[i][2]).strip('\n')
                # Заміна залишкових символів нового рядка на пробіли
                replaceS = stringStripN.replace('\n', ' ')
                
                # Якщо парсимо "place", додаємо рядок регіону до значення
                if regexStrings[i][0] == "place":
                    relation[regexStrings[i][0]] = region + ' ' + replaceS
                else:
                    relation[regexStrings[i][0]] = replaceS
            else:
                # Якщо збіг не знайдено, виводимо повідомлення та встановлюємо значення за замовчуванням у словнику
                print(f'Дані відсутні')
                relation[regexStrings[i][0]] = 'Дані відсутні'
        except AttributeError:
            # Обробка випадку, коли результат пошуку regex є None (AttributeError при зверненні до .group())
            print(f'Дані відсутні')
            relation[regexStrings[i][0]] = 'Дані відсутні'
    
    # Виведення словника розпарсеної інформації
    pprint(relation)

def regex_strings(directory, region):
    # Список регулярних виразів для парсингу різних полів з PDF
    regexStrings = [
        ["number", r"(\d{10}:\d{2}:\d{3}:\d{4})", 0],  # Парсинг номера ділянки
        ["area", r"(Площа.*ділянки.*Місце розташування)(.*)(\n\d+[\.]?\d*\n)({region})", 3],  # Парсинг площі
        ["place", r"(область.{1,90}рад[и|а])", 0],  # Парсинг місця
        ["price", r"(Значення, гривень\n)(.*)(\n\d{3,}[\.\d+]+)", 3],  # Парсинг ціни
        ["name_owner", r"(Прізвище.* фізичної)(.*)(\n[А-ЩЬЮЯЇІЄҐ]\w+[-]*\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\n)", 3],  # Парсинг прізвища власника
        ["company_owner", r"(права власності.+)(\n+.*\n+.+)(\n+)(.+юрид.+)(\n+)(.+)(\n|\s)(.+)", 8],  # Парсинг компанії-власника
        ["date_register", r"(Дата державної.*)(\n\n\d\d\.\d\d\.\d{4})", 2],  # Парсинг дати реєстрації
        ["rent_company", r"(право оренди земельної ділянки)(\n*)(.+)\"|»\n", 3],  # Парсинг компанії-орендаря
        ["rent_person", r"(право оренди земельної ділянки)(\n*[А-ЩЬЮЯЇІЄҐ]\w+[-]*\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\s[А-ЩЬЮЯЇІЄҐ]\w+\n*)", 2]  # Парсинг фізичної особи-орендаря
    ]

    # Ітерація по всіх файлах у вказаній директорії
    for file in os.listdir(directory):
        if file.endswith('.pdf'):  # Обробляти лише файли з розширенням .pdf
            pdfFile = os.path.join(directory, file)  # Отримати повний шлях до PDF файлу
            parse_pdf(pdfFile, regexStrings, region)  # Викликати функцію parse_pdf для парсингу PDF

    print('Готово!')  # Вказує, що парсинг завершено

# Виклик функції regex_strings з директорією та регіоном
regex_strings(r'.\files', 'Миколаївська')
