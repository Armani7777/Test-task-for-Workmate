import pytest
from csv_processor import filter_rows, aggregate_column

ROWS = [
    {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
    {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
    {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    {"name": "poco x5 pro", "brand": "xiaomi", "price": "299", "rating": "4.4"},
]

def test_filter_greater():
    filtered = filter_rows(ROWS, "price", ">", "500")
    assert len(filtered) == 2
    assert all(float(r["price"]) > 500 for r in filtered)

def test_filter_equal_text():
    filtered = filter_rows(ROWS, "brand", "=", "xiaomi")
    assert len(filtered) == 2
    assert all(r["brand"] == "xiaomi" for r in filtered)

def test_aggregate_avg():
    avg = aggregate_column(ROWS, "price", "avg")
    assert round(avg, 2) == 674.0

def test_aggregate_min():
    assert aggregate_column(ROWS, "rating", "min") == 4.4

def test_aggregate_max():
    assert aggregate_column(ROWS, "rating", "max") == 4.9

def test_aggregate_column_not_found():
    with pytest.raises(ValueError):
        aggregate_column(ROWS, "not_found", "avg")

def test_filter_column_not_found():
    with pytest.raises(ValueError):
        filter_rows(ROWS, "not_found", "=", "test")

def test_aggregate_non_numeric():
    with pytest.raises(ValueError):
        aggregate_column(ROWS, "brand", "avg")