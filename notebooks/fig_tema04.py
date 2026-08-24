"""Tema 4 — Momento angular, armónicos esféricos y rotor rígido."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm_y
import qf2figs as qf


def Y(l, m, theta, phi):
    """Armónico esférico (convenio scipy >=1.15: sph_harm_y(l, m, theta, phi))."""
    return sph_harm_y(l, m, theta, phi)


# --- 1. Modelo vectorial: conos de precesión -------------------------------
fig, ax = qf.figure(qf.TEXT, 2.9)
l = 2
mod = np.sqrt(l * (l + 1))
for m in range(l, -l - 1, -1):
    col = qf.PALETTE[abs(m) % 6]
    ax.annotate("", xy=(0, m), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-", color="none"))
    r = np.sqrt(mod**2 - m**2)
    ax.plot([0, r], [0, m], color=col, lw=1.3)
    ax.plot([0, -r], [0, m], color=col, lw=1.3, alpha=0.35)
    # elipse que representa el cono visto de lado
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(r * np.cos(t), m + 0.16 * r * np.sin(t), color=col, lw=0.7,
            ls="--", alpha=0.8)
    ax.plot(r, m, "o", color=col, ms=4)
    ax.text(-2.85, m, f"$m_l={m:+d}$" if m else "$m_l=0$", fontsize=7.5,
            color=col, va="center", ha="left")
ax.annotate("", xy=(0, 3.05), xytext=(0, -2.75),
            arrowprops=dict(arrowstyle="-|>", color=qf.MUTED, lw=0.7))
ax.text(0.10, 3.02, "$z$", fontsize=8, color=qf.MUTED)
# el módulo del vector, marcado sobre el eje z para comparar con l_z^max
ax.hlines(mod, -0.16, 0.16, color=qf.ACCENT, lw=1.2)
ax.text(0.22, mod + 0.02, r"$|\mathbf{l}|=\sqrt{6}\,\hbar=2.45\,\hbar$",
        fontsize=7.5, color=qf.ACCENT, va="bottom")
ax.text(0.22, 2.0 - 0.30,
        r"$l_z^{\max}=2\hbar$" "\n" r"$\Rightarrow$ nunca se alinea con $z$",
        fontsize=7, color=qf.ACCENT, va="top")
ax.set_xlim(-3.1, 3.6)
ax.set_ylim(-2.9, 3.3)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([-2, -1, 0, 1, 2])
ax.set_ylabel(r"$l_z\,/\,\hbar$")
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.set_title(r"Modelo vectorial del momento angular ($l=2$)", loc="left")
qf.save(fig, "momangular", "modelo-vectorial", "l2")

# --- 2. Armónicos esféricos REALES en 3D -----------------------------------
# Son los que usa la Química (p_x, p_y, d_xy...) y los que se necesitan
# en los Temas 5 y 10 para hibridación. Combinaciones de Y_l^{\pm m}.
th = np.linspace(0, np.pi, 120)
ph = np.linspace(0, 2 * np.pi, 240)
TH, PH = np.meshgrid(th, ph, indexing="ij")

reales = [
    (r"$s$",              lambda t, p: np.full_like(t, 0.2821)),
    (r"$p_z$",            lambda t, p: 0.4886 * np.cos(t)),
    (r"$p_x$",            lambda t, p: 0.4886 * np.sin(t) * np.cos(p)),
    (r"$d_{z^2}$",        lambda t, p: 0.3154 * (3 * np.cos(t)**2 - 1)),
    (r"$d_{xz}$",         lambda t, p: 1.0925 * np.sin(t) * np.cos(t) * np.cos(p)),
    (r"$d_{x^2-y^2}$",    lambda t, p: 0.5463 * np.sin(t)**2 * np.cos(2 * p)),
]
POS, NEG = "#4A90C4", "#D98A5A"     # tonos suaves de la familia de la paleta
fig = plt.figure(figsize=(qf.FULL, 1.85))
for i, (nombre, f) in enumerate(reales):
    ax = fig.add_subplot(1, 6, i + 1, projection="3d")
    val = f(TH, PH)
    R = np.abs(val)
    X = R * np.sin(TH) * np.cos(PH)
    Yc = R * np.sin(TH) * np.sin(PH)
    Z = R * np.cos(TH)
    cols = np.where(val[..., None] >= 0,
                    np.array(plt.matplotlib.colors.to_rgba(POS)),
                    np.array(plt.matplotlib.colors.to_rgba(NEG)))
    ax.plot_surface(X, Yc, Z, rstride=3, cstride=3, linewidth=0,
                    antialiased=True, facecolors=cols, shade=True)
    lim = np.max(R) * 0.70
    ax.set(xlim=(-lim, lim), ylim=(-lim, lim), zlim=(-lim, lim))
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=18, azim=32)
    ax.set_axis_off()
    ax.set_title(nombre, fontsize=8.5, pad=-2)
fig.suptitle("Armónicos esféricos reales (azul $+$, naranja $-$)",
             fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.88))
qf.save(fig, "armonicosesf", "orbitales-reales")

# --- 3. Nodos de |Y|^2 en proyección (theta, phi) --------------------------
casos = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2)]
fig, axes = plt.subplots(2, 3, figsize=(qf.TEXT, 2.6), sharex=True,
                         sharey=True)
for ax, (l, m) in zip(axes.flat, casos):
    val = np.real(Y(l, m, TH, PH) * np.conj(Y(l, m, TH, PH)))
    ax.pcolormesh(np.degrees(PH), np.degrees(TH), val, cmap="Blues",
                  shading="auto", rasterized=True)
    ax.set_title(rf"$l={l},\ m_l={m}$", fontsize=7.5, loc="left")
    ax.set_xticks([0, 180, 360])
    ax.set_yticks([0, 90, 180])
    ax.tick_params(labelsize=6.5)
    ax.invert_yaxis()
for ax in axes[-1]:
    ax.set_xlabel(r"$\phi$ / $^\circ$", fontsize=7.5)
for ax in axes[:, 0]:
    ax.set_ylabel(r"$\theta$ / $^\circ$", fontsize=7.5)
fig.suptitle(r"$|Y_{l,m_l}|^2$: los nodos aumentan con $l$", fontsize=8.5,
             x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.91))
qf.save(fig, "armonicosesf", "densidad-nodos")

# --- 4. Rotor rígido: niveles y espectro -----------------------------------
fig, (ax, ax2) = plt.subplots(1, 2, figsize=(qf.FULL, 2.7),
                              gridspec_kw=dict(width_ratios=[1, 1.4]))
B = 10.59  # cm^-1, HCl
Js = np.arange(0, 7)
for J in Js:
    E = B * J * (J + 1)
    ax.hlines(E, 0, 1, color=qf.INK, lw=1.1)
    ax.text(1.05, E, f"$J={J}$   ($g={2*J+1}$)", fontsize=7, va="center")
for J in Js[:-1]:
    ax.annotate("", xy=(0.45, B * (J + 1) * (J + 2)), xytext=(0.45, B * J * (J + 1)),
                arrowprops=dict(arrowstyle="->", color=qf.PALETTE[0], lw=0.8))
ax.set_xlim(0, 2.3)
ax.set_ylim(-20, B * 6 * 7 * 1.12)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
ax.set_ylabel(r"$\tilde{F}(J)=BJ(J+1)$ / cm$^{-1}$")
ax.set_title(r"Rotor rígido ($B=10.59$ cm$^{-1}$, HCl)", loc="left")

for J in range(0, 9):
    nu = 2 * B * (J + 1)
    inten = (2 * J + 1) * np.exp(-B * J * (J + 1) * 1.4388 / 298)
    ax2.vlines(nu, 0, inten, color=qf.PALETTE[0], lw=1.6)
ax2.annotate("", xy=(2 * B * 2, 5.6), xytext=(2 * B * 1, 5.6),
             arrowprops=dict(arrowstyle="<->", color=qf.ACCENT, lw=0.8))
ax2.text(2 * B * 1.5, 5.9, r"$2B$", color=qf.ACCENT, fontsize=8, ha="center")
ax2.set_xlim(0, 200)
ax2.set_ylim(0, 7)
ax2.set_xlabel(r"$\tilde{\nu}$ / cm$^{-1}$")
ax2.set_ylabel("intensidad rel.")
ax2.set_title(r"Espectro rotacional: líneas equiespaciadas $2B$", loc="left")
fig.tight_layout()
qf.save(fig, "rotorrigido", "niveles-espectro")
