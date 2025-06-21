import argparse
import sys
from csv_processor import filter_rows, aggregate_column, read_csv_file, print_table

def parse_filter(condition):
    for op in [">=", "<=", ">", "<", "="]:
        if op in condition:
            key, value = condition.split(op, 1)
            return key.strip(), op, value.strip()
    raise ValueError("Supported operators: >, <, =, >=, <=")

def main():
    parser = argparse.ArgumentParser(description="Process and analyze CSV files.")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("--filter", help="Filter condition, e.g., price>500 or brand=xiaomi", default=None)
    parser.add_argument("--aggregate", help="Aggregation, format: operation:column (e.g., avg:price)", default=None)

    args = parser.parse_args()

    try:
        rows = read_csv_file(args.file)
    except FileNotFoundError:
        print(f"File '{args.file}' not found.")
        sys.exit(1)

    if args.filter:
        try:
            key, op, value = parse_filter(args.filter)
            rows = filter_rows(rows, key, op, value)
        except Exception as e:
            print(f"Invalid filter: {e}")
            sys.exit(2)

    if args.aggregate:
        try:
            op, col = args.aggregate.split(":", 1)
            result = aggregate_column(rows, col, op)
            print(f"{op.upper()} of '{col}': {result}")
        except Exception as e:
            print(f"Invalid aggregation: {e}")
            sys.exit(3)
    else:
        print_table(rows)

if __name__ == "__main__":
    main()