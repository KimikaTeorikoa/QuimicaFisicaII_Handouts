# Figuras de Química Física II

Scripts de matplotlib que generan todas las figuras de los apuntes en
`../figs/`, en PDF vectorial (para LaTeX) y PNG (para inspección rápida).

## Uso

```bash
cd notebooks
python fig_tema03.py          # un capítulo
make -C .. figuras            # todos
```

Requiere `numpy`, `scipy` y `matplotlib`. En este equipo el intérprete con la
pila científica es `~/opt/anaconda3/bin/python3` (el `python3` de Homebrew no
tiene scipy).

## Estructura

| Script | Figuras | Tema |
|---|---|---|
| `fig_tema01.py` | 5 | Antecedentes |
| `fig_tema02.py` | 3 | Postulados |
| `fig_tema03.py` | 7 | Sistemas modelo |
| `fig_tema04.py` | 4 | Momento angular |
| `fig_tema05.py` | 5 | Átomo de hidrógeno |
| `fig_tema06.py` | 4 | Métodos aproximados |
| `fig_tema07.py` | 5 | Átomos polielectrónicos |
| `fig_tema09.py` | 4 | Moléculas diatómicas |
| `fig_tema10.py` | 4 | Moléculas poliatómicas |
| `fig_practica_ir.py` | 3 | Práctica de IR |

`qf2figs.py` es el módulo común: estilo, paleta, anchuras y `save()`.

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

- `fig_tema05.py` → `r_max(1s)=1.00 a₀`, `r_max(2s)=5.24 a₀`, `⟨r⟩(1s)=1.50 a₀`
- `fig_tema06.py` → variacional del oscilador 13.6 % por encima de la exacta
- `fig_tema10.py` → Hückel butadieno `±1.618, ±0.618`; benceno `2,1,1,−1,−1,−2`;
  deslocalización `0.472β` y `2β`; ángulo tetraédrico `109.47°`
- `fig_practica_ir.py` → el método de diferencias entre combinaciones recupera
  `B₀` y `B₁` exactamente

Si alguno de estos números cambia, es que se ha roto algo.
