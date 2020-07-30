"""
.. module:: parsing_csv_and_json_files.manipulate_csv_file
   :synopsis: Read, write csv files
"""
import csv
from loguru import logger

example_file_path = "csv_files/example.csv"


def read_from_file():
    opened_file = open(example_file_path)
    return csv.reader(opened_file)


def print_content(contents: csv.reader):
    for content in contents:
        logger.info(f"Row #{contents.line_num}: {content}")


def read_and_print():
    contents = read_from_file()
    print_content(contents)


def create_csv_file():
    def populate_file(output_writer: csv.writer):
        output_writer.writerow(["spam", "egss", "bacon", "ham"])
        output_writer.writerow(["Hello world!", "egss", "bacon", "ham"])
        output_writer.writerow([1, 2, 3.141592, 2.71])

    with open("csv_files/output.csv", "w+") as output:
        output_write = csv.writer(output)
        populate_file(output_write)


if __name__ == "__main__":
    read_and_print()
    create_csv_file()
