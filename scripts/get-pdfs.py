# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from urlparse import urljoin

BASE_URL = 'http://www.hatvp.fr'

def soup_url(url):
    def _deco(fun):
        def _fun(*args, **kwargs):
            soup = BeautifulSoup(requests.get(BASE_URL + url).content)
            return fun(soup, *args, **kwargs)
        _fun.__name__ = fun.__name__
        return _fun
    return _deco


@soup_url('/consulter-les-declarations-rechercher.html')
def get_pages(soup):
    """
    Yield all pages (not PDFs) from the website
    """
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href or not href.startswith('pages_nominatives/'):
            continue
        yield urljoin(BASE_URL, href)



if __name__ == '__main__':
    pages = get_pages()
    for p in pages:
        print p
