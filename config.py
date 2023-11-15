import argparse


class Settings:
    def __init__(self, csv_file: str, csv_encoding: str, port: int):
        self.csv_file = csv_file
        self.csv_encoding = csv_encoding
        self.port = port


def get_settings():
    parser = argparse.ArgumentParser(description="FastAPI server for processing CSV data")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--csv_encoding", default="utf-8-sig", help="Encoding of the CSV file (default: utf-8-sig)")
    parser.add_argument("-p", "--port", type=int, default=8000, help="Port to run the server on (default: 8000)")

    args = parser.parse_args()

    return Settings(args.csv_file, args.csv_encoding, args.port)
