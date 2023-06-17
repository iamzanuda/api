### Как запустить проект api_yatube:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/iamzanuda/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
