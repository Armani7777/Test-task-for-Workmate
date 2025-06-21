# CSV Processor

Скрипт для фильтрации и агрегации данных из CSV-файла через командную строку.

## Описание

* Фильтрация по любой колонке (>, <, =, >=, <=, работает и для числовых, и для строковых данных)
* Агрегация (avg, min, max) по числовым колонкам
* Красивый вывод таблицы в консоль (с помощью tabulate)
* Обработка ошибок (несуществующая колонка, неправильная агрегация и т.д.)

## Требования

* Python 3.8+
* Зависимости: pip install tabulate pytest pytest-cov

## Пример файла

```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
poco x5 pro,xiaomi,299,4.4
```

## Примеры запуска

Фильтрация по бренду:

python main.py phones.csv --filter "brand=xiaomi"

+---------------+---------+---------+----------+
| name          | brand   |   price |   rating |
+===============+=========+=========+==========+
| redmi note 12 | xiaomi  |     199 |      4.6 |
+---------------+---------+---------+----------+
| poco x5 pro   | xiaomi  |     299 |      4.4 |
+---------------+---------+---------+----------+

Агрегация по цене:

python main.py phones.csv --aggregate "avg:price"

AVG of 'price': 674.0

Комбинированный пример:

python main.py phones.csv --filter "brand=xiaomi" --aggregate "max:rating"

MAX of 'rating': 4.6

Обработка ошибки:

python main.py phones.csv --filter "unknown_col=val"
## Вывод: Invalid filter: Column 'unknown_col' not found.

## Как запустить тесты

pytest --cov=csv_processor

## Скриншоты результатов

![пример](Test_task_for_Workmate/test_result_screenshots/test_result_1.jpg)
![пример](Test_task_for_Workmate/test_result_screenshots/test_result_2.jpg)
