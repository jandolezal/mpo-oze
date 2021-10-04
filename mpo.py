import argparse

from links import pdfs_urls_to_csv


def main():
    parser = argparse.ArgumentParser(
        'mpo', description='get data from reports on renewables from MPO'
    )
    parser.add_argument(
        '-u', '--urls', action='store_true', help='scrape pdf urls (default: True)'
    )
    parser.add_argument(
        '-o',
        '--output',
        default='odkazy.csv',
        help='set csv filename for report urls (default: odkazy.csv)',
    )

    args = parser.parse_args()

    if args.urls:
        pdfs_urls_to_csv(args.output)


if __name__ == '__main__':
    main()
