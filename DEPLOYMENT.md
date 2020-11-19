<h1>Инструкция по локальному развёртыванию приложения</h1>

<h3>Получение исходного кода</h3>
Выберите каталог для установки приложения, перейдите в него и выполните команды GIT:<br>
git init<br>
git remote add origin git@github.com:max-belichenko/Django-Polls-API.git<br>
git pull origin main<br>
<br>
<h3>Настройка окружения</h3>
Находясь в каталоге с приложением выполните команды (необходимо использовать Python 3):<br>
python -m venv venv<br>
<b>Linux:</b> source venv/bin/activate<br>
<b>Windows:</b> /venv/Scripts/activate.bat<br> 
<br>
python -m pip install --upgrade pip<br>
cd polls_api<br>
pip install -r requirements.txt<br>
<br>
<h3>Настройка фреймворка</h3>
Перейдите в каталог polls_api/polls_api<br>
Установить значение SECRET_KEY в файле settings.py<br>
Сгенерировать значение можно с помощью Python:<br>
<br>
from django.utils.crypto import get_random_string<br>
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'<br>
get_random_string(50, chars)<br>
<br>
Установить значение ALLOWED_HOSTS в файле settings.py<br>
Для тестирования можно добавить локальный хост '127.0.0.1'<br>
<br>
<h3>Запуск приложения</h3>
Перейдите в каталог polls_api/polls_api<br>
Выполните следующие команды:<br>
pyton manage.py makemigrations<br>
pyton manage.py migrate<br>
pyton manage.py runserver<br>
