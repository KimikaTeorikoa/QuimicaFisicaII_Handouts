# CHECKPOINT

## Current Goal

Revisar los apuntes de Química Física II tema por tema siguiendo
`REVIEW_PLAN.md`. Temas 1, 2, 4 y 5 terminados; sigue el tema 6.

## Work Done

### Sesión 2026-10-23 — Tema 5

- Cerrados los 5 🔴, los 🟠 y los 🟡 del plan, más los hallazgos nuevos:
  $a_0$ (×10), nodos $n-l-1$, ortogonalidad del espín (=0), «orbitales de
  Mulliken» → orbitales atómicos con nota al margen.
- Decisiones del autor: dipolo magnético $\boldsymbol{\mu}$ (y
  $\mu_z=-\mu_Bm_l$); final de §Zeeman reescrito con el **efecto Zeeman
  anómalo**; $\psi_{1s}$ con $Z$; bloque comentado de orbitales p borrado.
- Pasada de redacción (calcos, redundancias) y cuatro retoques con física:
  componentes de $\mathbf{l}$ que no conmutan, cita de Compton (*ultimate*),
  campo **no homogéneo** en Stern–Gerlach, «En general» fuera. Rechazado
  definir $\mu$: ya está en el tema 4.
- Preámbulo limpio como tema01 (`\graphicspath` con `figs/`, `\@fptop`,
  `\retrato`; fuera `lipsum`, `\doc*`, bibliografía).
- `nb05`: sin títulos, etiquetas recolocadas, $\langle r\rangle$ en la RDF,
  signo de $\psi$ en los cortes 2D (quinto panel 3d$_{xz}$: el 3d$_{xy}$ es
  nulo en el plano $xz$), niveles sólo hasta $n=4$. Las 5 figuras colocadas.
- Retratos de dominio público: Zeeman (1902) y Stern (ETH, h. 1940).
  Bohr descartado (ya en tema01); Gerlach sin retrato utilizable.

## Current State

| Qué | Estado |
|---|---|
| tema05 | terminado, 9 páginas, 0 overfull |
| Compilación global | falla en tema06, math01, math02 (previos) |
| Remotos | `master` 5 commits por delante de `origin/master` (tema 4); el `git fetch` de Overleaf se cuelga |
| Sin commitear | todo el trabajo del tema 5 (tex, nb05, 5 PDF, 2 retratos, créditos, REVIEW_PLAN, este fichero) |

## Next Steps

1. Commitear el tema 5; antes de empujar a `origin`, comprobar si hay
   ediciones en Overleaf (el fetch no responde).
2. Revisar el tema 6 según `REVIEW_PLAN.md` (no compila).
3. 🔵 pendientes del tema 5, opcionales: energía en eV y $\langle r\rangle$ en
   el texto, puntero a orbitales reales del tema 4, espín-órbita, título
   «…del hidrógeno» → «hidrogenoides».
4. Para el futuro: esquema de Stern–Gerlach e isosuperficies 3D
   (`MAPA_CURSO.md` §9, punto 12).

## Key Files

- `CLAUDE.md` — convenciones del repositorio y trampas de maquetación
- `REVIEW_PLAN.md` — plan por temas; sus números de línea son de 2023
- `tema01.tex`, `tema02.tex` — referencia de estilo
- `notebooks/nb05_hidrogeno.ipynb` — genera las 5 figuras del tema 5
- `figs/retratos/CREDITOS.md` — procedencia de los retratos
