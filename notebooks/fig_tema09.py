"""Tema 9 — Moléculas diatómicas: curva de Morse, OM del H2+, diagramas."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

# --- 1. Curva de energía potencial: De, D0 y punto cero --------------------
fig, ax = qf.figure(qf.TEXT, 2.7)
De, beta, Re = 4.75, 1.94, 0.741
R = np.linspace(0.35, 3.2, 800)
V = De * (1 - np.exp(-beta * (R - Re)))**2 - De
ax.plot(R, V, color=qf.PALETTE[0])
we = 0.546          # hbar*omega en eV para H2
ax.hlines(-De + we / 2, 0.52, 1.15, color=qf.ACCENT, lw=1.4)
ax.text(1.19, -De + we / 2, r"$v=0$ (punto cero)", fontsize=7,
        color=qf.ACCENT, va="center")
for v in range(1, 5):
    Ev = -De + we * (v + 0.5) - 0.03 * we * (v + 0.5)**2
    lo = Re - np.log(1 + np.sqrt((Ev + De) / De)) / beta
    hi = Re - np.log(1 - np.sqrt((Ev + De) / De)) / beta
    ax.hlines(Ev, lo, hi, color=qf.MUTED, lw=0.7)
ax.axhline(0, color=qf.MUTED, lw=0.7, ls=":")
ax.text(3.15, 0.12, "átomos separados", fontsize=7, ha="right",
        color=qf.MUTED)
ax.annotate("", xy=(2.45, 0), xytext=(2.45, -De),
            arrowprops=dict(arrowstyle="<->", color=qf.PALETTE[1], lw=0.9))
ax.text(2.52, -De / 2, r"$D_e$", fontsize=8.5, color=qf.PALETTE[1],
        va="center")
ax.annotate("", xy=(2.85, 0), xytext=(2.85, -De + we / 2),
            arrowprops=dict(arrowstyle="<->", color=qf.PALETTE[2], lw=0.9))
ax.text(2.92, (-De + we / 2) / 2, r"$D_0$", fontsize=8.5,
        color=qf.PALETTE[2], va="center")
ax.plot(Re, -De, "o", color=qf.PALETTE[0], ms=4)
ax.annotate(r"$R_e$", xy=(Re, -De), xytext=(Re, -De - 0.55), fontsize=8.5,
            ha="center", color=qf.PALETTE[0])
ax.set_xlim(0.35, 3.2)
ax.set_ylim(-De - 0.9, 1.5)
ax.set_xlabel(r"$R$ / Å")
ax.set_ylabel(r"$V(R)$ / eV")
ax.set_title(r"Curva de energía potencial (H$_2$): $D_0=D_e-\frac{1}{2}"
             r"\hbar\omega$", loc="left", fontsize=8.5)
qf.save(fig, "h2", "curva-potencial", "De-D0")

# --- 2. OM del H2+: sigma_g y sigma_u --------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(qf.FULL, 3.2), sharex=True)
x = np.linspace(-4.5, 4.5, 1200)
d = 1.3


def s1(x, c):
    return np.exp(-np.abs(x - c))


A, B = s1(x, -d), s1(x, d)
S = np.trapz(A * B, x)
sg = (A + B) / np.sqrt(2 * (1 + S))
su = (A - B) / np.sqrt(2 * (1 - S))
for j, (psi, nombre, col) in enumerate(
        [(sg, r"$\sigma_g=1\sigma$  (enlazante)", qf.PALETTE[0]),
         (su, r"$\sigma_u=2\sigma^\star$  (antienlazante)", qf.PALETTE[1])]):
    ax = axes[0, j]
    ax.plot(x, A / np.sqrt(2 * (1 + S)) * (1 if j == 0 else 1),
            color=qf.MUTED, lw=0.7, ls="--")
    ax.plot(x, (B if j == 0 else -B) / np.sqrt(2 * (1 + S)),
            color=qf.MUTED, lw=0.7, ls="--")
    ax.plot(x, psi, color=col)
    ax.axhline(0, color=qf.MUTED, lw=0.5)
    ax.set_title(nombre, fontsize=8.5, loc="left", color=col)
    ax.set_ylabel(r"$\psi$", fontsize=8)
    ax2 = axes[1, j]
    ax2.plot(x, psi**2, color=col)
    ax2.fill_between(x, 0, psi**2, color=col, alpha=0.2, lw=0)
    ax2.axhline(0, color=qf.MUTED, lw=0.5)
    ax2.set_ylabel(r"$|\psi|^2$", fontsize=8)
    ax2.set_xlabel(r"$x$ (eje internuclear)", fontsize=8)
    for a in (ax, ax2):
        a.plot([-d, d], [0, 0], "o", color=qf.INK, ms=4, zorder=6)
        a.set_xlim(-4.5, 4.5)
axes[1, 1].axvline(0, color=qf.ACCENT, lw=1.0, ls=":")
axes[1, 1].text(0.15, 0.30, "plano nodal", fontsize=7, color=qf.ACCENT,
                rotation=90, va="top")
axes[1, 0].annotate("densidad acumulada\nentre los núcleos", xy=(0, 0.16),
                    xytext=(1.1, 0.33), fontsize=7, color=qf.ACCENT,
                    arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
fig.suptitle(r"Orbitales moleculares del H$_2^+$ por combinación lineal "
             r"de 1s$_A$ y 1s$_B$", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.93))
qf.save(fig, "h2mas", "om-sigma-g-u")

# --- 3. E(R) de los orbitales enlazante y antienlazante --------------------
fig, ax = qf.figure(qf.TEXT, 2.5)
Rr = np.linspace(0.5, 8, 600)
S_ = np.exp(-Rr) * (1 + Rr + Rr**2 / 3)
j_ = (1 / Rr) - np.exp(-2 * Rr) * (1 + 1 / Rr)
k_ = np.exp(-Rr) * (1 + Rr)
E1 = 1 / Rr - (j_ + k_) / (1 + S_)
E2 = 1 / Rr - (j_ - k_) / (1 - S_)
ax.plot(Rr, E1 * 27.211, color=qf.PALETTE[0])
ax.plot(Rr, E2 * 27.211, color=qf.PALETTE[1])
ax.axhline(0, color=qf.MUTED, lw=0.7, ls=":")
ax.text(7.9, 0.5, r"$E_{\rm H1s}$", fontsize=7.5, ha="right", color=qf.MUTED)
qf.label_line(ax, 4.2, E1[280] * 27.211 - 1.6, r"$1\sigma_g$ enlazante",
              qf.PALETTE[0], fontsize=7.5)
qf.label_line(ax, 4.2, E2[280] * 27.211 + 1.2, r"$2\sigma_u^\star$ antienlazante",
              qf.PALETTE[1], fontsize=7.5)
imin = np.argmin(E1)
ax.plot(Rr[imin], E1[imin] * 27.211, "o", color=qf.PALETTE[0], ms=4)
ax.annotate("", xy=(2.6, 0), xytext=(2.6, E2[np.argmin(np.abs(Rr - 2.6))] * 27.211),
            arrowprops=dict(arrowstyle="<->", color=qf.ACCENT, lw=0.8))
ax.annotate("", xy=(2.2, 0), xytext=(2.2, E1[np.argmin(np.abs(Rr - 2.2))] * 27.211),
            arrowprops=dict(arrowstyle="<->", color=qf.ACCENT, lw=0.8))
ax.text(3.0, 4.0, "el antienlazante sube\nmás de lo que baja\nel enlazante",
        fontsize=7, color=qf.ACCENT)
ax.set_xlim(0.5, 8)
ax.set_ylim(-8, 14)
ax.set_xlabel(r"$R$ / $a_0$")
ax.set_ylabel(r"$E-E_{\rm H1s}$ / eV")
ax.set_title(r"H$_2^+$: asimetría enlazante/antienlazante", loc="left",
             fontsize=8.5)
qf.save(fig, "h2mas", "energia-R")

# --- 4. Diagrama de OM del 2º periodo, con inversión s-p -------------------
fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 3.3), sharey=True)
niveles_N2 = [(r"$1\sigma_g$", -1.8, 2), (r"$1\sigma_u^\star$", -0.9, 2),
              (r"$1\pi_u$", 0.35, 4), (r"$2\sigma_g$", 0.75, 2),
              (r"$1\pi_g^\star$", 1.8, 0), (r"$2\sigma_u^\star$", 2.6, 0)]
niveles_O2 = [(r"$1\sigma_g$", -1.8, 2), (r"$1\sigma_u^\star$", -0.9, 2),
              (r"$2\sigma_g$", 0.30, 2), (r"$1\pi_u$", 0.80, 4),
              (r"$1\pi_g^\star$", 1.8, 2), (r"$2\sigma_u^\star$", 2.6, 0)]
def dibuja_electrones(ax, E, centros, occ):
    """Reparte `occ` electrones entre orbitales degenerados según Hund:
    primero uno por orbital con espines paralelos, luego se aparean."""
    k = len(centros)
    sencillos = min(occ, k)
    dobles = occ - sencillos
    for i, xc in enumerate(centros):
        if i < sencillos:
            if i < dobles:            # orbital doblemente ocupado
                ax.plot(xc - 0.075, E, marker=r"$\uparrow$", color=qf.INK,
                        ms=7, linestyle="none")
                ax.plot(xc + 0.075, E, marker=r"$\downarrow$", color=qf.INK,
                        ms=7, linestyle="none")
            else:                      # un solo electrón, espín arriba
                ax.plot(xc, E, marker=r"$\uparrow$", color=qf.INK, ms=7,
                        linestyle="none")


for ax, (niveles, tit, ne) in zip(
        axes, [(niveles_N2, r"N$_2$  ($1\pi_u$ por debajo de $2\sigma_g$)", 10),
               (niveles_O2, r"O$_2$  ($2\sigma_g$ por debajo de $1\pi_u$)", 12)]):
    for nombre, E, occ in niveles:
        es_pi = r"\pi" in nombre
        col = qf.PALETTE[1] if "star" in nombre else qf.PALETTE[0]
        centros = [-0.45, 0.45] if es_pi else [0.0]
        for xc in centros:
            ax.hlines(E, xc - 0.28, xc + 0.28, color=col, lw=1.6)
        dibuja_electrones(ax, E, centros, occ)
        ax.text(0.90, E, nombre, fontsize=7.5, va="center", color=col)
    ax.set_xlim(-1.0, 1.9)
    ax.set_ylim(-2.3, 4.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_title(tit, fontsize=8.5, loc="left")
axes[0].set_ylabel("energía (esquemática)")
axes[1].annotate("2 electrones desapareados\ncon espines paralelos (Hund):\n"
                 r"O$_2$ es paramagnético",
                 xy=(0.45, 1.90), xytext=(-0.95, 3.45), fontsize=6.8,
                 color=qf.ACCENT, va="top",
                 arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
fig.suptitle(r"Inversión $s$–$p$: orden de enlace $b=\frac{1}{2}(n-n^\star)=3$ "
             r"en N$_2$ y $2$ en O$_2$", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.92))
qf.save(fig, "diatomicas", "diagrama-om", "N2-O2")
