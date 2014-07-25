VENV=venv
BINUTILS=$(VENV)/bin

PIP=$(BINUTILS)/pip
PYTHON=$(BINUTILS)/python

default: deps

deps: $(VENV)
	$(PIP) install -qr requirements.txt

$(VENV):
	virtualenv $@

clean:
	find . -name '*~' -delete
