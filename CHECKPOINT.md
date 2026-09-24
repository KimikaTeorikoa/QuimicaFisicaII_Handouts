# CHECKPOINT

## Current Goal

Revisar los apuntes de Química Física II tema por tema siguiendo
`REVIEW_PLAN.md`. Temas 1 y 2 terminados; sigue el tema 3.

## Work Done

### Session 2026-09-03 — Tema 2

- Cerrados los 12 hallazgos del plan más 8 no previstos. Uno **rechazado**:
  "proporcional" era correcto, porque ahí $\psi$ todavía no está normalizada.
- Reescrito el postulado de la medida (devolvía el promedio en vez de un
  autovalor) y añadida $\hat{H}\psi=E\psi$, que no aparecía en todo el tema.
- Fijado el convenio de normalización: $N$ se mantiene y ahora se despeja.
- Pauli metido en `theorem` y condensado; los postulados ya numeran 1--6.
- Cuatro figuras colocadas y citadas. `postulados_psi-psi2` es nueva;
  `incertidumbre_x-k` pasa a `x-p` porque $k$ no se define en ningún tema.
- Tres retratos de dominio público: Born, Schrödinger y Pauli.
- Pasada de redacción sobre todo el capítulo (14 cambios).
- Escrito `CLAUDE.md` con las convenciones del repositorio.
- Todo commiteado y empujado a github y Overleaf (`4d00f58`).

## Current State

| Qué | Estado |
|---|---|
| tema01, tema02 | terminados, 8 páginas, 0 overfull |
| Compilación global | falla en tema04, tema06, math01, math02 |
| Remotos | `github/main` y `origin/master` en `4d00f58` |
| Figuras | 45 generadas; sólo las usan tema01 y tema02 |
| Sin commitear | esta actualización de CHECKPOINT.md y CLAUDE.md |

## Next Steps

1. Revisar el tema 3 según `REVIEW_PLAN.md`.
2. Arreglar los 4 documentos que no compilan.
3. Colocar las figuras en los temas 03--10; cada uno necesita además `figs/`
   en su `\graphicspath`, que hoy apunta sólo a `graphics/`.
4. Preámbulo común `qf2.sty` y limpieza de los restos de plantilla Tufte
   (`lipsum`, `\doccmd`...), pendientes en los 13 ficheros.
5. Pendiente de tema02: ejemplo resuelto de normalización y notación de Dirac
   con referencia cruzada a `math01`.

## Key Files

- `CLAUDE.md` — convenciones del repositorio y trampas de maquetación
- `REVIEW_PLAN.md` — plan por temas; sus números de línea son de 2023
- `tema01.tex`, `tema02.tex` — terminados, referencia de estilo
- `notebooks/nb02_postulados.ipynb` — genera las 4 figuras de tema02
- `Makefile` — `make`, `make figuras`, `make comprobar`
