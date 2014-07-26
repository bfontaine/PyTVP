# PyTVP

This repository contains a set of scripts to work with [HATVP][]’s data.

[HATVP]: http://www.hatvp.fr/index.html

## Usage

All scripts are in `scripts/`. Install all dependencies with `make`, then run
each script with:

    venv/bin/python script/the-name-of-the-script.py

## Content

### `get-pdfs.py`

This script retrieves all the website’s PDFs in one directory, `pdfs`. Just run
it and it’ll download each one of them.

    venv/bin/python script/get-pdfs.py

Warning: it takes 1.2GB. Alternatively, you can download all of them as [an
archive][tgz] or through [BitTorrent][torrent].

[tgz]: http://bfontaine.net/hatvp.tgz
[torrent]: http://bfontaine.net/hatvp.torrent
