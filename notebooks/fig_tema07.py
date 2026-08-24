"""Tema 7 — Átomos polielectrónicos: hueco de Fermi, apantallamiento, SCF."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

# --- 1. Hueco de Fermi: |Psi_s|^2 y |Psi_a|^2 en (x1, x2) -------------------
# Arregla el párrafo autocontradictorio de tema07.tex (líneas 354-363)
fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 2.7))
L = 1.0
n = 300
x1, x2 = np.meshgrid(np.linspace(0, L, n), np.linspace(0, L, n))


def phi(k, x):
    return np.sqrt(2 / L) * np.sin(k * np.pi * x / L)


a1, b2 = phi(1, x1), phi(2, x2)
a2, b1 = phi(1, x2), phi(2, x1)
Ps = (a1 * b2 + a2 * b1) / np.sqrt(2)
Pa = (a1 * b2 - a2 * b1) / np.sqrt(2)
for ax, P, tit, sub in [
        (axes[0], Ps**2, r"$|\Psi_s|^2$  (espacial simétrica)",
         r"espines opuestos · singlete · $J+K$"),
        (axes[1], Pa**2, r"$|\Psi_a|^2$  (espacial antisimétrica)",
         r"mismo espín · triplete · $J-K$")]:
    im = ax.pcolormesh(x1, x2, P, cmap="Blues", shading="auto",
                       rasterized=True, vmin=0, vmax=max(Ps.max()**2,
                                                         Pa.max()**2))
    ax.plot([0, L], [0, L], color=qf.ACCENT, lw=1.0, ls="--")
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(tit + "\n" + sub, fontsize=8.5, loc="left")
    ax.set_aspect("equal")
axes[1].annotate("hueco de Fermi:\n$\\Psi_a=0$ en $x_1=x_2$",
                 xy=(0.62, 0.62), xytext=(0.30, 0.86),
                 fontsize=7, color=qf.ACCENT,
                 arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
axes[0].annotate("densidad acumulada\nen $x_1=x_2$", xy=(0.35, 0.35),
                 xytext=(0.52, 0.10), fontsize=7, color=qf.ACCENT,
                 arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
fig.suptitle("Los electrones de igual espín se evitan: por eso el triplete "
             "es más estable", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0.04, 1, 0.92))
qf.save(fig, "polielectronicos", "hueco-fermi")

# --- 2. Singlete / triplete: separación 2K ---------------------------------
fig, ax = qf.figure(qf.MARGIN, 2.0)
J, K = 1.0, 0.28
ax.hlines(0, 0, 0.8, color=qf.MUTED, lw=1.4)
ax.text(0.4, -0.13, "sin $1/r_{12}$", fontsize=6.5, ha="center",
        color=qf.MUTED)
ax.hlines(J + K, 1.2, 2.0, color=qf.PALETTE[1], lw=1.6)
ax.hlines(J - K, 1.2, 2.0, color=qf.PALETTE[2], lw=1.6)
ax.text(2.08, J + K, r"$^1S$  $J+K$", fontsize=7, va="center",
        color=qf.PALETTE[1])
ax.text(2.08, J - K, r"$^3S$  $J-K$", fontsize=7, va="center",
        color=qf.PALETTE[2])
ax.plot([0.8, 1.2], [0, J + K], color=qf.MUTED, lw=0.5, ls=":")
ax.plot([0.8, 1.2], [0, J - K], color=qf.MUTED, lw=0.5, ls=":")
ax.annotate("", xy=(1.1, J + K), xytext=(1.1, J - K),
            arrowprops=dict(arrowstyle="<->", color=qf.ACCENT, lw=0.8))
ax.text(0.96, J, r"$2K$", fontsize=7, color=qf.ACCENT, ha="right",
        va="center")
ax.set_xlim(0, 3.4)
ax.set_ylim(-0.3, 1.6)
ax.set_xticks([])
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_title("Singlete/triplete del He", loc="left", fontsize=8)
qf.save(fig, "helio", "singlete-triplete")

# --- 3. Energías de ionización: penetración y apantallamiento --------------
fig, ax = qf.figure(qf.TEXT, 2.6)
Z = np.arange(1, 21)
EI = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423,
      21.565, 5.139, 7.646, 5.986, 8.152, 10.487, 10.360, 12.968, 15.760,
      4.341, 6.113]
simb = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg",
        "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca"]
ax.plot(Z, EI, "-o", color=qf.PALETTE[0], ms=3.5, lw=1.0)
for z, e, s in zip(Z, EI, simb):
    if s in ("He", "Ne", "Ar", "Li", "Na", "K", "Be", "B", "N", "O"):
        dy = 1.1 if s in ("He", "Ne", "Ar", "Be", "N") else -1.6
        ax.text(z, e + dy, s, fontsize=6.5, ha="center",
                color=qf.ACCENT if s in ("B", "O") else qf.INK)
for z0, z1, txt in [(4, 5, r"Be$\to$B: se abre el $2p$"),
                    (7, 8, r"N$\to$O: apareamiento en $2p$")]:
    ax.annotate("", xy=(z1, EI[z1 - 1]), xytext=(z0, EI[z0 - 1]),
                arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=1.0))
ax.text(10.4, 3.6, r"anomalías (naranja): Be$\to$B abre el $2p$;"
                   "\n" r"N$\to$O fuerza el apareamiento de espines",
        fontsize=6.8, color=qf.ACCENT)
ax.set_xticks([1, 5, 10, 15, 20])
ax.set_xlabel(r"$Z$")
ax.set_ylabel("1.ª energía de ionización / eV")
ax.set_ylim(2, 27)
ax.set_title("Periodicidad: penetración, apantallamiento y Hund", loc="left")
qf.save(fig, "polielectronicos", "energia-ionizacion")

# --- 4. Hidrogenoide vs polielectrónico: ruptura de la degeneración --------
fig, axes = plt.subplots(1, 2, figsize=(qf.TEXT, 2.4), sharey=True)
for ax, (tit, desplaza) in zip(
        axes, [("hidrogenoide: $E=E(n)$", False),
               ("polielectrónico: $E=E(n,l)$", True)]):
    for n in range(1, 4):
        for l in range(n):
            E = -13.6 / n**2
            if desplaza:
                E += 2.6 * l / n**1.2          # penetración: s < p < d
            ax.hlines(E, l * 1.05, l * 1.05 + 0.85,
                      color=qf.PALETTE[l % 6], lw=1.5)
    for l, nom in enumerate("spd"):
        ax.text(l * 1.05 + 0.42, 1.2, nom, fontsize=8.5, ha="center",
                color=qf.PALETTE[l % 6])
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-14.5, 2.4)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_title(tit, fontsize=8, loc="left")
axes[0].set_ylabel(r"$E$ / eV")
fig.tight_layout()
qf.save(fig, "polielectronicos", "ruptura-degeneracion")

# --- 5. Ciclo SCF de Hartree-Fock ------------------------------------------
fig, ax = qf.figure(qf.MARGIN, 2.6)
pasos = ["orbitales\nde prueba", r"construir $\hat{V}^{\rm eff}$",
         "resolver\necuaciones de Fock", "nuevos\norbitales"]
ys = [3.1, 2.2, 1.3, 0.4]
for y, t in zip(ys, pasos):
    ax.add_patch(plt.Rectangle((0.1, y - 0.16), 1.8, 0.42, fc="#eef4fa",
                               ec=qf.PALETTE[0], lw=0.8))
    ax.text(1.0, y + 0.05, t, fontsize=6.5, ha="center", va="center")
for y0, y1 in zip(ys[:-1], ys[1:]):
    ax.annotate("", xy=(1.0, y1 + 0.27), xytext=(1.0, y0 - 0.17),
                arrowprops=dict(arrowstyle="->", color=qf.PALETTE[0], lw=0.9))
ax.annotate("", xy=(1.9, 3.0), xytext=(2.25, 0.45),
            arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.9,
                            connectionstyle="arc3,rad=-0.55"))
ax.text(2.42, 1.75, "¿autoconsistente?\nno: repetir", fontsize=6,
        color=qf.ACCENT, rotation=90, ha="center", va="center")
ax.set_xlim(0, 3.1)
ax.set_ylim(0.05, 3.75)
ax.axis("off")
ax.set_title("Ciclo SCF", loc="left", fontsize=8)
qf.save(fig, "hartreefock", "ciclo-scf")
