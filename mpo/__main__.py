import argparse
import csv
import pathlib

from mpo import links, pdf, show


def main():
    parser = argparse.ArgumentParser(
        prog='mpo',
        description='parse czech renewable energy pdf reports',
    )
    parser.add_argument(
        'subcommand',
        choices=['links', 'pdf', 'show'],
        help='scrape links to reports, parse report or show report in a browser',
    )
    parser.add_argument(
        '-y',
        '--year',
        default='2020',
        help='select report year of interest (default: 2020)',
    )
    parser.add_argument(
        '-p',
        '--pages',
        default='2-end',
        help='select pages, e.g. 1,3-5,7-end (default: 2-end)',
    )
    args = parser.parse_args()

    # Get report urls
    if not pathlib.Path('links.csv').exists():
        links.pdfs_urls_to_csv()
    # Open report in a browser
    if args.subcommand == 'links':
        pass
    elif args.subcommand == 'show':
        report_url = links.get_url_for_year(args.year)
        show.open_report_page(report_url)
    # Parse report of interest
    elif args.subcommand == 'pdf':
        report_url = links.get_url_for_year(args.year)
        pdf.parse_pdf(pdf_url=report_url, year=args.year, pages=args.pages)
    else:
        print('Please use -h flag to see the options.')


if __name__ == '__main__':
    main()
