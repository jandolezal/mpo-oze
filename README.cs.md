# Obnovitelné zdroje v roce ....

Ministerstvo průmyslu a obchodu (MPO) publikuje každoročně statistickou zprávu Obnovitelné zdroje v roce YYYY ve formě pdf souboru.

Script scrapuje odkazy na tyto pdf zprávy z [webu MPO](https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/) a uloží je jako csv.

Další script z pdf zprávy naparsuje pomocí [Camelot](https://camelot-py.readthedocs.io/) tabulky s daty, odstraní mezery mezi čísly a uloží tabulky jako csv soubory v adresáři pro příslušný rok. Současně uloží pro každý rok excelový soubor (co tabulka, to list).


## Použití

`python3 -m venv venv`

`python3 setup.py install`

`mpo -h`


```
usage: mpo [-h] [-y YEAR] {links,pdf}

parse tables in reports on renewables from MPO

positional arguments:
  {links,pdf}           scrape links to reports or the report pdf itself

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  select report year of interest (default: 2020)

```