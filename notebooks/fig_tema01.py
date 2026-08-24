"""Tema 1 — Antecedentes de la Mecánica Cuántica."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

h, c, kB, e = 6.62607015e-34, 2.99792458e8, 1.380649e-23, 1.602176634e-19


def planck(lam, T):
    return 8 * np.pi * h * c / (lam**5 * (np.expm1(h * c / (lam * kB * T))))


def rayleigh_jeans(lam, T):
    return 8 * np.pi * kB * T / lam**4


# --- 1. Catástrofe ultravioleta -------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.9)
lam = np.linspace(60e-9, 2500e-9, 3000)
temps = [4000, 5000, 6000]
ymax = planck(2.897771955e-3 / temps[-1], temps[-1]) * 1e-6
for i, T in enumerate(temps):
    ax.plot(lam * 1e9, planck(lam, T) * 1e-6, color=qf.PALETTE[i])
    lmax = 2.897771955e-3 / T
    pmax = planck(lmax, T) * 1e-6
    ax.plot(lmax * 1e9, pmax, "o", color=qf.PALETTE[i], ms=3.5, zorder=5)
    ax.text(lmax * 1e9 + 55, pmax, f"{T} K", color=qf.PALETTE[i],
            fontsize=8, va="center", ha="left")
# Rayleigh-Jeans: se sale del marco, que es exactamente el argumento
rj = rayleigh_jeans(lam, 6000) * 1e-6
ax.plot(lam * 1e9, rj, "--", color=qf.MUTED, lw=1.1)
ax.text(1500, ymax * 0.72, "Rayleigh–Jeans\n(6000 K)", color=qf.MUTED,
        fontsize=7.5, ha="left", va="center")
ax.annotate("catástrofe\nultravioleta", xy=(905, ymax * 1.38),
            xytext=(1080, ymax * 1.16), fontsize=7.5, color=qf.ACCENT,
            va="center", ha="left",
            arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
# lugar geométrico de los máximos (ley de Wien)
Tw = np.linspace(3500, 6500, 100)
ax.plot(2.897771955e-3 / Tw * 1e9, planck(2.897771955e-3 / Tw, Tw) * 1e-6,
        ":", color=qf.MUTED, lw=0.9)
ax.text(300, ymax * 1.20, "lugar de los máximos\n(ley de Wien)",
        color=qf.MUTED, fontsize=7, ha="center", va="center")
ax.set_xlim(0, 2100)
ax.set_ylim(0, ymax * 1.42)
ax.set_xlabel(r"$\lambda$ / nm")
ax.set_ylabel(r"$\rho(\lambda)$ / J m$^{-3}$ nm$^{-1}$")
ax.set_title("Densidad espectral de energía del cuerpo negro", loc="left")
qf.save(fig, "cuerponegro", "planck", "rayleigh-jeans")

# --- 2. Ley de desplazamiento de Wien --------------------------------------
fig, ax = qf.figure(qf.MARGIN, 1.7)
T = np.linspace(1000, 6000, 200)
ax.plot(1 / T * 1e3, 2.897771955e-3 / T * 1e9, color=qf.PALETTE[0])
ax.set_xlabel(r"$1/T$ / $10^{-3}$ K$^{-1}$", fontsize=7.5)
ax.set_ylabel(r"$\lambda_{\max}$ / nm", fontsize=7.5)
ax.tick_params(labelsize=7)
ax.set_title("Ley de Wien", loc="left", fontsize=8)
qf.save(fig, "cuerponegro", "wien")

# --- 3. Efecto fotoeléctrico ----------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.7)
nu = np.linspace(0, 1.6e15, 400)
for i, (metal, Phi) in enumerate([("K  (2.24 eV)", 2.24),
                                  ("Zn (4.31 eV)", 4.31)]):
    Ek = h * nu / e - Phi
    ax.plot(nu[Ek >= 0] / 1e15, Ek[Ek >= 0], color=qf.PALETTE[i])
    nu0 = Phi * e / h
    ax.plot(nu0 / 1e15, 0, "o", color=qf.PALETTE[i], ms=4, zorder=5)
    ax.annotate(r"$\nu_0$", xy=(nu0 / 1e15, 0), xytext=(nu0 / 1e15, -0.42),
                color=qf.PALETTE[i], fontsize=8, ha="center")
    # etiqueta sobre la propia recta, a una altura fija dentro del marco
    y_lab = 1.35
    x_lab = (y_lab + Phi) * e / h / 1e15
    ax.text(x_lab - 0.045, y_lab, metal, color=qf.PALETTE[i],
            fontsize=8, va="center", ha="right")
ax.axhline(0, color=qf.MUTED, lw=0.6)
ax.text(0.04, 2.22, r"pendiente $=h$ para ambos metales",
        fontsize=7.5, color=qf.MUTED)
ax.set_xlim(0, 1.62)
ax.set_ylim(-0.6, 2.4)
ax.set_xlabel(r"$\nu$ / $10^{15}$ s$^{-1}$")
ax.set_ylabel(r"$E_{\rm cin}^{\max}$ / eV")
ax.set_title("Efecto fotoeléctrico", loc="left")
qf.save(fig, "fotoelectrico", "ecin-nu")

# --- 4. Niveles de Bohr y series espectrales -------------------------------
fig, (ax, ax2) = plt.subplots(
    1, 2, figsize=(qf.FULL, 3.0), gridspec_kw=dict(width_ratios=[1, 1.25]))
RH = 109677.58  # cm^-1
ns = np.arange(1, 8)
En = -13.605693 / ns**2
for n, E in zip(ns, En):
    ax.hlines(E, 0, 1, color=qf.INK, lw=1.0)
    # a partir de n=4 los niveles convergen y los rótulos se solaparían
    if n <= 3:
        ax.text(1.04, E, f"$n={n}$", fontsize=7.5, va="center")
ax.hlines(0, 0, 1, color=qf.MUTED, lw=0.8, ls="--")
ax.text(1.04, 0.12, r"$n\to\infty$", fontsize=7.5, va="bottom",
        color=qf.MUTED)

series = [("Lyman", 1, qf.PALETTE[0]), ("Balmer", 2, qf.PALETTE[1]),
          ("Paschen", 3, qf.PALETTE[2])]
for k, (nombre, n1, col) in enumerate(series):
    x0 = 0.13 + 0.30 * k
    for n2 in range(n1 + 1, n1 + 5):
        ax.annotate("", xy=(x0, -13.605693 / n1**2),
                    xytext=(x0, -13.605693 / n2**2),
                    arrowprops=dict(arrowstyle="->", color=col, lw=0.8))
        x0 += 0.045
    ax.text(0.13 + 0.30 * k, 1.1, nombre, color=col, fontsize=7.5, ha="left")
ax.set_xlim(0, 1.35)
ax.set_ylim(-14.6, 2.4)
ax.set_ylabel(r"$E_n$ / eV")
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.set_title("Niveles del átomo de hidrógeno", loc="left")

# espectro de líneas
for nombre, n1, col in series:
    for n2 in range(n1 + 1, 12):
        lam = 1e7 / (RH * (1 / n1**2 - 1 / n2**2))   # nm
        if 60 < lam < 2100:
            ax2.vlines(lam, 0, 1, color=col, lw=1.0)
ax2.set_xscale("log")
ax2.set_xlim(80, 2200)
ax2.set_ylim(0, 1.35)
ax2.set_yticks([])
ax2.spines["left"].set_visible(False)
ax2.set_xlabel(r"$\lambda$ / nm  (escala log)")
ax2.axvspan(380, 750, color="#f0f0f0", zorder=0)
ax2.text(np.sqrt(380 * 750), 1.12, "visible", ha="center", fontsize=7,
         color=qf.MUTED)
for nombre, n1, col in series:
    lam0 = 1e7 / (RH * (1 / n1**2 - 1 / (n1 + 1)**2))
    ax2.text(lam0, 1.03, nombre, color=col, fontsize=7.5, ha="center")
ax2.set_title("Series espectrales", loc="left")
fig.tight_layout()
qf.save(fig, "hidrogeno", "bohr-series")

# --- 5. Longitud de onda de De Broglie -------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.6)
objetos = [("electrón\n(100 eV)", 9.109e-31, 5.9e6),
           ("protón\n(térmico)", 1.673e-27, 2.5e3),
           ("C$_{60}$", 1.196e-24, 200),
           ("pelota\n(50 g, 40 m/s)", 0.05, 40)]
lams = [h / (m * v) for _, m, v in objetos]
ys = np.arange(len(objetos))[::-1]
ax.barh(ys, lams, color=qf.PALETTE[0], height=0.5)
ax.set_xscale("log")
for y, (nombre, m, v), lam in zip(ys, objetos, lams):
    m_, ex = f"{lam:.1e}".split("e")
    ax.text(lam * 1.6, y, rf"${m_}\times10^{{{int(ex)}}}$ m", va="center",
            fontsize=7.5, color=qf.INK)
ax.set_yticks(ys)
ax.set_yticklabels([o[0] for o in objetos], fontsize=7.5)
ax.axvspan(1e-11, 1e-9, color="#f0f0f0", zorder=0)
ax.set_ylim(-0.55, 3.75)
ax.text(3e-11, 3.68, "escala\natómica", fontsize=7, color=qf.MUTED,
        ha="center", va="top")
ax.set_xlim(1e-36, 1e-6)
ax.set_xlabel(r"$\lambda_{\rm dB}=h/p$ / m")
ax.set_title("Por qué no vemos difractar una pelota", loc="left")
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
qf.save(fig, "debroglie", "lambda-masa")
