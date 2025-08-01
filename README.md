# CSV Processor

Скрипт для фильтрации и агрегации данных из CSV-файла через командную строку.

## Описание

* Фильтрация по любой колонке (>, <, =, >=, <=, работает и для числовых, и для строковых данных)
* Агрегация (avg, min, max) по числовым колонкам
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

Агрегация по цене:
```bash
python main.py phones.csv --aggregate "avg:price"
```

<pre>AVG of 'price': 674.0</pre>

Комбинированный пример:
```bash
python main.py phones.csv --filter "brand=xiaomi" --aggregate "max:rating"
```

<pre>MAX of 'rating': 4.6</pre>

Обработка ошибки:
```bash
python main.py phones.csv --filter "unknown_col=val"
```
<pre>Вывод: Invalid filter: Column 'unknown_col' not found.</pre>

## Как запустить тесты
```bash
pytest --cov=csv_processor
```

## Скриншоты результатов

![пример](test_task_for_workmate/test_result_screenshots/test_result_1.jpg)
![пример](test_task_for_workmate/test_result_screenshots/test_result_2.jpg)
