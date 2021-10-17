#!/usr/bin/env python3

"""
MPO publikuje každoročně zprávu Obnovitelné zdroje v roce RRRR se
statistikami výroby energií z OZE.
Modul pro scrapování odkazů na tyto pdf zprávy a jejich uložení ve formátu csv.

year,url
2020,https://www.mpo.cz/path/to/pdf
...,...
"""


import re
import csv
import requests
from bs4 import BeautifulSoup


HEADERS = {
    'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'
}

BASE_URL = 'https://www.mpo.cz'

START_URLS = [
    'https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/',
    'https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/archiv.htm',
]


def gather_post_urls(url, domain, headers):
    post_url_list = []

    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    a_tags_list = bs.find_all('a', text=re.compile('zdroje energie v roce'))

    for a in a_tags_list:
        post_url_list.append(domain + a.attrs['href'])

    return post_url_list


def gather_pdf_urls(post_url_list, domain, headers):
    report_url_list = []

    for post_url in post_url_list:
        r = requests.get(post_url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')

        download_url = domain + bs.find('a', {'class': 'download'}).attrs['href']
        year = re.search(re.compile('\d{4}'), post_url).group(0)
        report_url_list.append(
            {
                'year': year,
                'url': download_url,
            }
        )

    return report_url_list


def pdfs_urls_to_csv(
    filename='odkazy.csv', urls=START_URLS, base_url=BASE_URL, headers=HEADERS
):

    post_urls_list = []

    for url in urls:
        post_urls_list += gather_post_urls(url, base_url, headers)

    pdf_url_list = gather_pdf_urls(post_urls_list, base_url, headers)

    with open(filename, 'w', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['year', 'url'])
        writer.writeheader()
        writer.writerows(pdf_url_list)


def get_url_for_year(year: str):
    with open('odkazy.csv', newline='') as csvf:
        reader = csv.DictReader(csvf)
        for row in reader:
            if row['year'] == year:
                return row['url']
    return None


if __name__ == '__main__':
    pdfs_urls_to_csv()
