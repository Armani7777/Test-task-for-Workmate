import csv
from typing import List, Dict, Any
from tabulate import tabulate

def read_csv_file(filepath: str) -> List[Dict[str, Any]]:
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def filter_rows(rows: List[Dict[str, Any]], column: str, op: str, value: str) -> List[Dict[str, Any]]:
    def cast(val):
        try:
            return float(val)
        except ValueError:
            return val

    value_cast = cast(value)
    def cmp(row):
        if column not in row:
            raise ValueError(f"Column '{column}' not found.")
        row_value = cast(row[column])
        if op == ">":
            return row_value > value_cast
        elif op == "<":
            return row_value < value_cast
        elif op == "=":
            return row_value == value_cast
        elif op == ">=":
            return row_value >= value_cast
        elif op == "<=":
            return row_value <= value_cast
        else:
            raise ValueError(f"Unsupported operator: {op}")

    return [row for row in rows if cmp(row)]

def aggregate_column(rows: List[Dict[str, Any]], column: str, operation: str) -> float:
    nums = []
    for row in rows:
        if column not in row:
            raise ValueError(f"Column '{column}' not found.")
        try:
            nums.append(float(row[column]))
        except ValueError:
            raise ValueError(f"Column '{column}' contains non-numeric data.")
    if not nums:
        raise ValueError("No data for aggregation.")
    if operation == "avg":
        return sum(nums) / len(nums)
    elif operation == "min":
        return min(nums)
    elif operation == "max":
        return max(nums)
    else:
        raise ValueError("Supported aggregations: avg, min, max")

def print_table(rows: List[Dict[str, Any]]):
    if rows:
        print(tabulate(rows, headers="keys", tablefmt="grid"))
    else:
        print("No data to display.")