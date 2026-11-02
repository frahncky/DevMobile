# Compila os slides do curso DevMobile
MODULOS := $(wildcard modulos/modulo*.tex)
PDFS    := $(patsubst modulos/%.tex,pdf/%.pdf,$(MODULOS))
LATEXMK := latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all verificar limpar

all: $(PDFS)

pdf/%.pdf: modulos/%.tex estilo/devmobile.sty
	cd modulos && $(LATEXMK) $*.tex
	@mkdir -p pdf && cp modulos/$*.pdf $@

# make modulo04  ->  compila apenas o módulo 04
modulo%:
	$(MAKE) $(patsubst modulos/%.tex,pdf/%.pdf,$(wildcard modulos/modulo$*-*.tex))

verificar: all
	python3 ferramentas/verificar_layout.py modulos/*.pdf

limpar:
	cd modulos && latexmk -c
	rm -f modulos/*.vrb modulos/*.listing modulos/*.nav modulos/*.snm
