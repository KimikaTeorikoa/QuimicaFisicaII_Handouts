# CHECKPOINT

## Current Goal

Revisar y completar los apuntes de Química Física II siguiendo `REVIEW_PLAN.md`,
tema por tema. Tema 1 terminado; faltan las mejoras 🔵 y propagar el estilo al resto.

## Work Done

### Session 2026-08-28

- Añadidos 5 retratos de dominio público de Wikimedia Commons (Planck, Einstein
  1905, de Broglie, Heisenberg h.1927, Bohr) en `figs/retratos/`, con procedencia
  completa en `CREDITOS.md` y `creditos.json`.
- Macro `\retrato` = `marginfigure` sin `\caption`: no consume números de figura
  ni afecta a los `\ref` existentes. Con aire arriba y abajo.
- Rayleigh descartado: el margen de la p. 1 no da para ponerlo junto a su nombre.
- Corregidos 4 puntos de terminología física (sección B): fuerza centrípeta y no
  centrífuga en Bohr; el principio de incertidumbre ya no se presenta como límite
  del aparato de medida; ondulatorias; onda-partícula.
- Cerrados 5 huecos de razonamiento (C): enunciado de equipartición; por qué
  $h\nu\gg k_BT$ evita la catástrofe; $\Phi$ antes que $\nu_0$; por qué colapsa el
  átomo clásico; enlace $E_n\to$ Rydberg y fracaso de Bohr más allá del H.
- Ajustes de redacción (D) y eliminada la relación $\Delta E\,\Delta t$ por
  decisión de David (el tiempo no es un observable).
- Fig. 4: `protón (térmico)` → `protón (300 K)`, velocidad calculada en el
  cuaderno desde $T$; C$_{60}$ con su velocidad de haz.

## Current State

| Qué | Estado |
|---|---|
| tema01 | terminado, 8 páginas, 0 overfull |
| Compilación global | falla en tema04, tema06, math01, math02 |
| Remotos | GitHub `main` y Overleaf `master` sincronizados en `dea7267` |
| Estilo QF2 | aplicado solo a tema01 |

## Next Steps

1. Las 5 mejoras 🔵 de tema01: Stefan-Boltzmann, límite Planck→Rayleigh-Jeans,
   potencial de frenado, condición de Bragg, tabla-resumen. Dos de ellas cambian
   el reparto del margen: si la p. 1 se reordena, Rayleigh podría volver.
2. Arreglar los 4 documentos que no compilan (tema04, tema06, math01, math02).
3. Propagar las convenciones de estilo de tema01 a los temas 02-10.
4. Revisar temas 2 y 3 según `REVIEW_PLAN.md`.

## Key Files

- `REVIEW_PLAN.md` — plan de revisión tema por tema, con severidades
- `tema01.tex` — terminado; macro `\retrato` y notas de LaTeX en el preámbulo
- `figs/retratos/CREDITOS.md` — procedencia y licencia de los retratos
- `notebooks/nb01_antecedentes.ipynb` — genera las 5 figuras de tema01
- `Makefile` — `make`, `make figuras`, `make comprobar`
