import csv
import os
import sys


def is_valid_integer(value):
    if value is None:
        return False
    try:
        int(value)
        return True
    except ValueError:
        return False


def read_csv(path, encoding='utf-8-sig'):
    if not os.path.exists(path):
        print(f"Error: File not found at path: {os.path.abspath(path)}")
        sys.exit(1)

    required_header = [
        "PLAYER", "POSITION", "FTM", "FTA", "2PM", "2PA", "3PM", "3PA", "REB", "BLK", "AST", "STL", "TOV"
    ]

    with open(path, "r", encoding=encoding) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames

        if header != required_header:
            print(f"Error: Incorrect CSV format. Expected header: {', '.join(required_header)}")
            sys.exit(1)

        data = []
        for row in reader:
            if len(row) != len(header):
                print(f"Error: Row length does not match the header length in row: {row}")
                sys.exit(1)

            for key, value in row.items():
                if key not in ["PLAYER", "POSITION"] and not is_valid_integer(value):
                    print(f"Error: Invalid value '{value}' for column '{key}' in row: {row}")
                    sys.exit(1)
            data.append(row)

    return data
