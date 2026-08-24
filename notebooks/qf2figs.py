"""
Estilo común para las figuras de Química Física II.

Uso:
    import qf2figs as qf
    fig, ax = qf.figure(qf.TEXT)
    ...
    qf.save(fig, "caja1d", "psi2", "n1-4", v=1)

Convenio de nombres:  <sistema>_<observable>[_<variante>]_v<N>.pdf
Las figuras se guardan en ../figs/ en PDF vectorial.
"""
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

FIGDIR = Path(__file__).resolve().parent.parent / "figs"

# Anchuras de la clase tufte-handout (pulgadas)
TEXT = 4.2     # \textwidth
MARGIN = 2.0   # \marginparwidth  -> entorno marginfigure
FULL = 6.4     # \textwidth + margen -> entorno figure*

# Paleta Okabe-Ito reordenada. Validada con el validador de la skill dataviz:
# banda de luminosidad, suelo de croma, separación CVD (peor par adyacente
# ΔE 9.6 deutan) y suelo de visión normal (ΔE 20.0) -> PASS.
# El aviso de contraste se salda etiquetando cada curva directamente.
PALETTE = ["#0072B2", "#D55E00", "#009E73", "#E69F00", "#CC79A7", "#56B4E9"]

INK = "#1a1a1a"      # texto principal
MUTED = "#8a8a8a"    # ejes, rejilla, líneas de construcción
ACCENT = "#D55E00"   # resaltados puntuales
FILL_POS = "#0072B2"
FILL_NEG = "#D55E00"


def set_style():
    mpl.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Palatino", "Palatino Linotype", "URW Palladio L",
                       "DejaVu Serif"],
        "mathtext.fontset": "dejavuserif",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
        "axes.linewidth": 0.6,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "axes.prop_cycle": mpl.cycler(color=PALETTE),
        "axes.spines.top": False,
        "axes.spines.right": False,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelcolor": INK,
        "ytick.labelcolor": INK,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "lines.linewidth": 1.4,
        "lines.markersize": 4,
        "grid.color": "#e2e2e2",
        "grid.linewidth": 0.5,
        "legend.frameon": False,
        "figure.dpi": 140,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
    })


def figure(width=TEXT, height=None, **kw):
    """Crea una figura del ancho adecuado para la clase tufte-handout."""
    if height is None:
        height = width * 0.62          # proporción áurea aproximada
    return plt.subplots(figsize=(width, height), **kw)


def save(fig, sistema, observable, variante=None, v=1, close=True):
    """Guarda siguiendo el convenio <sistema>_<observable>[_<variante>]_v<N>.pdf"""
    FIGDIR.mkdir(exist_ok=True)
    partes = [sistema, observable] + ([variante] if variante else []) + [f"v{v}"]
    nombre = "_".join(partes) + ".pdf"
    fig.savefig(FIGDIR / nombre)
    fig.savefig(FIGDIR / nombre.replace(".pdf", ".png"), dpi=200)
    if close:
        plt.close(fig)
    print(f"  -> figs/{nombre}")
    return FIGDIR / nombre


def label_line(ax, x, y, text, color, dx=0.0, dy=0.0, **kw):
    """Etiqueta directa sobre una curva (sustituye a la leyenda)."""
    kw.setdefault("fontsize", 8)
    kw.setdefault("ha", "left")
    kw.setdefault("va", "center")
    return ax.text(x + dx, y + dy, text, color=color, **kw)


def zero_axis(ax, y=0.0, xmin=None, xmax=None):
    """Línea de cero discreta."""
    ax.axhline(y, color=MUTED, lw=0.6, zorder=0,
               xmin=0 if xmin is None else xmin,
               xmax=1 if xmax is None else xmax)


set_style()
