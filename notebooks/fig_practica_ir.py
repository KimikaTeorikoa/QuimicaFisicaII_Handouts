"""Prácticas — Espectroscopía IR: espectro roto-vibracional y Morse.

Reproduce el análisis de practicas_exp_ir.tex para el HCl, de modo que el
alumno vea de antemano la forma del espectro que va a medir y el método
de diferencias entre combinaciones que tendrá que aplicar.
"""
import numpy as np
import matplotlib.pyplot as plt
import qf2figs as qf

# Parámetros del HCl (cm^-1)
nu0 = 2885.9
B0, B1 = 10.440, 10.137
D = 5.3e-4
T = 298.0
c2 = 1.4388     # hc/kB en cm K


def poblacion(J, B):
    return (2 * J + 1) * np.exp(-c2 * B * J * (J + 1) / T)


# --- 1. Espectro roto-vibracional P / R ------------------------------------
fig, ax = qf.figure(qf.FULL, 2.8)
Js = np.arange(0, 14)
nuP = nu0 - (B1 + B0) * Js[1:] + (B1 - B0) * Js[1:]**2
nuR = nu0 + (B1 + B0) * (Js + 1) + (B1 - B0) * (Js + 1)**2
IP = poblacion(Js[1:], B0)
IR = poblacion(Js, B0)
Imax = max(IP.max(), IR.max())
ax.vlines(nuP, 0, IP / Imax, color=qf.PALETTE[0], lw=1.5)
ax.vlines(nuR, 0, IR / Imax, color=qf.PALETTE[1], lw=1.5)
ax.axvline(nu0, color=qf.MUTED, lw=0.9, ls="--")
ax.text(nu0, 1.42, r"origen de banda $\tilde{\nu}_0$" "\n"
        r"(rama Q ausente en HCl)", fontsize=7, ha="center", color=qf.MUTED,
        va="top")
ax.text(nu0 - 155, 1.17, r"rama P  ($\Delta J=-1$)", fontsize=8,
        color=qf.PALETTE[0], ha="center")
ax.text(nu0 + 155, 1.17, r"rama R  ($\Delta J=+1$)", fontsize=8,
        color=qf.PALETTE[1], ha="center")
for J, x, y in zip(Js[1:5], nuP[:4], IP[:4] / Imax):
    ax.text(x, y + 0.03, f"{J}", fontsize=6, ha="center", color=qf.PALETTE[0])
for J, x, y in zip(Js[:4], nuR[:4], IR[:4] / Imax):
    ax.text(x, y + 0.03, f"{J}", fontsize=6, ha="center", color=qf.PALETTE[1])
ax.set_xlim(nu0 - 320, nu0 + 320)
ax.set_ylim(0, 1.5)
ax.set_xlabel(r"$\tilde{\nu}$ / cm$^{-1}$")
ax.set_ylabel("intensidad relativa")
ax.set_title(r"Espectro roto-vibracional del HCl ($v=0\to1$): la intensidad "
             r"sigue la población de Boltzmann", loc="left", fontsize=8.5)
qf.save(fig, "hcl", "rotovibracional", "PR")

# --- 2. Método de las diferencias entre combinaciones ----------------------
fig, axes = plt.subplots(1, 2, figsize=(qf.FULL, 2.5))
J = np.arange(1, 11)
nuP_J = nu0 - (B1 + B0) * J + (B1 - B0) * J**2
nuR_J = nu0 + (B1 + B0) * (J + 1) + (B1 - B0) * (J + 1)**2
nuR_Jm1 = nu0 + (B1 + B0) * J + (B1 - B0) * J**2
nuP_Jp1 = nu0 - (B1 + B0) * (J + 1) + (B1 - B0) * (J + 1)**2

ax = axes[0]
y = nuR_J - nuP_J
ax.plot(J + 0.5, y, "o", color=qf.PALETTE[0], ms=4)
p = np.polyfit(J + 0.5, y, 1)
ax.plot(J + 0.5, np.polyval(p, J + 0.5), color=qf.PALETTE[0], lw=1.0)
ax.set_xlabel(r"$J+\frac{1}{2}$")
ax.set_ylabel(r"$\tilde{\nu}_R(J)-\tilde{\nu}_P(J)$ / cm$^{-1}$")
ax.set_title(rf"pendiente $=4B_1 \Rightarrow B_1={p[0]/4:.3f}$ cm$^{{-1}}$",
             fontsize=8.5, loc="left")

