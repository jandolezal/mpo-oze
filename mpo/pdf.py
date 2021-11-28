#!/usr/bin/env python3

import csv
import re
import os

import camelot


def adjust_row(row):
    adjusted_row = []

    for cell in row:
        if ' ' in cell and re.fullmatch(re.compile(r'[^A-Za-z]+'), cell):
            adjusted_cell = cell.replace(' ', '')
            adjusted_row.append(adjusted_cell)
        elif '\n' in cell:
            adjusted_cell = cell.replace('\n', '')
            adjusted_row.append(adjusted_cell)
        else:
            adjusted_row.append(cell)

    return adjusted_row


def parse_pdf(pdf_url, year):
    print(f'Starting parsing the report for the year {year} from {pdf_url}')
    tables = camelot.read_pdf(pdf_url, pages='2-end', suppress_stdout=True)

    if not os.path.exists(year):
        os.mkdir(year)

    # Write all tables directly to excel
    dirpath = os.path.abspath(year)
    excelpath = os.path.join(dirpath, year) + '.xlsx'
    tables.export(excelpath, f='excel')

    for table in tables:

        # If the parsing accuracy is low discard the table
        # These tables are usually not tables but figures (plots)
        if table.parsing_report["accuracy"] < -100.0:
            print(
                f'Skipping table page {table.parsing_report["page"]} order {table.parsing_report["order"]}'
            )
            continue

        # Get rid of spaces between digits for csv files
        adjusted_table = []

        for row in table.data:
            adjusted_table.append(adjust_row(row))

        page = str(table.parsing_report['page'])
        order = str(table.parsing_report['order'])

        csvname = f'{year}_page_{page}_table_{order}.csv'
        csvpath = os.path.join(dirpath, csvname)
        with open(csvpath, mode='w', newline='') as csvf:
            writer = csv.writer(csvf)
            writer.writerows(adjusted_table)

    print(f'Parsing completed.')


def main():
    with open('odkazy.csv', newline='') as csvf:
        reader = csv.DictReader(csvf)

        for row in reader:
            parse_pdf(row['url'], row['year'])


if __name__ == '__main__':
    main()
