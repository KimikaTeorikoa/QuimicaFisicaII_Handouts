"""Tema 6 — Métodos aproximados: variacional y perturbativo."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

# --- 1. Variacional simple: oscilador armónico con psi = cos(lambda x) ------
# (recupera el ejemplo que está comentado en tema06.tex, líneas 135-181)
fig, ax = qf.figure(qf.TEXT, 2.4)
lam = np.linspace(0.35, 2.2, 500)
# E(lambda) = lambda^2/2 + (1/lambda^2)(pi^2/24 - 1/4)   en unidades hbar=m=k=1
E = lam**2 / 2 + (np.pi**2 / 24 - 0.25) / lam**2
ax.plot(lam, E, color=qf.PALETTE[0])
imin = np.argmin(E)
ax.plot(lam[imin], E[imin], "o", color=qf.PALETTE[0], ms=5, zorder=5)
ax.axhline(0.5, color=qf.ACCENT, lw=1.2, ls="--")
ax.text(2.05, 0.535, r"exacta  $E_0=\frac{1}{2}\hbar\omega$", color=qf.ACCENT,
        fontsize=7.5, ha="right")
ax.annotate(rf"$E_{{\min}}={E[imin]:.3f}\,\hbar\omega$"
            f"\n(+{100*(E[imin]/0.5-1):.0f}\\%)",
            xy=(lam[imin], E[imin]), xytext=(lam[imin] + 0.32, E[imin] + 0.12),
            fontsize=7.5, color=qf.PALETTE[0],
            arrowprops=dict(arrowstyle="->", color=qf.PALETTE[0], lw=0.7))
ax.set_xlim(0.35, 2.2)
ax.set_ylim(0.45, 1.3)
ax.set_xlabel(r"$\lambda$ (parámetro variacional)")
ax.set_ylabel(r"$E(\lambda)\,/\,\hbar\omega$")
ax.set_title(r"Variacional simple: $E(\lambda)\geq E_0$ siempre", loc="left")
print(f"    E_min = {E[imin]:.4f} hbar-omega  (exacta 0.5) -> "
      f"{100*(E[imin]/0.5-1):.1f} % por encima")
qf.save(fig, "variacional", "oscilador", "E-lambda")

# --- 2. Helio: E(zeta) y apantallamiento -----------------------------------
fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 2.5))
z = np.linspace(1.0, 2.4, 400)
Ez = z**2 - (27 / 8) * z          # en hartree
ax = axes[0]
ax.plot(z, Ez, color=qf.PALETTE[0])
zopt = 27 / 16
ax.plot(zopt, zopt**2 - 27 / 8 * zopt, "o", color=qf.PALETTE[0], ms=5,
        zorder=5)
ax.axhline(-2.9033, color=qf.ACCENT, lw=1.2, ls="--")
ax.text(2.38, -2.87, "experimental", color=qf.ACCENT, fontsize=7.5,
        ha="right")
ax.axvline(2, color=qf.MUTED, lw=0.8, ls=":")
ax.text(2.03, -2.0, r"$Z=2$ (sin apantallar)", fontsize=7, color=qf.MUTED,
        rotation=90, va="top")
ax.annotate(rf"$\zeta_{{opt}}=27/16={zopt:.4f}$" "\n"
            rf"$E=-2.848\,E_h$",
            xy=(zopt, zopt**2 - 27 / 8 * zopt),
            xytext=(1.05, -2.55), fontsize=7.5, color=qf.PALETTE[0],
            arrowprops=dict(arrowstyle="->", color=qf.PALETTE[0], lw=0.7))
ax.set_xlabel(r"$\zeta$")
ax.set_ylabel(r"$E(\zeta)$ / $E_h$")
ax.set_title(r"He: $E(\zeta)=\zeta^2-\frac{27}{8}\zeta$", loc="left",
             fontsize=8.5)

ax = axes[1]
r = np.linspace(0, 5, 400)
for i, (zz, et) in enumerate([(1.0, r"$\zeta=1$ (H)"),
                              (zopt, r"$\zeta=1.69$ (óptimo)"),
                              (2.0, r"$\zeta=2$ (sin apantallar)")]):
    P = r**2 * (zz**3 / np.pi) * np.exp(-2 * zz * r) * 4 * np.pi
    ax.plot(r, P, color=qf.PALETTE[i])
    qf.label_line(ax, r[np.argmax(P)] + 0.15, P.max(), et, qf.PALETTE[i],
                  fontsize=7)
ax.set_xlabel(r"$r/a_0$")
ax.set_ylabel(r"$P(r)$")
ax.set_title("El apantallamiento expande el orbital", loc="left",
             fontsize=8.5)
fig.tight_layout()
qf.save(fig, "helio", "variacional-zeta")

# --- 3. Comparación de métodos ---------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.3)
metodos = ["Ignorando\n$1/r_{12}$", "Perturb.\n1er orden", "Variacional",
           "Perturb.\n2º orden", "Experimento"]
vals = [-4.0000, -2.7500, -2.8477, -2.9077, -2.9033]
cols = [qf.PALETTE[1], qf.PALETTE[3], qf.PALETTE[0], qf.PALETTE[2], qf.INK]
ypos = np.arange(len(metodos))[::-1]
ax.barh(ypos, vals, color=cols, height=0.55)
ax.axvline(-2.9033, color=qf.ACCENT, lw=1.0, ls="--", zorder=3)
for y, v in zip(ypos, vals):
    ax.text(v - 0.05, y, f"{v:.4f}", va="center", ha="right", fontsize=7.5,
            color="white" if v < -2.6 else qf.INK)
ax.set_yticks(ypos)
ax.set_yticklabels(metodos, fontsize=7.5)
ax.set_xlim(-4.25, 0)
ax.set_xlabel(r"$E$ / $E_h$")
ax.set_title("Energía del estado fundamental del He", loc="left")
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
qf.save(fig, "helio", "comparacion-metodos")

# --- 4. Sistema de dos niveles: repulsión de niveles -----------------------
fig, ax = qf.figure(qf.TEXT, 2.4)
H12 = np.linspace(0, 2.5, 400)
H11, H22 = -1.0, 1.0
Em = (H11 + H22) / 2 - np.sqrt(((H11 - H22) / 2)**2 + H12**2)
Ep = (H11 + H22) / 2 + np.sqrt(((H11 - H22) / 2)**2 + H12**2)
ax.plot(H12, Ep, color=qf.PALETTE[1])
ax.plot(H12, Em, color=qf.PALETTE[0])
ax.axhline(H11, color=qf.MUTED, lw=0.7, ls=":")
ax.axhline(H22, color=qf.MUTED, lw=0.7, ls=":")
ax.text(2.55, Ep[-1], r"$E_+$ (antienlazante)", fontsize=7.5,
        color=qf.PALETTE[1], va="center")
ax.text(2.55, Em[-1], r"$E_-$ (enlazante)", fontsize=7.5,
        color=qf.PALETTE[0], va="center")
ax.text(0.05, H22 + 0.12, r"$H_{22}$", fontsize=7.5, color=qf.MUTED)
ax.text(0.05, H11 - 0.28, r"$H_{11}$", fontsize=7.5, color=qf.MUTED)
ax.annotate("", xy=(1.5, Ep[240]), xytext=(1.5, Em[240]),
            arrowprops=dict(arrowstyle="<->", color=qf.ACCENT, lw=0.8))
ax.text(1.56, 0, "los niveles\nse repelen", fontsize=7, color=qf.ACCENT,
        va="center")
ax.set_xlim(0, 2.5)
ax.set_xlabel(r"$|H_{12}|$  (acoplamiento)")
ax.set_ylabel(r"$E$")
ax.set_title(r"Determinante secular $2\times2$: la base de los Temas 9 y 10",
             loc="left", fontsize=8.5)
qf.save(fig, "secular", "dos-niveles")
