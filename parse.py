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


def parse_pdf(pdf, year):
    tables = camelot.read_pdf(pdf, pages='2-end')
    
    if not os.path.exists(year):
        os.mkdir(year)
    
    for table in tables:
        
        adjusted_table = []
        
        for row in table.data:
            adjusted_table.append(adjust_row(row))
        
        page = str(table.parsing_report['page'])
        order = str(table.parsing_report['order'])

        filename = f'{year}_page_{page}_table_{order}.csv'
        dirname = os.path.abspath(year)
        filepath = os.path.join(dirname, filename)

        with open(filepath, mode='w', newline='') as csvf:
            writer = csv.writer(csvf)
            writer.writerows(adjusted_table)


def main():
    with open('odkazy.csv', newline='') as csvf:
        reader = csv.DictReader(csvf)
        
        for row in reader:
            parse_pdf(row['url'], row['year'])


if __name__ == '__main__':
    main()
