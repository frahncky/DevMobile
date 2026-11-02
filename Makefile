# Compila os slides do curso DevMobile
# 21 módulos (00 a 20) em duas trilhas: comum + Kotlin e comum + Flutter.
# Cada módulo é compilado dentro da própria pasta; o estilo fica em estilo/
# e a teoria compartilhada em modulos/fundamentos/.

TRILHAS     := comum kotlin flutter
MODULOS     := $(foreach t,$(TRILHAS),$(wildcard modulos/$(t)/modulo*.tex))
PDFS        := $(patsubst modulos/%.tex,pdf/%.pdf,$(MODULOS))
FUNDAMENTOS := $(wildcard modulos/fundamentos/*.tex)
LATEXMK     := latexmk -pdf -interaction=nonstopmode -halt-on-error

.PHONY: all $(TRILHAS) verificar limpar

all: $(PDFS)

# make kotlin  ->  só a trilha Kotlin (sem os módulos comuns)
$(TRILHAS):
	$(MAKE) $(filter pdf/$@/%,$(PDFS))

pdf/%.pdf: modulos/%.tex estilo/devmobile.sty $(FUNDAMENTOS)
	cd $(dir modulos/$*) && $(LATEXMK) $(notdir $*).tex
	@mkdir -p $(dir $@) && cp modulos/$*.pdf $@

# make modulo05  ->  compila o módulo 05 de todas as trilhas
modulo%:
	$(MAKE) $(patsubst modulos/%.tex,pdf/%.pdf,$(wildcard modulos/*/modulo$*-*.tex))

verificar: all
	python3 ferramentas/verificar_layout.py $(MODULOS:.tex=.pdf)

limpar:
	for t in $(TRILHAS); do (cd modulos/$$t && latexmk -c && rm -f *.vrb *.listing *.nav *.snm); done
