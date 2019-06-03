## **Курс Web-разработчик на Python от OTUS**

### **Домашнее задание №6**
Сделать демо интернет-магазина на Django.

### Установка

```консоль
Получение исходного кода приложения:
$ git clone https://github.com/zokMeodoff/otus_hw6.git

Установка зависимостей:
$ cd otus_hw6
$ pip install -r requirements.txt

Миграции:
$ python manage.py migrate

Загрузка данных в БД:
$ python manage.py loaddata categories
$ python manage.py loaddata products

Создание пользователя для админки:
$ python manage.py createsuperuser --username=admin
```

### Запуск

```консоль
$ python manage.py runserver
```

### Работа приложения
Страница со списком продуктов: http://127.0.0.1:8000/products/  
Страница конкретного продукта: http://127.0.0.1:8000/products/1/  
Страница с админкой: http://127.0.0.1:8000/admin/
Предусмотрен переход по ссылкам с главной страницы на страницы конкретных продуктов и возврат со страницы конкретного продукта на главную.









