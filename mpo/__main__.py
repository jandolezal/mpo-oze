import argparse
import csv

from mpo import links
from mpo import pdf


def main():
    parser = argparse.ArgumentParser(
        prog='mpo',
        description='parse tables in reports on renewables from MPO',
    )
    parser.add_argument(
        'subcommand',
        choices=['links', 'pdf'],
        help='scrape links to reports or the report pdf itself',
    )
    parser.add_argument(
        '-y',
        '--year',
        default='2020',
        help='select report year of interest (default: 2020)',
    )

    args = parser.parse_args()

    # Get report urls
    if args.subcommand == 'links':
        links.pdfs_urls_to_csv()
    # Parse report of interest
    elif args.subcommand == 'pdf':
        report_url = links.get_url_for_year(args.year)
        pdf.parse_pdf(report_url, args.year)
    else:
        print('Please use -h flag to see the options.')


if __name__ == '__main__':
    main()
