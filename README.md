# Renewables in YYYY

The Czech Ministry of Industry and Trade (Ministerstvo průmyslu a obchodu, MPO) each year publishes a statistical report [Renewable Energy Resources in YYYY](https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/obnovitelne-zdroje-energie-v-roce-2020--263512/) in the form of a PDF file which contains statistics about renewable energy production in the country.

This package provides two commands for scraping links to these PDF reports and parsing tables in ther reports (for selected year).

One script scrapes links to these PDF reports from the [website](https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/) and saves them to CSV.

Another script parses selected pdf report using [Camelot](https://camelot-py.readthedocs.io/):
* reads data tables,
* removes spaces between numbers and
* saves tables as CSV files in the directory for the relevant year. It also saves one Excel file for the year (one worksheet per table).

## Instalation

```bash
python3 -m venv venv

pip install mpo-oze
```

## Usage

```bash
# Scrape links to csv file
mpo links

# Parse 2020 report
mpo pdf -y 2020

# Show 2019 report in a browser
mpo show -y 2019

# Parse only tables from page 5
mpo pdf -y 2020 -p 5
```

```
usage: mpo [-h] [-y YEAR] [-p PAGES] {links,pdf,show}

parse czech renewable energy pdf reports

positional arguments:
  {links,pdf,show}      scrape links to reports, parse report or show report
                        in a browser

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  select report year of interest (default: 2020)
  -p PAGES, --pages PAGES
                        select pages, e.g. 1,3-5,7-end (default: 2-end)

```
