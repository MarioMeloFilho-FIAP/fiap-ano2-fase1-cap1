SHELL := /bin/bash

all: prep-venv clean

prep-venv: 
	python3 -m venv fiap_ano2_fase1_cap1_venv && \
	source fiap_ano2_fase1_cap1_venv/bin/activate && \
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -r requirements.txt && \
	python3 -m pip install -e . && \
	/bin/bash

clean:
	-rm -rf fiap_ano2_fase1_cap1_venv
