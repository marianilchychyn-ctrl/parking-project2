import pytest

from parking import apply_discount, billable_hours, parking_cost, parking_minutes


@pytest.mark.parametrize("start, end, expected", [
    (0, 60, 60),
    (540, 680, 140),
    (100, 100, 0),
])
def test_parking_minutes(start, end, expected):
    assert parking_minutes(start, end) == expected


@pytest.mark.parametrize("minutes, expected", [
    (0, 0),
    (1, 1),
    (60, 1),
    (61, 2),
])
def test_billable_hours(minutes, expected):
    assert billable_hours(minutes) == expected


@pytest.mark.parametrize("minutes, rate, expected", [
    (10, 20, 0.0),
    (61, 20, 40.0),
    (120, 15.5, 31.0),
])
def test_parking_cost(minutes, rate, expected):
    assert parking_cost(minutes, rate) == pytest.approx(expected)


def test_discount_float():
    assert apply_discount(33.3, 10) == pytest.approx(29.97)


def test_negative_duration_raises():
    with pytest.raises(ValueError):
        parking_minutes(100, 50)


def test_negative_minutes_raises():
    with pytest.raises(ValueError):
        billable_hours(-1)


def test_negative_rate_raises():
    with pytest.raises(ValueError):
        parking_cost(60, -5)


def test_bad_discount_raises():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
