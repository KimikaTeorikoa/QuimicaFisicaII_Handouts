"""Tema 5 — Átomo de hidrógeno: funciones radiales, RDF, orbitales, Zeeman."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, factorial
import qf2figs as qf

a0 = 1.0     # trabajamos en unidades de a0


def R_nl(n, l, r, Z=1):
    rho = 2 * Z * r / (n * a0)
    norm = np.sqrt((2 * Z / (n * a0))**3 * factorial(n - l - 1) /
                   (2 * n * factorial(n + l)))
    return norm * rho**l * np.exp(-rho / 2) * genlaguerre(n - l - 1, 2 * l + 1)(rho)


orbitales = [(1, 0, "1s"), (2, 0, "2s"), (2, 1, "2p"),
             (3, 0, "3s"), (3, 1, "3p"), (3, 2, "3d")]

# --- 1. Funciones radiales R_nl --------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(qf.FULL, 3.0), sharex=True)
r = np.linspace(1e-6, 25, 2000)
for ax, (n, l, nombre) in zip(axes.flat, orbitales):
    R = R_nl(n, l, r)
    ax.plot(r, R, color=qf.PALETTE[0])
    ax.axhline(0, color=qf.MUTED, lw=0.5)
    # nodos radiales: n - l - 1
    nodos = n - l - 1
    if nodos:
        sign = np.sign(R)
        idx = np.where(np.diff(sign) != 0)[0]
        ax.plot(r[idx], np.zeros_like(idx), "o", color=qf.ACCENT, ms=4,
                zorder=5)
    ax.set_title(f"{nombre}   ({nodos} nodo{'s' if nodos != 1 else ''} radial"
                 f"{'es' if nodos != 1 else ''})", fontsize=7.5, loc="left")
    ax.set_xlim(0, 25)
    ax.tick_params(labelsize=7)
for ax in axes[-1]:
    ax.set_xlabel(r"$r/a_0$", fontsize=8)
for ax in axes[:, 0]:
    ax.set_ylabel(r"$R_{n,l}(r)$", fontsize=8)
fig.suptitle(r"Funciones radiales: el número de nodos es $n-l-1$",
             fontsize=9, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.92))
qf.save(fig, "hidrogeno", "radial", "Rnl")

# --- 2. Función de distribución radial -------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 2.6), sharey=False)
r = np.linspace(1e-6, 30, 4000)
ax = axes[0]
offs = {"1s": (0.6, 0.0), "2s": (0.8, 0.022), "2p": (-1.9, 0.020)}
for i, (n, l, nombre) in enumerate([(1, 0, "1s"), (2, 0, "2s"), (2, 1, "2p")]):
    P = r**2 * R_nl(n, l, r)**2
    ax.plot(r, P, color=qf.PALETTE[i])
    rmax = r[np.argmax(P)]
    rmed = np.trapz(r * P, r) / np.trapz(P, r)
    ax.plot(rmax, P.max(), "o", color=qf.PALETTE[i], ms=4)
    dx, dy = offs[nombre]
    qf.label_line(ax, rmax + dx, P.max() + dy, nombre, qf.PALETTE[i])
    print(f"    {nombre}: r_max={rmax:.2f} a0, <r>={rmed:.2f} a0")
ax.set_xlim(0, 16)
ax.set_xlabel(r"$r/a_0$")
ax.set_ylabel(r"$P(r)=r^2R^2$")
ax.set_title(r"$r_{\max}(1s)=a_0$;  penetración del 2s", loc="left",
             fontsize=8.5)
# zona de penetración
P2s = r**2 * R_nl(2, 0, r)**2
ax.fill_between(r, 0, P2s, where=(r < 2.1), color=qf.PALETTE[1], alpha=0.25,
                lw=0)
ax.annotate("penetración\ninterna del 2s", xy=(1.1, 0.06), xytext=(4.2, 0.30),
            fontsize=7, color=qf.PALETTE[1],
            arrowprops=dict(arrowstyle="->", color=qf.PALETTE[1], lw=0.7))

ax = axes[1]
offs3 = {"3s": (1.0, 0.006), "3p": (1.0, -0.008), "3d": (-2.6, 0.004)}
for i, (n, l, nombre) in enumerate([(3, 0, "3s"), (3, 1, "3p"), (3, 2, "3d")]):
    P = r**2 * R_nl(n, l, r)**2
    ax.plot(r, P, color=qf.PALETTE[i])
    dx, dy = offs3[nombre]
    qf.label_line(ax, r[np.argmax(P)] + dx, P.max() + dy, nombre,
                  qf.PALETTE[i])
ax.set_xlim(0, 30)
ax.set_xlabel(r"$r/a_0$")
ax.set_ylabel(r"$P(r)=r^2R^2$")
ax.set_title("Capa $n=3$: a igual $n$, menor $l$ penetra más", loc="left",
             fontsize=8.5)
fig.tight_layout()
qf.save(fig, "hidrogeno", "rdf", "1s-3d")

# --- 3. Cortes 2D de |psi|^2 -----------------------------------------------
fig, axes = plt.subplots(1, 4, figsize=(qf.FULL, 1.9))
N = 400
lim = 16
xx, zz = np.meshgrid(np.linspace(-lim, lim, N), np.linspace(-lim, lim, N))
rr = np.sqrt(xx**2 + zz**2) + 1e-9
ct = zz / rr
casos = [(1, 0, "s", "$1s$"), (2, 0, "s", "$2s$"),
         (2, 1, "pz", "$2p_z$"), (3, 2, "dz2", "$3d_{z^2}$")]
for ax, (n, l, tipo, nombre) in zip(axes, casos):
    ang = {"s": np.full_like(ct, 0.2821),
           "pz": 0.4886 * ct,
           "dz2": 0.3154 * (3 * ct**2 - 1)}[tipo]
    psi = R_nl(n, l, rr) * ang
    d = psi**2
    ax.imshow(d**0.35, cmap="Blues", origin="lower",
              extent=(-lim, lim, -lim, lim), rasterized=True)
    ax.set_title(nombre, fontsize=8.5, loc="left")
    ax.set_xticks([])
    ax.set_yticks([])
fig.suptitle(r"Cortes en el plano $xz$ de $|\psi_{n,l,m}|^2$ "
             r"(escala realzada)", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.86))
qf.save(fig, "hidrogeno", "densidad-2d")

# --- 4. Niveles y degeneración ---------------------------------------------
fig, ax = qf.figure(qf.TEXT, 2.6)
for n in range(1, 6):
    E = -13.6057 / n**2
    for l in range(n):
        ax.hlines(E, l * 1.05, l * 1.05 + 0.9, color=qf.PALETTE[l % 6], lw=1.5)
    ax.text(-0.25, E, f"$n={n}$", fontsize=7.5, ha="right", va="center")
    ax.text(4.6, E, rf"$n^2={n**2}$", fontsize=7, ha="left", va="center",
            color=qf.MUTED)
ax.axhline(0, color=qf.MUTED, lw=0.8, ls="--")
ax.text(-0.25, 0, r"$n=\infty$", fontsize=7.5, ha="right", va="center",
        color=qf.MUTED)
for l, nom in enumerate("spdf"):
    ax.text(l * 1.05 + 0.45, 1.0, nom, fontsize=8.5, ha="center",
            color=qf.PALETTE[l % 6])
ax.text(4.6, 1.0, "degen.", fontsize=7, ha="left", color=qf.MUTED)
ax.set_xlim(-1.1, 5.6)
ax.set_ylim(-14.6, 2.0)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.set_ylabel(r"$E_n$ / eV")
ax.set_title(r"En el hidrógeno $E$ depende sólo de $n$: degeneración $n^2$",
             loc="left", fontsize=8.5)
qf.save(fig, "hidrogeno", "niveles-degeneracion")

# --- 5. Efecto Zeeman ------------------------------------------------------
fig, ax = qf.figure(qf.MARGIN, 2.0)
muB = 5.7883818e-5    # eV/T
B = np.linspace(0, 10, 100)
for m, col in zip([1, 0, -1], [qf.PALETTE[0], qf.PALETTE[2], qf.PALETTE[1]]):
    ax.plot(B, m * muB * B * 1e3, color=col)
    ax.text(10.4, m * muB * 10 * 1e3, f"$m_l={m:+d}$" if m else "$m_l=0$",
            fontsize=6.5, va="center", color=col)
ax.set_xlim(0, 10)
ax.set_xlabel("$B_z$ / T", fontsize=7.5)
ax.set_ylabel(r"$E-E_n$ / meV", fontsize=7.5)
ax.tick_params(labelsize=7)
ax.set_title("Efecto Zeeman ($l=1$)", loc="left", fontsize=8)
qf.save(fig, "zeeman", "desdoblamiento", "l1")
