### Как запустить проект:

Скачать проект можно здесь [**api_final_yatube**](https://github.com/iamzanuda/api_final_yatube)

**Клонировать репозиторий и перейти в него в командной строке:**

```
git clone https://github.com/iamzanuda/api_final_yatube.git
```

```
cd api_final_yatube
```

**Cоздать и активировать виртуальное окружение:**

```
python -m venv env
```

```
source venv/Scripts/activate
```

**Установить зависимости из файла requirements.txt:**

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python manage.py migrate
```

**Запустить проект:**

```
python manage.py runserver
```
![python version](https://img.shields.io/badge/Python-3.9-yellowgreen) 
![python version](https://img.shields.io/badge/Django-2.2.16-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework--simplejwt-5.1-yellowgreen)
