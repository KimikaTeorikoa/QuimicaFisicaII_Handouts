# Química Física II — compilación de apuntes y figuras
#
#   make            compila todos los documentos
#   make figuras    regenera todas las figuras (ejecuta los cuadernos)
#   make tema03     compila un documento suelto
#   make limpiar    borra los auxiliares

PYTHON  ?= $(HOME)/opt/anaconda3/bin/python3
LATEX   ?= pdflatex -interaction=nonstopmode -halt-on-error

TEMAS      := tema01 tema02 tema03 tema04 tema05 tema06 tema07 tema09 tema10
MATES      := math01 math02
PRACTICAS  := practicas_exp_normativa practicas_exp_uvvis practicas_exp_ir
EJERCICIOS := $(basename $(wildcard ejercicios/ejercicios_*.tex))
TODOS      := $(TEMAS) $(MATES) $(PRACTICAS) $(EJERCICIOS)

CUADERNOS  := $(wildcard notebooks/nb*.ipynb)

.PHONY: all figuras limpiar limpiar-todo comprobar $(TODOS)

all: $(TODOS)

$(TODOS):
	@printf '%-34s ' '$@'
	@$(LATEX) $@.tex >/dev/null 2>&1 && echo OK || { echo FALLA; \
	  grep -m1 -A3 '^!' $@.log; exit 1; }

# Regenera todas las figuras en figs/ ejecutando los cuadernos.
# Los .ipynb no se modifican: se ejecutan en memoria, sin guardar salidas.
figuras:
	@$(PYTHON) notebooks/run_notebooks.py

# Compila todo sin abortar al primer fallo: informe completo del estado
comprobar:
	@echo "documento                          estado"
	@echo "-----------------------------------------"
	@fail=0; for d in $(TODOS); do \
	  printf '%-34s ' "$$d"; \
	  if $(LATEX) $$d.tex >/dev/null 2>&1; then echo OK; \
	  else echo FALLA; fail=1; fi; \
	done; \
	echo "-----------------------------------------"; \
	if [ $$fail -eq 0 ]; then echo "todo compila"; \
	else echo "hay documentos que no compilan"; exit 1; fi

limpiar:
	@rm -f *.aux *.log *.out *.toc *.bbl *.blg *.idx *.ilg *.ind \
	       ejercicios/*.aux ejercicios/*.log ejercicios/*.out
	@echo "auxiliares eliminados"

limpiar-todo: limpiar
	@rm -f $(addsuffix .pdf,$(TODOS))
	@echo "PDF eliminados"
