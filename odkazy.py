#!/usr/bin/env python3

import re
import csv
import requests
from bs4 import BeautifulSoup


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
        report_url_list.append({
            'year': year,
            'url': download_url,
        })
    
    return report_url_list


def main():
    headers = {'user-agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0'}
    
    domain = 'https://www.mpo.cz'
    
    urls = [
        'https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/',
        'https://www.mpo.cz/cz/energetika/statistika/obnovitelne-zdroje-energie/archiv.htm'
    ]

    post_urls_list = []

    for url in urls:
        post_urls_list += gather_post_urls(url, domain, headers)
    
    pdf_url_list = gather_pdf_urls(post_urls_list, domain, headers)

    with open('odkazy.csv', 'w', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=['year', 'url'])
        writer.writerows(pdf_url_list)


if __name__ == '__main__':
    main()
