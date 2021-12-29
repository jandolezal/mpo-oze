# Obnovitelné zdroje v roce ....

Ministerstvo průmyslu a obchodu (MPO) publikuje každoročně statistickou zprávu Obnovitelné zdroje v roce YYYY ve formě pdf souboru.

Script scrapuje odkazy na tyto pdf zprávy z [webu MPO](https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/) a uloží je jako csv.

Další script z pdf zprávy naparsuje pomocí [Camelot](https://camelot-py.readthedocs.io/) tabulky s daty, odstraní mezery mezi čísly a uloží tabulky jako csv soubory v adresáři pro příslušný rok. Současně uloží pro každý rok excelový soubor (co tabulka, to list).


## Použití

```bash
python3 -m venv venv

pip install mpo-oze

mpo -h
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
