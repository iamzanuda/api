# API Yatube

[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-464646??style=flat-square&logo=Django)]([https://www.djangoproject.com/](https://www.django-rest-framework.org/))
[![JSON Web Token Authentication](https://img.shields.io/badge/-JWT%20Authentication-464646??style=flat-square&logo=Django)](https://www.django-rest-framework.org/api-guide/authentication/#json-web-token-authentication)

**Проект API для социальной сети.**
+ Аутентификация пользователя.
+ Возможность создания, удаления, редактирования, коментирования и подписки на другого автора для аутентифицированного пользователя.
+ Возможность просматривать посты для не аутентифицированного пользователя.

**Используемые технологии:**
+ Django==3.2.16
+ djangorestframework==3.12.4
+ djangorestframework-simplejwt==4.7.2
+ djoser==2.1.0

_Скачать проект можно здесь [**api_final_yatube**](https://github.com/iamzanuda/api_final_yatube)_

### Как запустить проект:

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
![python version](https://img.shields.io/badge/Django-3.2.16-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 
![python version](https://img.shields.io/badge/djangorestframework--simplejwt-4.7.2-yellowgreen)