ax = axes[1]
y2 = nuR_Jm1 - nuP_Jp1
ax.plot(J + 0.5, y2, "o", color=qf.PALETTE[1], ms=4)
p2 = np.polyfit(J + 0.5, y2, 1)
ax.plot(J + 0.5, np.polyval(p2, J + 0.5), color=qf.PALETTE[1], lw=1.0)
ax.set_xlabel(r"$J+\frac{1}{2}$")
ax.set_ylabel(r"$\tilde{\nu}_R(J-1)-\tilde{\nu}_P(J+1)$ / cm$^{-1}$")
ax.set_title(rf"pendiente $=4B_0 \Rightarrow B_0={p2[0]/4:.3f}$ cm$^{{-1}}$",
             fontsize=8.5, loc="left")
print(f"    recuperado B1={p[0]/4:.4f} (dado {B1})   "
      f"B0={p2[0]/4:.4f} (dado {B0})")
fig.suptitle("Diferencias entre combinaciones: cada recta da una constante "
             "rotacional", fontsize=8.5, x=0.02, ha="left")
fig.tight_layout(rect=(0, 0, 1, 0.90))
qf.save(fig, "hcl", "diferencias-combinaciones")

# --- 3. Morse frente a armónico: anarmonicidad y sobretonos ----------------
fig, ax = qf.figure(qf.TEXT, 2.7)
De_cm = 37255.0        # cm^-1 para HCl
we, wexe = 2990.9, 52.8
Re = 1.2746
mu = 1.62661e-27
beta = we * 2 * np.pi * 2.998e10 * np.sqrt(mu / (2 * 6.626e-34 * 2.998e10 * De_cm)) * 1e-10
R = np.linspace(0.7, 4.2, 700)
Vm = De_cm * (1 - np.exp(-beta * (R - Re)))**2
Vh = 0.5 * (2 * np.pi * we * 2.998e10)**2 * mu * ((R - Re) * 1e-10)**2 \
    / (6.626e-34 * 2.998e10)
ax.plot(R, Vm, color=qf.PALETTE[0])
ax.plot(R, Vh, "--", color=qf.PALETTE[1])
qf.label_line(ax, 2.6, De_cm * 0.80, "Morse (anarmónico)", qf.PALETTE[0],
              fontsize=7.5)
qf.label_line(ax, 1.85, De_cm * 0.92, "armónico", qf.PALETTE[1], fontsize=7.5)
for v in range(7):
    G = we * (v + 0.5) - wexe * (v + 0.5)**2
    disc = 1 - np.sqrt(G / De_cm)
    lo = Re - np.log(1 + np.sqrt(G / De_cm)) / beta
    hi = Re - np.log(disc) / beta if disc > 0 else 3.6
    ax.hlines(G, lo, hi, color=qf.MUTED, lw=0.6)
ax.annotate("", xy=(1.05, we - wexe), xytext=(1.05, 0.5 * we - 0.25 * wexe),
            arrowprops=dict(arrowstyle="->", color=qf.ACCENT, lw=0.9))
ax.text(0.99, we * 0.8, "fundamental\n$0\\to1$", fontsize=6.5,
        color=qf.ACCENT, ha="right", va="center")
ax.annotate("", xy=(3.35, 2 * we - 6 * wexe),
            xytext=(3.35, 0.5 * we - 0.25 * wexe),
            arrowprops=dict(arrowstyle="->", color=qf.PALETTE[2], lw=0.9))
ax.text(3.42, we, "sobretono\n$0\\to2$", fontsize=6.5, color=qf.PALETTE[2],
        va="center")
ax.axhline(De_cm, color=qf.MUTED, lw=0.7, ls=":")
ax.text(4.15, De_cm * 1.02, r"$D_e$", fontsize=8, ha="right", color=qf.MUTED)
ax.set_xlim(0.7, 4.2)
ax.set_ylim(0, De_cm * 1.15)
ax.set_xlabel(r"$R$ / Å")
ax.set_ylabel(r"$G(v)$ / cm$^{-1}$")
ax.set_title("Anarmonicidad: los niveles convergen y aparecen sobretonos",
             loc="left", fontsize=8.5)
qf.save(fig, "hcl", "morse-vs-armonico")
