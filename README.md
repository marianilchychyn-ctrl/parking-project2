# Паркування

Навчальний Python-проєкт: розрахунок тривалості та вартості стоянки.

## Функції
- `parking_minutes(start_min, end_min)` — тривалість у хвилинах;
- `billable_hours(minutes)` — кількість оплачуваних годин (розпочата година рахується повністю);
- `parking_cost(minutes, rate_per_hour, free_minutes=15)` — вартість стоянки;
- `apply_discount(cost, percent)` — знижка у відсотках.

Некоректні дані (від'ємні значення, знижка поза 0–100) викликають `ValueError`.

## Підготовка
```bash
py -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements-dev.txt
```

## Запуск
```bash
python parking.py
```

## Тести
```bash
python -m pytest -v tests
```

## Структура
```
parking.py            # код
tests/test_parking.py # тести pytest
.github/workflows/    # GitHub Actions
requirements-dev.txt  # залежності для тестів
```

## Ліцензія
Див. файл LICENSE.
