"""Tema 10 — Moléculas poliatómicas: hibridación y método de Hückel."""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

POS, NEG = "#4A90C4", "#D98A5A"

# --- 1. Construcción de un híbrido sp: interferencia s + p -----------------
fig, axes = plt.subplots(1, 3, figsize=(qf.FULL, 1.9), sharey=True)
th = np.linspace(0, 2 * np.pi, 600)
funcs = [(lambda t: np.full_like(t, 0.35), "$s$"),
         (lambda t: 0.6 * np.cos(t), "$p_z$"),
         (lambda t: 0.35 + 0.6 * np.cos(t), "$h=s+p_z$")]
for ax, (f, nombre) in zip(axes, funcs):
    val = f(th)
    r = np.abs(val)
    ax.plot(r * np.sin(th), r * np.cos(th), color=qf.MUTED, lw=0.6)
    for sgn, col in [(1, POS), (-1, NEG)]:
        m = np.sign(val) == sgn
        ax.fill(np.where(m, r * np.sin(th), np.nan),
                np.where(m, r * np.cos(th), np.nan), color=col, alpha=0.85,
                lw=0)
    ax.set_title(nombre, fontsize=9, loc="left")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.plot(0, 0, "o", color=qf.INK, ms=3)
axes[2].annotate("interferencia constructiva\n(el híbrido apunta)",
                 xy=(0.05, 0.85), xytext=(-0.75, 1.15), fontsize=6.5,
                 color=qf.ACCENT,
                 arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.7))
fig.suptitle("Un orbital híbrido es interferencia entre $s$ y $p$",
             fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.88))
qf.save(fig, "hibridacion", "construccion-sp")

# --- 2. Geometrías sp, sp2, sp3 --------------------------------------------
fig = plt.figure(figsize=(qf.FULL, 2.0))
geoms = [
    ("sp (lineal, 180°)", [(0, 0, 1), (0, 0, -1)]),
    ("sp$^2$ (trigonal, 120°)",
     [(np.cos(a), np.sin(a), 0) for a in np.radians([90, 210, 330])]),
    ("sp$^3$ (tetraédrica, 109.47°)",
     [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]),
]
for i, (tit, dirs) in enumerate(geoms):
    ax = fig.add_subplot(1, 3, i + 1, projection="3d")
    for d in dirs:
        d = np.array(d, float)
        d /= np.linalg.norm(d)
        ax.quiver(0, 0, 0, *d, color=POS, lw=2.2, arrow_length_ratio=0.22)
    ax.plot([0], [0], [0], "o", color=qf.INK, ms=5)
    ax.set(xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1))
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=18, azim=35)
    ax.set_axis_off()
    ax.set_title(tit, fontsize=8, pad=-2)
# comprobación numérica del ángulo tetraédrico
v1, v2 = np.array([1, 1, 1.]), np.array([1, -1, -1.])
ang = np.degrees(np.arccos(v1 @ v2 / (np.linalg.norm(v1) * np.linalg.norm(v2))))
print(f"    ángulo tetraédrico calculado: {ang:.2f}°")
fig.suptitle("Geometrías de los conjuntos de híbridos", fontsize=8.5,
             x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.9))
qf.save(fig, "hibridacion", "geometrias")

# --- 3. Hückel: butadieno y benceno ----------------------------------------
def huckel(n, ciclico=False):
    H = np.zeros((n, n))
    for i in range(n - 1):
        H[i, i + 1] = H[i + 1, i] = 1.0
    if ciclico:
        H[0, -1] = H[-1, 0] = 1.0
    w, v = np.linalg.eigh(H)
    return w[::-1], v[:, ::-1]          # x tal que E = alpha + x*beta


fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 3.0), sharey=True)
for ax, (n, ciclico, nombre, nelec) in zip(
        axes, [(4, False, "butadieno", 4), (6, True, "benceno", 6)]):
    xs, vecs = huckel(n, ciclico)
    ocupados = 0
    # agrupar niveles degenerados
    usados = np.zeros(n, bool)
    for i, x in enumerate(xs):
        if usados[i]:
            continue
        deg = np.where(np.abs(xs - x) < 1e-8)[0]
        usados[deg] = True
        for k, idx in enumerate(deg):
            off = (k - (len(deg) - 1) / 2) * 0.55
            ax.hlines(x, off - 0.22, off + 0.22, color=qf.PALETTE[0], lw=1.8)
            ne = min(2, max(0, nelec - ocupados))
            for e in range(ne):
                ax.plot(off + (-0.07 if e == 0 else 0.07), x,
                        marker=r"$\uparrow$" if e == 0 else r"$\downarrow$",
                        color=qf.INK, ms=7, linestyle="none")
            ocupados += ne
        ax.text(0.72, x, f"$\\alpha{x:+.3f}\\beta$", fontsize=7,
                va="center", color=qf.MUTED)
    Etot = 2 * sum(xs[:nelec // 2])
    Eloc = nelec / 2 * 2 * 1.0        # n/2 enlaces dobles aislados: 2*1*beta c/u
    ax.set_title(f"{nombre}: $E_\\pi={nelec}\\alpha{Etot:+.3f}\\beta$",
                 fontsize=8.5, loc="left")
    ax.text(0.02, 0.03, f"deslocalización: {Etot - Eloc:+.3f}$\\beta$",
            transform=ax.transAxes, fontsize=7.5, color=qf.ACCENT)
    ax.set_xlim(-1.0, 1.5)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.axhline(0, color=qf.MUTED, lw=0.6, ls=":")
    print(f"    {nombre}: x = {np.round(xs, 4)}  E_pi = {nelec}a {Etot:+.4f}b")
axes[0].set_ylabel(r"$(E-\alpha)/\beta$   ($\beta<0$: arriba = más estable)")
fig.suptitle("Método de Hückel: niveles $\\pi$ y energía de deslocalización",
             fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.92))
qf.save(fig, "huckel", "niveles", "butadieno-benceno")

# --- 4. HOMO-LUMO frente a la longitud de la cadena conjugada -------------
fig, ax = qf.figure(qf.TEXT, 2.4)
ns = np.arange(1, 11)
gaps = []
for k in ns:
    xs, _ = huckel(2 * k)
    gaps.append(xs[k - 1] - xs[k])       # HOMO - LUMO en unidades de |beta|
ax.plot(ns, gaps, "-o", color=qf.PALETTE[0], ms=4)
ax.set_xlabel("número de dobles enlaces conjugados")
ax.set_ylabel(r"$\Delta E_{\rm HOMO-LUMO}$ / $|\beta|$")
ax.set_title("Al alargar la conjugación el salto se estrecha:\n"
             r"$\lambda_{\max}$ se desplaza al visible", loc="left",
             fontsize=8.5)
ax.annotate("el color de los carotenos", xy=(8, gaps[7]),
            xytext=(5.0, 1.35), fontsize=7, color=qf.ACCENT,
            arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.8))
qf.save(fig, "huckel", "homo-lumo", "polienos")
