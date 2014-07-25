# -*- coding: UTF-8 -*-

import re
import requests
import os
import os.path

BASE_URL = 'http://www.hatvp.fr'


def mk_pdf_url(filename):
    return '%s/files/declarations/%s' % (BASE_URL, filename)


def get_pdf_urls(full=True):
    """
    Yield all PDF URLs from the website. If 'full' is falsy, only the PDF's
    filename is yielded.
    """
    url = '%s/js/data.js' % BASE_URL
    js = requests.get(url).content

    for link in re.findall(r'd\.pdf = "([^.]+\.pdf)"', js):
        yield mk_pdf_url(link) if full else link


def download_pdf(filename, target_dir='pdfs'):
    """
    download a PDF in a given directory. 'pdf' should be the PDF's filename,
    NOT the full URL.
    """
    pdf = requests.get(mk_pdf_url(filename))
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    with open('%s/%s' % (target_dir, filename), 'wb') as f:
        f.write(pdf.content)


if __name__ == '__main__':
    pdfs = get_pdf_urls(False)
    for p in pdfs:
        print p
        download_pdf(p)
