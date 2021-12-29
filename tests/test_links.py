from os import path
import pathlib

import pytest

from mpo import links


@pytest.mark.skip(reason='This test function would issue GET request to www.mpo.cz')
def test_links():
    links.pdfs_urls_to_csv(filename='tests/test_links.csv')
    with open('tests/test_links.csv') as file:
        lines = file.readlines()
        assert lines[0] == 'year,url\n'
        assert lines[1] == '2020,https://www.mpo.cz/assets/cz/energetika/statistika/obnovitelne-zdroje-energie/2021/9/Obnovitelne-zdroje-energie-2020.pdf\n'
        assert lines[-1] == '2007,https://www.mpo.cz/assets/dokumenty/35392/39800/468163/priloha001.pdf\n'
