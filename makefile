TEX_ENGINE = xelatex
OPR_SYSTEM = $(shell uname -s)

ifeq ($(OPR_SYSTEM), Darwin)
	DOC_VIEWER = open -a Preview
else
	DOC_VIEWER = zathura
endif

draft:
	python -m main
	cd brew && $(TEX_ENGINE) main
	$(DOC_VIEWER) brew/main.pdf

.PHONY: draft final ready clean

final:
	sed -i.bak 's/\[draft\]//' brew/main.tex
	cd brew && $(TEX_ENGINE) main
	$(DOC_VIEWER) brew/main.pdf

ready:
	mkdir -p brew
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \
	deactivate

clean:
	find . -type d -name __pycache__ | xargs rm -fr
	find . -type f -name "*.pyc" | xargs rm -fr
	find brew -type f -name "*.aux" | xargs rm -rf
	find brew -type f -name "*.log" | xargs rm -rf
	find brew -type f -name "*.pdf" | xargs rm -rf
	find brew -type f -name "*.tex" | xargs rm -rf
