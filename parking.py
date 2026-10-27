"""Паркування: тривалість і вартість стоянки."""
import math


def parking_minutes(start_min: int, end_min: int) -> int:
    """Тривалість у хвилинах (час задано хвилинами від початку доби)."""
    if end_min < start_min:
        raise ValueError("Кінець раніше за початок")
    return end_min - start_min


def billable_hours(minutes: int) -> int:
    """Кожна розпочата година оплачується повністю."""
    if minutes < 0:
        raise ValueError("Тривалість не може бути від'ємною")
    return math.ceil(minutes / 60)


def parking_cost(minutes: int, rate_per_hour: float, free_minutes: int = 15) -> float:
    """Вартість стоянки: перші free_minutes безкоштовні."""
    if rate_per_hour < 0:
        raise ValueError("Тариф не може бути від'ємним")
    if minutes <= free_minutes:
        return 0.0
    return billable_hours(minutes) * rate_per_hour


def apply_discount(cost: float, percent: float) -> float:
    """Знижка у відсотках (0-100)."""
    if not 0 <= percent <= 100:
        raise ValueError("Знижка має бути від 0 до 100")
    return cost * (1 - percent / 100)


if __name__ == "__main__":
    m = parking_minutes(9 * 60, 11 * 60 + 20)
    print(f"Тривалість: {m} хв, вартість: {parking_cost(m, 20)} грн")
