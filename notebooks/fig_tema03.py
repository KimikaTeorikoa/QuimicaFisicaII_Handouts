"""Tema 3 — Sistemas modelo: caja, efecto túnel, oscilador armónico."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_hermite
from math import factorial
import qf2figs as qf

# --- 1. Caja 1D: funciones de onda, densidades y escalera de niveles --------
fig, axes = plt.subplots(1, 3, figsize=(qf.FULL, 3.0),
                         gridspec_kw=dict(width_ratios=[1, 1, 0.5]))
L = 1.0
x = np.linspace(0, L, 600)
esc = 0.40
for ax, (func, tit) in zip(
        axes[:2],
        [(lambda n: np.sqrt(2 / L) * np.sin(n * np.pi * x / L), r"$\psi_n(x)$"),
         (lambda n: 2 / L * np.sin(n * np.pi * x / L) ** 2, r"$|\psi_n(x)|^2$")]):
    for n in range(1, 5):
        y = func(n)
        y = y / np.max(np.abs(y)) * esc
        ax.axhline(n, color=qf.MUTED, lw=0.5, ls=":", zorder=0)
        ax.plot(x, y + n, color=qf.PALETTE[n - 1])
        ax.fill_between(x, n, y + n, color=qf.PALETTE[n - 1],
                        alpha=0.16, lw=0)
    ax.axvline(0, color=qf.INK, lw=1.4)
    ax.axvline(L, color=qf.INK, lw=1.4)
    ax.set_xlim(-0.02, L + 0.02)
    ax.set_ylim(0.35, 4.75)
    ax.set_xticks([0, L])
    ax.set_xticklabels(["0", "$L$"])
    ax.set_yticks(range(1, 5))
    ax.set_yticklabels([f"$n={n}$" for n in range(1, 5)])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"$x$")
    ax.set_title(tit, loc="left", fontsize=9)
axes[1].set_yticklabels([])
# escalera de niveles a escala real
ax = axes[2]
for n in range(1, 5):
    ax.hlines(n**2, 0, 1, color=qf.PALETTE[n - 1], lw=1.6)
    ax.text(1.08, n**2, f"$n={n}$", fontsize=7.5, va="center",
            color=qf.PALETTE[n - 1])
ax.annotate("", xy=(0.35, 16), xytext=(0.35, 9),
            arrowprops=dict(arrowstyle="<->", color=qf.MUTED, lw=0.7))
ax.text(0.42, 12.5, r"$\Delta E$ crece", fontsize=7, color=qf.MUTED,
        va="center")
ax.set_xlim(0, 1.9)
ax.set_ylim(0, 18.5)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.set_yticks([1, 4, 9, 16])
ax.set_ylabel(r"$E_n \,/\, (h^2/8mL^2)$", fontsize=8)
ax.set_title("niveles", loc="left", fontsize=9)
fig.suptitle(r"Partícula en una caja: $E_n=n^2h^2/8mL^2$", fontsize=9,
             x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.93))
qf.save(fig, "caja1d", "psi-psi2", "n1-4")

# --- 2. Límite clásico -----------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(qf.FULL, 1.75), sharey=True)
for ax, n in zip(axes, [1, 5, 30]):
    y = 2 / L * np.sin(n * np.pi * x / L) ** 2
    ax.fill_between(x, 0, y, color=qf.PALETTE[0], alpha=0.30, lw=0)
    ax.plot(x, y, color=qf.PALETTE[0], lw=0.9)
    ax.axhline(1 / L, color=qf.ACCENT, lw=1.2, ls="--")
    ax.set_title(f"$n={n}$", fontsize=8, loc="left")
    ax.set_xticks([0, L])
    ax.set_xticklabels(["0", "$L$"])
    ax.set_xlabel(r"$x$", fontsize=8)
axes[0].set_ylabel(r"$|\psi_n|^2$", fontsize=8)
axes[-1].text(0.5, 1 / L + 0.14, "densidad clásica", color=qf.ACCENT,
              fontsize=7.5, ha="center")
fig.suptitle("Principio de correspondencia: al crecer $n$ la densidad "
             "tiende a la uniforme", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.88))
qf.save(fig, "caja1d", "limite-clasico")

# --- 3. Caja 2D: degeneración ----------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(qf.FULL, 1.9))
xx, yy = np.meshgrid(np.linspace(0, 1, 200), np.linspace(0, 1, 200))
for ax, (n1, n2) in zip(axes, [(1, 1), (1, 2), (2, 1), (2, 2)]):
    psi = 2 * np.sin(n1 * np.pi * xx) * np.sin(n2 * np.pi * yy)
    ax.imshow(psi, cmap="RdBu_r", vmin=-2, vmax=2, origin="lower",
              extent=(0, 1, 0, 1))
    ax.set_title(rf"$(n_1,n_2)=({n1},{n2})$" + "\n"
                 rf"$E={n1**2 + n2**2}\,h^2/8mL^2$", fontsize=7.5, loc="left")
    ax.set_xticks([])
    ax.set_yticks([])
for s in axes[1].spines.values():
    s.set(color=qf.ACCENT, lw=1.6, visible=True)
for s in axes[2].spines.values():
    s.set(color=qf.ACCENT, lw=1.6, visible=True)
fig.suptitle(r"Caja 2D cuadrada: los estados $(1,2)$ y $(2,1)$ son "
             r"degenerados", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.86))
qf.save(fig, "caja2d", "degeneracion")

# --- 4. Efecto túnel -------------------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.7)
Lb, V0, E = 1.0, 1.0, 0.35
k = np.sqrt(E) * 6.0
kap = np.sqrt(V0 - E) * 6.0
xI = np.linspace(-1.6, 0, 500)
xII = np.linspace(0, Lb, 300)
xIII = np.linspace(Lb, 2.6, 500)
A = 1.0
psiII = A * np.exp(-kap * xII)
T = psiII[-1]
ax.add_patch(plt.Rectangle((0, 0), Lb, 1.55, color="#ececec", zorder=0))
ax.plot([-1.6, 0, 0, Lb, Lb, 2.6], [0, 0, V0, V0, 0, 0],
        color=qf.INK, lw=1.2)
ax.axhline(E, color=qf.MUTED, lw=0.8, ls="--")
ax.text(-1.55, E + 0.04, "$E$", fontsize=8, color=qf.MUTED)
ax.text(0.5, V0 + 0.05, "$V$", fontsize=8, color=qf.INK, ha="center")
off = 0.35
ax.plot(xI, off + 0.28 * np.cos(k * xI), color=qf.PALETTE[0])
ax.plot(xII, off + 0.28 * psiII, color=qf.PALETTE[1])
ax.plot(xIII, off + 0.28 * T * np.cos(k * (xIII - Lb)), color=qf.PALETTE[2])
for xc, t, col in [(-0.9, "I: incidente + reflejada", qf.PALETTE[0]),
                   (0.5, "II: decaimiento", qf.PALETTE[1]),
                   (1.9, "III: transmitida", qf.PALETTE[2])]:
    ax.text(xc, 1.35, t, fontsize=7, color=col, ha="center")
ax.set_xlim(-1.6, 2.6)
ax.set_ylim(-0.15, 1.6)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.set_xticks([0, Lb])
ax.set_xticklabels(["0", "$L$"])
ax.set_xlabel(r"$x$")
ax.set_title(r"Efecto túnel para $E<V$", loc="left")
qf.save(fig, "tunel", "psi-regiones")

# --- 5. Coeficiente de transmisión ------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.4)
hbar, me, eV = 1.054571817e-34, 9.1093837015e-31, 1.602176634e-19
eps = np.linspace(0.001, 0.999, 500)
V = 5 * eV
for i, (nombre, m, Lb) in enumerate([("electrón, $L=0.5$ nm", me, 0.5e-9),
                                     ("electrón, $L=1.0$ nm", me, 1.0e-9),
                                     ("protón,  $L=0.5$ nm", 1836 * me, 0.5e-9)]):
    kap = np.sqrt(2 * m * V * (1 - eps)) / hbar
    T = 16 * eps * (1 - eps) * np.exp(-2 * kap * Lb)
    ax.semilogy(eps, T, color=qf.PALETTE[i])
    qf.label_line(ax, 0.55, T[int(0.55 * len(eps))] * 2.4, nombre,
                  qf.PALETTE[i], fontsize=7.5)
ax.set_ylim(1e-14, 3)
ax.set_xlim(0, 1)
ax.set_xlabel(r"$\varepsilon = E/V$")
ax.set_ylabel(r"$T$  (escala log)")
ax.set_title(r"Transmisión: $T\simeq16\varepsilon(1-\varepsilon)"
             r"\mathrm{e}^{-2\kappa L}$", loc="left")
qf.save(fig, "tunel", "coef-transmision")

# --- 6. Oscilador armónico --------------------------------------------------
def psi_ho(v, y):
    N = 1 / np.sqrt(2**v * factorial(v) * np.sqrt(np.pi))
    return N * eval_hermite(v, y) * np.exp(-y**2 / 2)


fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 3.2), sharey=True)
y = np.linspace(-5.5, 5.5, 1200)
for ax, (f, tit) in zip(axes, [(lambda v: psi_ho(v, y), r"$\psi_v(y)$"),
                               (lambda v: psi_ho(v, y)**2, r"$|\psi_v(y)|^2$")]):
    ax.plot(y, y**2 / 2, color=qf.INK, lw=1.0)
    for v in range(5):
        Ev = v + 0.5
        f_ = f(v)
        f_ = f_ / np.max(np.abs(f_)) * 0.42
        ax.hlines(Ev, -np.sqrt(2 * Ev), np.sqrt(2 * Ev),
                  color=qf.MUTED, lw=0.5, ls=":")
        ax.plot(y, f_ + Ev, color=qf.PALETTE[v % 6])
        ax.fill_between(y, Ev, f_ + Ev, color=qf.PALETTE[v % 6],
                        alpha=0.16, lw=0)
        # puntos de retorno clásicos
        ax.plot([-np.sqrt(2 * Ev), np.sqrt(2 * Ev)], [Ev, Ev], "|",
                color=qf.ACCENT, ms=6, mew=1.2)
    ax.set_ylim(0, 6.2)
    ax.set_xlim(-5.5, 5.5)
    ax.set_yticks([v + 0.5 for v in range(5)])
    ax.set_yticklabels([f"$v={v}$" for v in range(5)])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"$y=x/\alpha$")
    ax.set_title(tit, loc="left", fontsize=9)
axes[1].set_yticklabels([])
axes[0].set_ylabel(r"$E_v \,/\, \hbar\omega$")
axes[1].text(3.3, 5.5, "| puntos de retorno\n   clásicos", fontsize=7,
             color=qf.ACCENT)
fig.suptitle(r"Oscilador armónico: $E_v=(v+\frac{1}{2})\hbar\omega$, "
             r"niveles equiespaciados", fontsize=9, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.93))
qf.save(fig, "osciladorarmonico", "psi-psi2", "v0-4")

# --- 7. Límite clásico del oscilador ----------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.4)
v = 20
Ev = v + 0.5
yt = np.sqrt(2 * Ev)
y = np.linspace(-yt * 1.18, yt * 1.18, 4000)
dens = psi_ho(v, y) ** 2
ax.plot(y, dens, color=qf.PALETTE[0], lw=0.7)
yc = np.linspace(-yt * 0.9995, yt * 0.9995, 2000)
clas = 1 / (np.pi * np.sqrt(2 * Ev - yc**2))
ax.plot(yc, clas, color=qf.ACCENT, lw=1.4)
ax.text(0, 0.030, r"clásica  $\propto 1/\sqrt{E-V}$", color=qf.ACCENT,
        fontsize=7.5, ha="center")
ax.text(-yt * 0.55, 0.077, f"cuántica, $v={v}$", color=qf.PALETTE[0],
        fontsize=7.5)
ax.axvline(-yt, color=qf.MUTED, lw=0.6, ls=":")
ax.axvline(yt, color=qf.MUTED, lw=0.6, ls=":")
ax.set_ylim(0, 0.10)
ax.set_xlabel(r"$y=x/\alpha$")
ax.set_ylabel("densidad de probabilidad")
ax.set_title("Principio de correspondencia en el oscilador", loc="left")
qf.save(fig, "osciladorarmonico", "limite-clasico", "v20")
