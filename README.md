Щоб pdf2image встановити, нам треба перейти  на сторінку GitHub https://github.com/oschwartz10612/poppler-windows/releases/, скачати та встановити її. Беремо найсвіжішу версію 24.08.0-0. Качаємо її і розпаковуємо архів у зручне місце на вашому комп'ютері, наприклад, C:\poppler.
Далі нам треба додати Poppler до змінної PATH, бо інакше система не буде бачити цю утіліту. Це можна зробити за допомогою Powershell
Натисни комбінацію клавіш Windows + X і вибери Windows PowerShell (Admin) або знайди PowerShell у меню "Пуск", клацни правою кнопкою миші та вибери Запуск від імені адміністратора.
Додавання шляху до Poppler в PATH: У вікні PowerShell виконайте наступну команду, щоб додати шлях до папки bin Poppler у системну змінну PATH:

[System.Environment]::SetEnvironmentVariable("Path", $Env:Path + ";C:\poppler\Library\bin", [System.EnvironmentVariableTarget]::Machine)

C:\poppler\Library\bin — це шлях до папки bin у розпакованій директорії Poppler. 

Якщо ви розпакували Poppler в інше місце, замініть цей шлях на відповідний.

[System.EnvironmentVariableTarget]::Machine 

— додає зміни до системної змінної PATH для всіх користувачів комп'ютера.
Закрийте та знову відкрийте PowerShell, щоб переконатися, що зміни набули чинності. Виконаємо наступну команду: $Env:Path
Це виведе всі шляхи, які містяться у змінній PATH. Якщо, серед них є C:\poppler\Library\bin, то шлях був змінений вірно.

pdfinfo.exe --version

Якщо на екрані не з’явиться поточна версія програми, то скоріше за все Поплер не працює на вашому компі.


В PowerShell виконуємо команду 

wsl --install

wsl --list --verbose

Ця команда відобразить список встановлених Linux-дистрибутивів і версію WSL. 

cd ~ # Переходимо у домашню директорію.

mkdir MyProjects # Створюємо папку для всіх проєктів.

cd MyProjects/ # Переходимо в цю папку. 

mkdir pdfToText # Створюємо окремий проект для роботи з PDF. 

cd pdfToText/ # Заходимо в папку проєкту.

Далі оновіть систему та встановіть pip — менеджер пакетів Python:

sudo apt update 

sudo apt install python3-pip

pip install virtualenv # Інсталюємо інструмент virtualenv. python3 -m virtualenv venv # Створюємо віртуальне середовище "venv". source venv/bin/activate # Активуємо це середовище.
Далі встановіть Tesseract для розпізнавання тексту:

sudo apt install tesseract-ocr 

sudo apt install tesseract-ocr-ukr # Інсталюємо підтримку української мови.

sudo apt install poppler-utils

Встановіть необхідні бібліотеки для роботи з PDF та зображеннями

pip install pytesseract pillow pdf2image

wget https://raw.githubusercontent.com/Nikcenter/Lesson_20/refs/heads/main/imagepdf_text.py
