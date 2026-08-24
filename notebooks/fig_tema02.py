"""Tema 2 — Postulados de la Mecánica Cuántica."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

# --- 1. Funciones de onda aceptables y no aceptables ------------------------
fig, axes = plt.subplots(2, 2, figsize=(qf.TEXT, 3.3), sharex=True)
x = np.linspace(-3, 3, 800)

# (a) multivaluada
ax = axes[0, 0]
t = np.linspace(-np.pi / 2 + 0.05, np.pi / 2 - 0.05, 400)
ax.plot(1.6 * np.sin(2 * t), 1.3 * np.sin(t), color=qf.PALETTE[1])
ax.set_title("(a) no unívoca", loc="left", fontsize=8, color=qf.PALETTE[1])

# (b) discontinua
ax = axes[0, 1]
xa, xb = x[x < 0], x[x >= 0]
ax.plot(xa, np.exp(-xa**2) * 0.5, color=qf.PALETTE[1])
ax.plot(xb, np.exp(-xb**2) * 1.2 - 0.35, color=qf.PALETTE[1])
ax.plot(0, 0.5, "o", mfc="white", mec=qf.PALETTE[1], ms=4, mew=1.0)
ax.plot(0, 0.85, "o", color=qf.PALETTE[1], ms=4)
ax.set_title("(b) discontinua", loc="left", fontsize=8, color=qf.PALETTE[1])

# (c) derivada discontinua
ax = axes[1, 0]
ax.plot(x, np.exp(-np.abs(x) * 1.6), color=qf.PALETTE[1])
ax.set_title("(c) derivada discontinua", loc="left", fontsize=8,
             color=qf.PALETTE[1])

# (d) aceptable
ax = axes[1, 1]
ax.plot(x, 1.15 * x * np.exp(-x**2), color=qf.PALETTE[2])
ax.set_title("(d) aceptable", loc="left", fontsize=8, color=qf.PALETTE[2])

for ax in axes.flat:
    ax.axhline(0, color=qf.MUTED, lw=0.5)
    ax.set_yticks([])
    ax.set_xticks([])
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(-3, 3)
fig.supxlabel(r"$x$", fontsize=9, y=0.02)
fig.suptitle("Requisitos de una función de onda admisible", fontsize=9,
             x=0.02, ha="left")
fig.tight_layout(rect=(0, 0.02, 1, 0.94))
qf.save(fig, "postulados", "funciones-admisibles")

# --- 2. Paquete de ondas: localización por superposición ---------------------
fig, axes = plt.subplots(1, 4, figsize=(qf.FULL, 1.9), sharey=True)
x = np.linspace(-12, 12, 2000)
k0, dk = 3.0, 0.55
for ax, N in zip(axes, [1, 3, 11, 81]):
    ks = np.array([k0]) if N == 1 else np.linspace(k0 - 2.2, k0 + 2.2, N)
    w = np.exp(-((ks - k0) ** 2) / (2 * dk ** 2))
    psi = (w[:, None] * np.cos(ks[:, None] * x)).sum(0) / w.sum()
    ax.plot(x, psi, color=qf.PALETTE[0], lw=1.0)
    ax.set_title(f"$N={N}$", fontsize=8, loc="left")
    ax.axhline(0, color=qf.MUTED, lw=0.5)
    ax.set_yticks([])
    ax.set_xticks([-10, 0, 10])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"$x$", fontsize=8)
axes[0].set_ylabel(r"$\Psi(x)$", fontsize=8)
fig.suptitle(r"Superposición de $N$ ondas armónicas: al localizar en $x$ "
             r"se pierde la definición de $p$", fontsize=8.5, x=0.02,
             ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.90))
qf.save(fig, "incertidumbre", "paquete-ondas")

# --- 3. Par x / k: el principio de incertidumbre ----------------------------
fig, axes = plt.subplots(1, 2, figsize=(qf.TEXT, 2.1))
x = np.linspace(-8, 8, 1000)
k = np.linspace(-8, 8, 1000)
for i, s in enumerate([0.5, 1.2, 2.6]):
    axes[0].plot(x, np.exp(-x**2 / (2 * s**2)), color=qf.PALETTE[i])
    axes[1].plot(k, np.exp(-k**2 * s**2 / 2), color=qf.PALETTE[i])
    axes[0].text(0.15, np.exp(-0.15**2 / (2 * s**2)) * 1.02,
                 rf"$\sigma={s}$", color=qf.PALETTE[i], fontsize=7,
                 ha="left", va="bottom")
axes[0].set_xlabel(r"$x$")
axes[0].set_ylabel(r"$|\psi(x)|$")
axes[0].set_title(r"espacio de posiciones", loc="left", fontsize=8)
axes[1].set_xlabel(r"$k \;(\propto p)$")
axes[1].set_ylabel(r"$|\tilde\psi(k)|$")
axes[1].set_title(r"espacio de momentos", loc="left", fontsize=8)
for ax in axes:
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
fig.suptitle(r"Estrechar en $x$ ensancha en $k$:  $\Delta x\,\Delta k\geq 1/2$",
             fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.90))
qf.save(fig, "incertidumbre", "x-k")
