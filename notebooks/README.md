# Figuras de Química Física II

Scripts de matplotlib que generan todas las figuras de los apuntes en
`../figs/`, en PDF vectorial (para LaTeX) y PNG (para inspección rápida).

## Uso

```bash
python run_notebooks.py                        # todos los cuadernos
python run_notebooks.py nb03_sistemas_modelo.ipynb   # uno solo
make -C .. figuras                             # equivalente al primero
```

`run_notebooks.py` ejecuta los cuadernos **en memoria**: el `.ipynb` del disco
no se toca, de modo que en el repositorio nunca quedan salidas guardadas.
Reenvía a la terminal lo que imprimen las celdas y aborta si alguna falla.

Requiere `numpy`, `scipy` y `matplotlib`. En este equipo el intérprete con la
pila científica es `~/opt/anaconda3/bin/python3` (el `python3` de Homebrew no
tiene scipy).

## Estructura

| Cuaderno | Figuras | Tema |
|---|---|---|
| `nb01_antecedentes.ipynb` | 5 | Antecedentes |
| `nb02_postulados.ipynb` | 3 | Postulados |
| `nb03_sistemas_modelo.ipynb` | 7 | Sistemas modelo |
| `nb04_momento_angular.ipynb` | 4 | Momento angular |
| `nb05_hidrogeno.ipynb` | 5 | Átomo de hidrógeno |
| `nb06_metodos_aproximados.ipynb` | 4 | Métodos aproximados |
| `nb07_polielectronicos.ipynb` | 5 | Átomos polielectrónicos |
| `nb09_diatomicas.ipynb` | 4 | Moléculas diatómicas |
| `nb10_poliatomicas.ipynb` | 4 | Moléculas poliatómicas |
| `nbP1_practica_ir.ipynb` | 3 | Práctica de IR |

Cada cuaderno tiene **una celda por figura**, precedida de una celda de texto
con su título, más una celda inicial de importaciones y constantes.

`qf2figs.py` es el módulo común: estilo, paleta, anchuras y `save()`. Se deja
como `.py` porque se importa desde todos los cuadernos.
`run_notebooks.py` es el ejecutor sin cabeza que usa `make figuras`.

## Convenio de nombres

```
<sistema>_<observable>[_<variante>]_v<N>.pdf
```

`v<N>` se incrementa cuando cambian los datos o el análisis, no en cada
retoque estético. El número de versión se pasa a `qf.save(..., v=2)`.

## Anchuras

Las tres constantes de `qf2figs` están calibradas para `tufte-handout`:

| Constante | Pulgadas | Entorno LaTeX |
|---|---|---|
| `qf.MARGIN` | 2.0 | `marginfigure` |
| `qf.TEXT` | 4.2 | `figure` |
| `qf.FULL` | 6.4 | `figure*` |

Verificado: los tres entornos compilan con estas figuras.

## Integración en los `.tex`

Añadir al preámbulo (idealmente al `preamble.tex` común):

```latex
\graphicspath{{figs/}{graphics/}}
```

y después, según la anchura con la que se generó la figura:

```latex
\begin{marginfigure}
  \includegraphics[width=\linewidth]{zeeman_desdoblamiento_l1_v1.pdf}
  \caption{Desdoblamiento Zeeman de un nivel $l=1$.}
  \label{fig:zeeman}
\end{marginfigure}

\begin{figure}
  \includegraphics[width=\linewidth]{caja1d_psi-psi2_n1-4_v1.pdf}
  \caption{Funciones de onda y densidades de la partícula en una caja.}
  \label{fig:caja1d}
\end{figure}

\begin{figure*}
  \includegraphics[width=\linewidth]{diatomicas_diagrama-om_N2-O2_v1.pdf}
  \caption{Diagramas de OM de N$_2$ y O$_2$.}
  \label{fig:om-2periodo}
\end{figure*}
```

**Ojo:** `tema01`–`tema10` fijan `\setkeys{Gin}{width=\linewidth,
totalheight=\textheight,keepaspectratio}`, que ya impone la anchura; el
`[width=\linewidth]` explícito es redundante pero inofensivo.

## Color

Paleta Okabe-Ito reordenada, pensada para daltonismo y para impresión en
gris. Validada con el validador de la skill `dataviz`: banda de luminosidad,
suelo de croma, separación CVD (peor par adyacente ΔE 9.6 en deuteranopía) y
suelo de visión normal (ΔE 20.0) — todo PASS. Cada curva lleva **etiqueta
directa** en lugar de leyenda, que es lo que salda el aviso de contraste y
además funciona mejor en papel.

## Comprobaciones numéricas

Varios scripts imprimen valores que sirven de test de regresión frente a los
datos de los apuntes:

- `nb05_hidrogeno.ipynb` → `r_max(1s)=1.00 a₀`, `r_max(2s)=5.24 a₀`, `⟨r⟩(1s)=1.50 a₀`
- `nb06_metodos_aproximados.ipynb` → variacional del oscilador 13.6 % por
  encima de la exacta
- `nb10_poliatomicas.ipynb` → Hückel butadieno `±1.618, ±0.618`; benceno
  `2,1,1,−1,−1,−2`; deslocalización `0.472β` y `2β`; ángulo tetraédrico `109.47°`
- `nbP1_practica_ir.ipynb` → el método de diferencias entre combinaciones
  recupera `B₀` y `B₁` exactamente

Si alguno de estos números cambia, es que se ha roto algo.
