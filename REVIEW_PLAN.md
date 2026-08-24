# Plan de revisión — Química Física II (Apuntes)

Revisión completa del repositorio. Este documento es el plan de trabajo; no se ha
modificado todavía ningún `.tex`.

> **Sincronizado con Overleaf el 2026-08-08** (`cfed413` → `87b19c7`).
> La primera versión de este plan se escribió contra el estado de diciembre de
> 2023, antes de poder hacer `fetch`. Las secciones marcadas ✅ ya están
> resueltas en Overleaf; las marcadas **⚠️ SIN REVISAR** son material nuevo que
> todavía no he leído. Ver §0.0.

---

## 0.0 Estado de sincronización

El `fetch` recuperó un único commit de Overleaf (`87b19c7`, "Update on
Overleaf") que condensa ~2,5 años de trabajo: **14 ficheros, +1327/−298 líneas**.

### Ya corregido en Overleaf (9 de mis hallazgos) ✅

| Tema | Hallazgo | Estado |
|---|---|---|
| 01 | 🔴 Energía de Bohr sin elevar al cuadrado | ✅ corregido |
| 06 | 🟠 Parámetro variacional llamado $Z$ en vez de $\zeta$ | ✅ corregido |
| 07 | 🔴 $E=2h_{1s}+J\pm K$ para el primer excitado | ✅ ahora $h_{1s}+h_{2s}+J\pm K$ |
| 09 | 🔴 Choque `mathabx`/`physics` → no compilaba | ✅ `mathabx` comentado, `braket` añadido |
| 09 | 🔴 Signo menos Unicode (U+2212) | ✅ eliminado |
| 09 | 🔴 "no más de **un** electrón puede ocupar un orbital" | ✅ reescrito (línea 508) |
| 09 | 🔴 "desestabilización del antienlazante > estabilización del **antienlazante**" | ✅ ahora "del enlazante" |
| 09 | 🟠 "se asume que se asume" | ✅ corregido |
| 09 | 🟠 "inpar" | ✅ corregido |

Además, mejora nueva no prevista: nota al margen en tema05 sobre el origen de
las letras *s, p, d, f* (sharp/principal/diffuse/fundamental).

### Sigue en pie

**Los 4 fallos de compilación restantes** (tema04, tema06, math01, math02) —
verificado tras sincronizar. Y todo lo demás del plan salvo lo listado arriba.

### Material nuevo — ✅ YA REVISADO (ver §6)

Nada de esto existía en diciembre de 2023. **Revisado en la sesión del
2026-08-08**; los hallazgos están en la §6 al final del documento.

| Fichero | Líneas | Compila |
|---|---|---|
| `ejercicios/ejercicios_01.tex` | +90 | OK |
| `ejercicios/ejercicios_02.tex` | (era `exercises01`, −83) | OK |
| `ejercicios/ejercicios_03.tex` | +104 | OK |
| `ejercicios/ejercicios_04.tex` | +70 | OK |
| `ejercicios/ejercicios_05.tex` | +75 | OK |
| `ejercicios/ejercicios_06.tex` | (era `exercises02`, ±34) | OK |
| `practicas_exp_ir.tex` | +356 | OK |
| `practicas_exp_uvvis.tex` | +201 | OK |
| `practicas_exp_normativa.tex` | +102 | OK |
| `tema09.tex` — apéndice "Derivación de las ecuaciones de la energía para el H$_2^+$" | dentro de las 499 | OK |
| `tema09.tex` — nueva `\subsection` "Moléculas diatómicas homonucleares y configuraciones electrónicas" | ídem | OK |

Esto **invalida parcialmente el §"Hojas de problemas"** de este plan: ya no hay
dos hojas sino seis, reorganizadas en `ejercicios/`, y mi crítica "no hay hojas
para los temas 7, 9 y 10" puede haber quedado obsoleta. Hay además tres guiones
de prácticas experimentales (IR, UV-Vis, normativa) que son un bloque de curso
entero sin revisar.

### Sigue ausente

- **`tema08`** — no se ha creado.
- **`math02.tex`** — sigue vacío y sin compilar (URL de Overleaf en el `\title`).
- **`tema10.tex`** — sin cambios desde diciembre de 2023.
- **Figuras** — sigue sin haber ni una sola en los apuntes.

**Severidad usada en todo el documento**

| Marca | Significado |
|---|---|
| 🔴 | Bloqueante: impide compilar, o es un error de física/matemáticas que el alumno copiará |
| 🟠 | Error real pero no bloqueante (notación, signo en un sitio, dato numérico) |
| 🟡 | Estilo, ortotipografía, gramática |
| 🔵 | Mejora pedagógica / contenido nuevo propuesto |

---

## 0. Diagnóstico global

### 0.1 Estado de compilación (verificado, `pdflatex` local)

| Fichero | Estado | Causa |
|---|---|---|
| tema01 | OK | |
| tema02 | OK | |
| tema03 | OK | |
| **tema04** | 🔴 **FALLA** | `\bm{\omega}` (línea 91) sin `\usepackage{bm}` |
| tema05 | OK | |
| **tema06** | 🔴 **FALLA** | `\psi_0^{(0)}^\star` → *Double superscript* (líneas 374, 378-379, 389, 394, 398-399, 414) |
| tema07 | OK | |
| tema08 | — | **no existe** (ver §0.3) |
| tema09 | OK ✅ | *arreglado en Overleaf: `mathabx` comentado, `braket` añadido* |
| tema10 | OK | |
| math01 | 🔴 **FALLA** | `\bibliographystyle{plainnat}` dentro de `thebibliography` → natbib author-year |
| **math02** | 🔴 **FALLA** | línea 16: una URL de Overleaf pegada dentro de `\title` (`\tithttps://www.overleaf.com/...le[...]`) |
| ejercicios_01…06 | OK | (6 hojas, ⚠️ sin revisar) |
| practicas_exp_ir / _uvvis / _normativa | OK | (⚠️ sin revisar) |

Quedan **4 fallos**, verificados tras sincronizar con Overleaf. Mientras
persistan no puedes regenerar los apuntes completos fuera de Overleaf, que es un
riesgo real de continuidad.

### 0.2 Infraestructura del repositorio

- 🔴 **No hay ni una sola figura en los apuntes.** `\includegraphics` sólo
  aparece en `sample-handout.tex` (el ejemplo de la plantilla). `figs/planck.png`
  existe pero está huérfano; `graphics/` es íntegramente material de demostración
  de Tufte-LaTeX (`nasa_vision_sm.png`, `hilbertcurves.pdf`, ...). Para un curso
  de mecánica cuántica esto es la carencia más grave del conjunto.
- 🟠 El preámbulo (≈45 líneas) está **duplicado literalmente en los 13 ficheros**,
  y ha divergido: `physics` sólo en 05/07/09/10, `mathabx` en 07/09/10, `booktabs`
  en unos sí y otros no. De ahí salen los fallos de 04 y 09.
  **Propuesta:** un `preamble.tex` común + `\input{preamble}`, o mejor un
  `qf2.sty`. Elimina de golpe tres de los cinco fallos de compilación.
- 🟠 Los `\newcommand{\doccmd}`, `\docopt`, `\docarg`, `docspec`, `\docenv`,
  `\docpkg`, `\doccls`, `\docclsopt` y `\usepackage{lipsum}` son restos de la
  plantilla. No se usan en ningún sitio. Fuera.
- 🟡 `.gitignore` inexistente: `*.aux`, `*.log`, `*.out`, `*.pdf` y `.DS_Store`
  aparecen como *untracked* en `git status`. Añadir uno.
- 🟡 `History.txt`, `Manifest.txt`, `README.txt`, `sample-handout.*`,
  `sample-handout.bib` son de la plantilla Tufte. Mover a `template/` o borrar, y
  escribir un `README.md` propio del curso (cómo compilar, orden de los temas).
- 🔵 Añadir un `Makefile` o `latexmkrc` que compile los 13 documentos y falle
  ruidosamente. Es la única manera de que no vuelva a ocurrir lo del tema04.
- 🔵 No hay bibliografía activa: todos los ficheros terminan con un
  `thebibliography` **comentado** y un `\bibliographystyle{plainnat}` suelto que
  no hace nada. Unificar en `qf2.bib` (Atkins-de Paula, Atkins-Friedman, Levine,
  Fleisch) y citar de verdad en el texto.

### 0.3 Huecos de contenido

- 🔴 **Falta el tema 8.** El tema09 arranca con moléculas diatómicas y el tema10
  dice *"extendemos los conceptos que aplicamos en el caso de las moléculas
  sencillas"*. El hueco entre "átomos polielectrónicos" (07) y "moléculas
  diatómicas" (09) sugiere que faltan **términos espectroscópicos / acoplamiento
  Russell-Saunders** (`²S+¹L_J`, reglas de Hund completas). Hay que decidir: ¿se
  escribe, o se renumera 09→08 y 10→09?
- 🟠 Sólo hay **dos** hojas de problemas (`exercises01` cubre temas 1-4,
  `exercises02` cubre 5-6). **No hay problemas de los temas 7, 9 y 10.**
- 🟠 `math02.tex` ("Laboratorio Matemáticas 2: Ondas") es un **esqueleto vacío**:
  abstract en blanco y una `\section{Fundamentos}` sin contenido.

---

## 1. Revisión tema por tema

### Tema 1 — Antecedentes de la Mecánica Cuántica (`tema01.tex`, 377 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| ✅ | 346-348 | ~~Energía de Bohr: falta elevar al cuadrado el paréntesis~~ | **corregido en Overleaf** |
| 🔴 | 293-297 | Heisenberg escrito como $\Delta x\Delta q\ge\frac12\hbar$ — **son las dos la posición**; además luego define $\Delta p$ y $\Delta q$ sin usar $\Delta x$ | $\Delta x\,\Delta p_x\ge\hbar/2$, y unificar la notación $q\leftrightarrow x$ en todo el tema |
| 🟠 | 106, 109 | Rayleigh-Jeans y Planck: $\rho$ se llama *"densidad de estados"*. **No lo es** | es la **densidad espectral de energía** (J·m⁻³ por unidad de $\lambda$). Aparece 3 veces |
| 🟠 | 175 | "Heinritz Hertz" | **Heinrich** Hertz. Añadir además que la caracterización sistemática es de **Lenard (1902)** |
| 🟠 | 88 | "Kirchoff" | **Kirchhoff** |
| 🟠 | 294 | Etiqueta `eq:heiss` | `eq:heisenberg` (errata que se arrastra a los `\ref`) |
| 🟠 | 164 | $\hbar$ en "m²kg/s" mientras $h$ va en "J·s" | unificar a J·s |
| 🟡 | 267, 285 | Comillas rectas `"..."` en vez de ``` ``...'' ``` | 2 sitios |
| 🟡 | 119, 120 | "monotónicamente" | *monótonamente* |
| 🟡 | 197 | `condici\'on` escrito con escape en un fichero UTF-8 | `condición` |
| 🟡 | 357 | $R_H$=109677 cm⁻¹ sin incertidumbre ni referencia | dar 109677.58 cm⁻¹ |

**Mejoras**

- 🔵 Añadir la **ley de Stefan-Boltzmann** junto a la de Wien; el alumno de 3.º ya
  la conoce y cierra el bloque de cuerpo negro.
- 🔵 Mostrar explícitamente que Planck → Rayleigh-Jeans cuando $hc/\lambda k_BT\ll1$.
  Es un límite de dos líneas y es exactamente el tipo de comprobación que se pide
  en examen.
- 🔵 En el efecto fotoeléctrico, añadir el **potencial de frenado** $V_s$ y la
  recta $eV_s$ vs $\nu$ (pendiente $h$, ordenada $-\Phi$): es el experimento real.
- 🔵 El experimento de **Davisson-Germer** se menciona sin la condición de Bragg.
  Añadir $n\lambda=2d\sin\theta$ y un número concreto (54 eV → 0.167 nm).
- 🔵 Cerrar el tema con una tabla-resumen "observación / falla clásica / arreglo
  cuántico" para las cinco evidencias.

**Figuras (todas nuevas)** → `nb01_antecedentes.ipynb`
1. Distribución de Planck a 3-4 temperaturas + curva de Rayleigh-Jeans divergiendo (la catástrofe UV en una sola imagen). *Reemplaza y jubila `figs/planck.png`.*
2. Ley de desplazamiento de Wien: $\lambda_{max}$ vs $1/T$, recta.
3. $E_{cin}$ vs $\nu$ para dos metales: rectas paralelas de pendiente $h$, cortes en $\nu_0$ distintos.
4. Diagrama de niveles de Bohr con las series de Lyman/Balmer/Paschen dibujadas como flechas, y el espectro de líneas correspondiente.
5. $\lambda_{dB}$ frente a la masa (electrón → pelota de tenis) en escala log-log, para que se vea por qué no vemos difractar objetos macroscópicos.

---

### Tema 2 — Postulados (`tema02.tex`, 430 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 127 | Coordenadas esféricas: `z = \cos\theta` | `z = r\cos\theta` |
| 🟠 | 136 | Límite de integración `\int_\infty^\infty` | `\int_{-\infty}^{\infty}` |
| 🟠 | 235-239 | Postulado de la medida mal enunciado: *"el valor del observable en una serie de medidas es igual al valor promedio"*. Se salta lo esencial | reformular: **cada medida individual devuelve un autovalor** $\omega_k$; lo que es el valor esperado es la **media sobre muchas medidas**. Tal como está, el alumno concluye que una medida da $\langle\Omega\rangle$ |
| 🟠 | 228-229 | "Sus funciones propias son ortogonales" sin condición | sólo para **autovalores distintos**; si hay degeneración, se pueden ortogonalizar |
| 🟠 | 202 | `\begin{tabular}{lcr}` con sólo 2 columnas | `{ll}` |
| 🟠 | 353 | $(\Delta\Omega^2)$ | $(\Delta\Omega)^2$ |
| 🟠 | 341, 345 | "$\Delta x=0$", "$\Delta p=\infty$" para un paquete de ondas | son límites idealizados; escribir $\Delta x\to0$, $\Delta p\to\infty$ |
| 🟠 | 111-113 | La normalización mezcla $N$ y $\psi$: $N^2\int\psi^\star\psi\,dx=1$, pero después se usa $\psi$ ya normalizada | fijar un convenio y mantenerlo |
| 🟡 | 70 | `\section*{Estados y funciones de onda}` sin numerar mientras el resto sí | quitar el `*` |
| 🟡 | 238-239 | Comillas tipográficas `“ ”` en el fuente | ``` `` '' ``` |
| 🟡 | 165 | "Un ejemplo de operador, pueden ser el operador..." | concordancia |
| 🟡 | 101 | $|\psi(r)|^2d\tau$ escrito como *proporcional*, cuando ya está normalizado | "es igual a" |

**Mejoras**

- 🔵 **Numerar los postulados explícitamente** (I-VI) y ponerlos juntos en un
  recuadro al inicio, antes de desarrollarlos. Ahora están dispersos y el alumno
  no sabe cuántos son.
- 🔵 El postulado de Pauli (§ final) es en realidad un postulado *aparte* y se
  vuelve a contar entero en el Tema 7. Decidir dónde vive y dejar en el otro sitio
  sólo una referencia cruzada.
- 🔵 Falta un **ejemplo resuelto** en todo el tema. Añadir uno mínimo: normalizar
  $\psi=Ne^{-ax^2}$ y calcular $\langle x\rangle$, $\langle x^2\rangle$.
- 🔵 Falta la relación explícita $\langle\Omega\rangle=\int\psi^\star\hat\Omega\psi\,d\tau$
  como ecuación numerada — se menciona pero nunca se escribe.
- 🔵 Introducir aquí la **notación de Dirac** (ya está desarrollada en `math01`) y
  hacer la referencia cruzada.

**Figuras** → `nb02_postulados.ipynb`
1. Funciones de onda **aceptables vs no aceptables** (multivaluada, discontinua, derivada discontinua, no integrable) en un panel 2×2. Es la figura que más rentabiliza el §"requisitos".
2. $\psi$ y $|\psi|^2$ para un paquete gaussiano, con $\Delta x$ marcado.
3. Paquete de ondas: superposición progresiva de 1, 3, 10, 100 armónicas → localización creciente en $x$ y deslocalización en $k$. Es la demostración visual del principio de incertidumbre y ahora sólo está en palabras (líneas 334-347).
4. Par $\psi(x)$ / $\tilde\psi(k)$ mostrando $\Delta x\,\Delta k\ge 1/2$ para tres anchuras.

---

### Tema 3 — Sistemas modelo (`tema03.tex`, 525 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 172, 275 | $-\dfrac{\hbar}{2m}$ en el hamiltoniano — **falta el cuadrado** | $-\dfrac{\hbar^2}{2m}$. Dos sitios |
| 🔴 | 455 | $\alpha=(\hbar/mk)^{1/4}$ — dimensionalmente incorrecto | $\alpha=\left(\hbar^2/mk\right)^{1/4}$ (comprobación: $\hbar^2/mk$ tiene unidades de m⁴) |
| 🔴 | 132-134 | *"positiva y negativa se corresponden con la partícula desplazándose hacia la **izquierda** o hacia la **derecha**"* — **invertido**, y se contradice con la frase siguiente (línea 137-139, que sí es correcta) | $p_x=+k\hbar$ → hacia la derecha |
| 🔴 | 374 | Continuidad de la derivada en $x=0$: `A i k - B i k = C\kappa + D\kappa` | debe ser $C\kappa - D\kappa$ |
| 🔴 | 269 | Subsección titulada **"En tres dimensiones"** pero todo el desarrollo es **en dos** ($x$, $y$) | o se retitula "En dos dimensiones", o se extiende a 3D. Recomiendo extender: la degeneración en 3D es mucho más ilustrativa |
| 🟠 | 176-181 | La "demostración" de $\psi=0$ fuera de la caja mediante $\frac{1}{\infty}\frac{\partial^2\psi}{\partial x^2}=\psi$ no es matemáticamente admisible | sustituir por el argumento de límite: $V\to\infty$ con $E$ finita ⟹ $\psi\to0$; o tomar el pozo finito y hacer $V_0\to\infty$ |
| 🟠 | 329 | *"podemos usar la **función de partición** de la partícula libre"* | **función de onda** |
| 🟠 | 489-490 | Pie de tabla: "para diferentes valores del número cuántico $y$" | el número cuántico es $v$; $y$ es la variable |
| 🟠 | 61 | "principio de correspondencia de **Böhr**" | **Bohr**, sin diéresis (aparece 1 vez aquí; comprobar en todo el repo) |
| 🟠 | 247 | "La **energía residual** para $n=1$" | término estándar: **energía del punto cero** |
| 🟠 | 388 | `$R=|B^2|/|A^2|$` | $R=|B|^2/|A|^2$ |
| 🟠 | 314 | El efecto túnel está como `\subsection` **dentro** de "Partícula en una caja" | debe ser `\section` propia (barrera de potencial finita) |
| 🟡 | 73 | `\section*{}` vacía | borrar |
| 🟡 | 501-506 | Bloque de 6 líneas comentado sobre efecto túnel en el oscilador | decidir: recuperar o borrar |
| 🟡 | 82 | $E=1/2mv^2$ se lee como $\frac{1}{2m}v^2$ | usar `\frac{1}{2}mv^2` (recurrente en todo el repo) |
| 🟡 | 407 | "Asímismo" | *asimismo* (sin tilde). Aparece también en línea 123 |

**Mejoras**

- 🔵 Falta **el pozo de potencial finito** como sistema propio. Ahora se salta de
  la caja infinita al efecto túnel sin el caso intermedio, que es el que explica
  la penetración en la barrera.
- 🔵 Añadir el **argumento de escala**: $E_n\propto1/mL^2$ aplicado a un caso
  químico real (polienos conjugados, β-caroteno) — conecta el modelo con la
  espectroscopía UV-Vis que ya han visto.
- 🔵 Del oscilador armónico falta: la comparación con el **potencial de Morse**,
  y la conexión $\omega=\sqrt{k/\mu}$ con la espectroscopía IR (número de onda de
  la tensión C-H). Son dos párrafos y justifican todo el capítulo.
- 🔵 No se menciona el **teorema del virial** para el oscilador ($\langle T\rangle=\langle V\rangle$),
  que es un resultado que se pide en problemas.

**Figuras** → `nb03_sistemas_modelo.ipynb` — *el notebook con mayor retorno de todo el curso*
1. Caja 1D: $\psi_n$ y $|\psi_n|^2$ para $n=1..4$, desplazadas verticalmente sobre el diagrama de niveles $E_n$. La figura canónica que ahora no existe.
2. Límite clásico: $|\psi_n|^2$ para $n=1$, $n=20$, $n=50$ frente a la densidad clásica uniforme.
3. Caja 2D: mapas de calor de $\Psi_{n_1n_2}$ para (1,1), (1,2), (2,1), (2,2) mostrando la degeneración $E_{12}=E_{21}$.
4. Efecto túnel: paquete de ondas incidiendo sobre una barrera, con $\psi$ real en las tres regiones y el decaimiento exponencial dentro.
5. $T(E/V)$ para varias anchuras $L$ y masas (electrón vs protón) — cuantifica "más importante para partículas pequeñas".
6. Oscilador armónico: $\psi_v$ y $|\psi_v|^2$ para $v=0..4$ sobre la parábola, con los puntos de retorno clásicos marcados (se ve la penetración en la región prohibida).
7. $|\psi_v|^2$ para $v=20$ superpuesta a la densidad de probabilidad clásica $\propto1/\sqrt{E-V}$ — el principio de correspondencia, que ahora sólo está enunciado (líneas 507-509).

---

### Tema 4 — Momento angular (`tema04.tex`, 544 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 91 | `\bm{\omega}` sin `\usepackage{bm}` → **no compila** | añadir `bm` (o usar `\boldsymbol`) |
| 🔴 | 170-172 | $\hat{l}^2=\hbar^2\Lambda^2$ — **signo incorrecto** | $\hat{l}^2=-\hbar^2\Lambda^2$. Con el signo actual los autovalores salen negativos y contradice la ec. de la línea 245 y el resultado $E=l(l+1)\hbar^2/2I$ |
| 🔴 | 133-135 | $\hat{l}=\hat{l}_x+\hat{l}_y+\hat{l}_z$ — **suma escalar de componentes vectoriales** | $\hat{\mathbf{l}}=\hat{l}_x\mathbf{i}+\hat{l}_y\mathbf{j}+\hat{l}_z\mathbf{k}$ |
| 🔴 | 300 | Valores de $m_l$: "$\pm1,\pm2\ldots$" — **falta el 0** | $m_l=0,\pm1,\pm2,\ldots$ |
| 🔴 | 382 | "Las **$2m_l+1$** funciones de onda correspondientes al número cuántico $l$" | $2l+1$ |
| 🔴 | 450 | $-\dfrac{\hbar^2}{2m}\nabla^2_{cm}\psi_{cm}$ — masa equivocada | $-\dfrac{\hbar^2}{2M}$ (masa total) |
| 🟠 | 204 y 399 | **Etiqueta `eq:lz` duplicada** → los `\ref` apuntan mal | renombrar una |
| 🟠 | 275 y 475 | **Etiqueta `eq:rotor` duplicada** | ídem |
| 🟠 | 126-130 | *"El operador momento angular $\hat{l}$ no tiene funciones propias"* — impreciso | lo correcto: $\hat{l}_x,\hat{l}_y,\hat{l}_z$ no tienen autofunciones **comunes**; $\hat{l}^2$ y una componente sí |
| 🟠 | 162-166 | "no podemos especificar más de una componente" | matizar: si $l=0$, las tres son simultáneamente 0 |
| 🟠 | 114 | $E=1/2I\omega^2=L^2/2I$ mezcla $l$ minúscula y $L$ mayúscula | unificar |
| 🟠 | 485 | $B=h/(8\pi^2I)$ — correcto en Hz, pero se suele tabular en cm⁻¹ | dar también $\tilde{B}=h/(8\pi^2cI)$ |
| 🟡 | 72 | "contrapartida **translacional**" | *traslacional* (recurrente: también 118, 191 de tema09) |
| 🟡 | 77-87 | Bloque de 11 líneas comentado sobre el torque | recuperar o borrar |
| 🟡 | 365 | Fila `... & &` suelta al final de la tabla | limpiar |

**Mejoras**

- 🔵 Falta por completo el **rotor rígido en 2D** (partícula en un anillo) como
  paso previo. Es el sistema donde la cuantización de $m_l$ sale de forma
  transparente y donde las condiciones de contorno cíclicas se entienden.
- 🔵 No aparecen los **operadores escalera** $\hat{l}_\pm$. Aunque no se examinen,
  una nota al margen explica de dónde salen los $2l+1$ valores de $m_l$, que ahora
  se postulan sin más.
- 🔵 Falta la conexión con **espectroscopía rotacional**: reglas de selección
  $\Delta J=\pm1$, espaciado $2B$ entre líneas, y un número real (HCl, $B\approx10.6$ cm⁻¹).
  Es la aplicación química del capítulo entero.
- 🔵 El modelo vectorial (conos de precesión) se describe en texto pero no se
  formaliza: $|\mathbf{l}|=\sqrt{l(l+1)}\hbar > l\hbar = l_z^{max}$, es decir, el
  vector **nunca** se alinea con $z$. Merece un párrafo explícito.

**Figuras** → `nb04_momento_angular.ipynb`
1. **Modelo vectorial**: conos de precesión para $l=2$, con las 5 orientaciones de $m_l$ y $|\mathbf{l}|=\sqrt6\hbar$ dibujado a escala frente a $l_z^{max}=2\hbar$.
2. Armónicos esféricos reales $|Y_{l,m}|$ para $l=0,1,2$ como superficies 3D coloreadas por fase — sustituye a la Tabla 1, que sin dibujo no dice nada.
3. Mapas de $|Y_{l,m}|^2$ en proyección $(\theta,\phi)$ mostrando el número de nodos frente a $l$ y $m$ (la afirmación de las líneas 345-349, hoy sólo en palabras).
4. Niveles del rotor rígido $E_J=BJ(J+1)$ con degeneración $2J+1$, más el espectro de absorción resultante (líneas igualmente espaciadas $2B$) — sirve también para el punto 🔵 anterior.

---

### Tema 5 — Átomo de hidrógeno (`tema05.tex`, 469 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 84 | Tabla de unidades atómicas: $a_0 = 5.291\text{e}{-10}$ m | **5.291×10⁻¹¹ m** (error de un orden de magnitud) |
| 🔴 | 188 | "resulta en la presencia de $(n-l)$ nodos" | los nodos **radiales** son $n-l-1$; los angulares, $l$; total $n-1$ |
| 🔴 | 440 | $\int\alpha^\star\beta\,d\sigma=\int\beta^\star\alpha\,d\sigma=\mathbf{1}$ | **= 0** (es la condición de ortogonalidad; tal como está contradice la línea 445) |
| 🔴 | 203 | `\bigg(\frac{Z}{a})^{3/2}` — **delimitador sin cerrar** en la fila 3s de la tabla | `\bigg(\frac{Z}{a}\bigg)^{3/2}` |
| 🔴 | 133 | *"las funciones de onda hidrogenoides, denominadas **orbitales de Mulliken**"* | no existe tal denominación. Son **orbitales atómicos**; lo que se debe a Mulliken es el **término "orbital"** (1932). Reescribir como nota al margen |
| 🟠 | 80-85 | Toda la tabla usa `1.602e$^{-19}$`, que se compone como *1.602e⁻¹⁹* | `$1.602\times10^{-19}$` en las 6 filas |
| 🟠 | 83 | Fila "Constante eléctrica": **falta un `&`** en una tabla de 4 columnas | añadir la celda vacía |
| 🟠 | 249-250 | "Las contribuciones al momento angular no pueden determinar con precisión" | *no se pueden determinar* |
| 🟠 | 252, 390 | Se usa $m$ donde el resto del texto usa $m_l$ | unificar a $m_l$ |
| 🟠 | 380 | Magnetón de Bohr como `\beta_B` y `9.3e-24` | símbolo estándar $\mu_B$; $9.274\times10^{-24}$ J·T⁻¹ |
| 🟠 | 264 | "con lo cual **el un** átomo hidrogenoide" | typo |
| 🟠 | 209-211 | La llave del `\caption` cierra antes del punto y deja `%` y texto suelto | limpiar |
| 🟠 | 426 | "Goudsmith" | **Goudsmit** (George Uhlenbeck y Samuel Goudsmit) |
| 🟠 | 291-297 | Se dan dos expresiones para $P(r)$ presentándolas como "general" y "no esférica", pero $P(r)=r^2R^2$ es **la** general y $4\pi r^2\psi^2$ es el caso $l=0$ | invertir la presentación |
| 🟡 | 269 | `Tabla~\n\ref{...}` con salto de línea dentro del `~` | corregir |
| 🟡 | 404 | Compton era estadounidense, "físico americano" | *estadounidense* |
| 🟡 | 316-323 | Bloque comentado de 8 líneas sobre orbitales p | recuperar (es contenido útil) o borrar |

**Mejoras**

- 🔵 El **efecto Zeeman anómalo** se insinúa (líneas 394-400: "sí se pueden
  observar dos bandas") pero no se nombra ni se explica. Cerrar el círculo o
  decir explícitamente que se resuelve con el espín, que es el §siguiente.
- 🔵 Falta el **acoplamiento espín-órbita** y la estructura fina, aunque sea
  cualitativamente. Es el puente natural hacia los términos espectroscópicos
  (el tema 8 ausente).
- 🔵 Los **orbitales reales** ($p_x,p_y$ como combinaciones de $Y_1^{\pm1}$) no
  aparecen nunca, y sin embargo el Tema 10 los usa continuamente para la
  hibridación. Hay que introducirlos aquí.
- 🔵 Falta $\langle r\rangle_{n,l}=\frac{a_0}{Z}\left[\frac{3n^2-l(l+1)}{2}\right]$
  y su contraste con $r_{max}$ — se dice que para 2s el máximo está en $5.2a_0$
  pero no se distingue radio más probable de radio medio.
- 🔵 Añadir la energía en eV ($-13.6\,Z^2/n^2$) junto a la expresión SI: es la
  forma con la que el alumno va a trabajar.

**Figuras** → `nb05_hidrogeno.ipynb` — *el segundo notebook prioritario*
1. $R_{n,l}(r)$ para 1s, 2s, 2p, 3s, 3p, 3d: se ven los nodos radiales y se corrige visualmente el error de la línea 188.
2. Funciones de distribución radial $r^2R^2$ para las mismas, con $r_{max}$ y $\langle r\rangle$ marcados. Muestra la **penetración** de 2s frente a 2p (que se necesita en el Tema 7).
3. Cortes 2D de $|\psi|^2$ para 1s, 2s, 2p$_z$, 3d$_{z^2}$, 3d$_{xy}$ con la fase en color.
4. Isosuperficies 3D de los orbitales reales s, p, d.
5. Diagrama de niveles $-13.6/n^2$ con la degeneración $n^2$ explícita.
6. Desdoblamiento Zeeman: $E$ vs $B_z$ para un nivel $l=1$ abriéndose en 3 ramas.
7. Esquema Stern-Gerlach: predicción clásica (banda continua) vs observación (dos manchas).

---

### Tema 6 — Métodos aproximados (`tema06.tex`, 623 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 374, 378, 379, 389, 394, 398, 399, 414 | `\psi_0^{(0)}^\star` → **doble superíndice, no compila** (8 apariciones) | `{\psi_0^{(0)}}^\star` o mejor definir `\newcommand{\psic}[2]{\psi_{#1}^{(#2)\star}}` |
| 🔴 | 547 | $E(\zeta)=\frac{m_ee^4}{16\pi^2\epsilon_0^2\hbar^2}$ — **no depende de $\zeta$**, y a continuación se pide $dE/d\zeta=0$ | debe ser $E(\zeta)=\left(\zeta^2-\tfrac{27}{8}\zeta\right)E_h$, de donde $\zeta_{opt}=27/16=1.6875$ y $E=-2.8477\,E_h$ |
| 🔴 | 543 | $\psi_{1s}=\left(\frac{\zeta^3}{\pi a_0}\right)^{1/2}$ | $\left(\frac{\zeta^3}{\pi a_0^3}\right)^{1/2}$ |
| 🔴 | 583 | $r_{12}=(r_1+r_2-2r_1r_2\cos\theta)^{1/2}$ — **faltan los cuadrados** | $r_{12}=(r_1^2+r_2^2-2r_1r_2\cos\theta)^{1/2}$ |
| 🔴 | 338, 340 | En el desarrollo de $\lambda^2$: el tercer término es `\hat{H}^{(2)}\psi^{(0)}` **repetido** | debe ser $\hat{H}^{(0)}\psi^{(2)}$ (y en el miembro derecho, $E^{(0)}\psi^{(2)}$) |
| 🔴 | 363 | $\hat{H}^{(1)}\psi_0^{(0)} + \hat{H}^{(1)}\psi_0^{(1)}$ | el segundo es $\hat{H}^{(0)}\psi_0^{(1)}$ |
| 🟠 | 335 | `\lambda\psi^{(1)} +  + \lambda\psi^{(2)}` — doble `+` y exponente mal | `+\lambda^2\psi^{(2)}` |
| 🟠 | 525-527 | *"$E_h$ es la energía del estado fundamental del átomo de hidrógeno"* — **falso** | $E_h$ es el **hartree**; el estado fundamental del H es $-\tfrac12 E_h$. La fórmula que se da sí es la del hartree. Además falta cerrar el paréntesis |
| 🟠 | 206 | $S_{ji}=\int\varphi^\star\varphi\,d\tau$ sin subíndices | $S_{ji}=\int\varphi_j^\star\varphi_i\,d\tau$ |
| 🟠 | 236-242 | El denominador pasa de $c_1^2+c_2^2+2c_1c_2S_{12}$ (implica $S_{11}=S_{22}=1$) a reintroducir $S_{11},S_{22}$ | fijar un convenio |
| ✅ | 541 | ~~"un parámetro variacional, $Z$" y a continuación se usa $\zeta$~~ | **corregido en Overleaf** |
| 🟠 | 490-493 | $m_{e1}$, $m_{e2}$ como masas distintas | ambos son $m_e$ |
| 🟠 | 601, 606 | "Perturbación 2º orden" da $-2.9077$ en la tabla y $-2.908$ en el texto; etiqueta `tab:my_label` | unificar cifras y renombrar la etiqueta |
| 🟠 | 72 | Teorema variacional enunciado como *"siempre superior"* | **mayor o igual** (la igualdad sólo si $\psi=\psi_0$, como se dice después) |
| 🟡 | 135-181 | **47 líneas comentadas** con el ejemplo variacional del oscilador armónico — que es justo el ejemplo trabajado que falta | **recuperarlo**: es contenido de calidad ya escrito |
| 🟡 | 418-475 | Otras **58 líneas comentadas** (método de Rayleigh-Schrödinger) | decidir |
| 🟡 | 94 | "hamiltoniano , de tal manera" | espacio antes de coma |
| 🟡 | 359-360 | "La segunda ecuación\n, correspondiente" | ídem |
| 🟡 | 156, 547, 579 | Mezcla `\epsilon_0` y `\varepsilon_0` | unificar (`\varepsilon_0`) |

**Mejoras**

- 🔵 **Recuperar el ejemplo del oscilador armónico comentado** (líneas 135-181):
  es el único ejemplo completamente resuelto del método variacional simple y está
  bien hecho. Sin él, el §"método variacional simple" son 5 viñetas abstractas.
- 🔵 El método de variaciones lineal se desarrolla para $N=2$ pero no se conecta
  con que **eso es exactamente lo que se hará en el Tema 9** (H₂⁺, LCAO) y en el
  Tema 10 (Hückel). Añadir la referencia cruzada explícita: es la misma ecuación
  secular tres veces.
- 🔵 Falta señalar que el teorema variacional **sólo acota el estado fundamental**;
  para excitados hace falta ortogonalidad a los inferiores.
- 🔵 Falta mencionar que la corrección de segundo orden es **siempre negativa**
  para el fundamental (todos los $E_0-E_n<0$) — resultado que se pide en examen.

**Figuras** → `nb06_metodos_aproximados.ipynb`
1. $E(\lambda)$ del ejemplo variacional del oscilador, con el mínimo marcado y la energía exacta como línea horizontal: se ve el 14% de sobrestimación.
2. $E(\zeta)$ del helio con $\zeta_{opt}=1.6875$, y las funciones $\psi_{1s}$ para $\zeta=1$, $1.69$, $2$ superpuestas — visualiza el apantallamiento.
3. Barras comparativas de las cinco energías de la Tabla (exp., sin $H_{12}$, variacional, PT1, PT2) frente al valor experimental.
4. Sistema de dos niveles: $E_\pm$ frente a $H_{12}$, mostrando la repulsión de niveles ("avoided crossing"). Es la figura que hace intuitiva la ecuación secular 2×2 y reaparece idéntica en los Temas 9 y 10.
5. Corrección perturbativa a la caja con un escalón $V_0$ (el problema 4 de `exercises02`): $\psi^{(0)}$, la perturbación y $E_n^{(1)}$ frente a $n$.

---

### Tema 7 — Átomos polielectrónicos (`tema07.tex`, 485 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| ✅ | 343 | ~~$E=2h_{1s}+J_{1s,2s}\pm K_{1s,2s}$ para el primer excitado~~ | **corregido en Overleaf**: ahora $h_{1s}+h_{2s}+J\pm K$ |
| 🔴 | 354-363 | Párrafo del **hueco de Fermi autocontradictorio**: dice que $\Psi_t$ (espacial antisimétrica = **mismo** espín) tiene corrección $J-K$, "mientras que es desfavorable cuando los electrones tienen **el mismo espín** ($J+K$)" | triplete (mismo espín, espacial antisimétrica) → $J-K$; singlete (espines opuestos) → $J+K$. Reescribir el párrafo entero |
| 🔴 | 166-172 | Los orbitales se llaman $\psi_\alpha$ y $\psi_\beta$ **a la vez** que $\alpha,\beta$ son las funciones de espín (líneas 152-153, 246-257). Colisión de notación grave | renombrar los orbitales a $\psi_a$, $\psi_b$ |
| 🟠 | 65 | El documento **empieza con `\subsection`** sin `\section` previa → numeración "0.1" | promover a `\section` |
| 🟠 | 138 | $\Psi_s(\mathbf{r}_1,\mathbf{r}_2)=\Psi(\mathbf{r}_2,\mathbf{r}_1)$ — falta el subíndice en el miembro derecho | $\Psi_s(\mathbf{r}_2,\mathbf{r}_1)$ |
| 🟠 | 387-388 | "Para una misma capa (mismo $n$) la energía de las subcapas (**mismo $l$**)" | las subcapas de una misma capa tienen **distinto** $l$ |
| 🟠 | 305-306 | `\bra{1s(1)}\hat{h}_1\ket{1s(1)}\braket{1s(2)}` — `\braket` de un solo argumento, y el segundo término repite el índice 1 | reescribir: $\langle 1s(2)|1s(2)\rangle$ |
| 🟠 | 126 | "principio de exclusión introducido por Pauli en **1924**" | **1925** (Pauli, enero de 1925) |
| 🟠 | 373 | `Z_{ef}` en itálica | `Z_{\mathrm{ef}}` |
| 🟠 | 467-469 | "Las energías $\varepsilon$ son equivalentes a las energías de ionización" | es el **teorema de Koopmans**: $I\approx-\varepsilon$. Nombrarlo e indicar el signo y que es una aproximación (cancelación de errores) |
| 🟠 | 232-237 | El determinante de Slater se escribe con **electrones en filas**, y en tema09 (línea 567) con **electrones en columnas** | unificar el convenio entre capítulos |
| 🟡 | 105 | Comillas tipográficas `“propio”` en el fuente | ``` `` '' ``` |
| 🟡 | 155 | "la funcion de onda" | *función* |
| 🟡 | 157 | `\updownarrows` para "apareados" y en línea 411 `\upuparrows` para "paralelo" | correcto, pero requiere `mathabx`: comprobar tras unificar preámbulo |

**Mejoras**

- 🔵 Falta el enunciado **"forma débil"** de Pauli (no dos electrones con los
  cuatro números cuánticos iguales) *derivado* del determinante — se enuncia
  (línea 146) antes de demostrarlo (línea 232). Reordenar.
- 🔵 La **regla de Hund** se enuncia sólo en su primera parte (máxima
  multiplicidad). Faltan las reglas 2ª y 3ª ($L$ máximo, $J$), que son las que
  conectan con los términos espectroscópicos del tema 8 ausente.
- 🔵 Las **reglas de Slater** para calcular $\sigma$ no aparecen. Son un cálculo
  concreto y examinable que hace tangible todo el §apantallamiento.
- 🔵 Falta cualquier dato numérico: energías de ionización de la 2.ª fila para
  ilustrar penetración/apantallamiento y las anomalías (B<Be, O<N).
- 🔵 Del método Hartree-Fock falta la **energía de correlación**
  ($E_{corr}=E_{exacta}-E_{HF}$) — la limitación esencial del método, en una línea.

**Figuras** → `nb07_polielectronicos.ipynb`
1. Densidades de probabilidad $|\Psi_s|^2$ y $|\Psi_a|^2$ frente a $(x_1,x_2)$ como mapas de calor: se ve el **hueco de Fermi** en la diagonal $x_1=x_2$. Es la figura que arregla el error 🔴 de las líneas 354-363, que hoy sólo está en palabras contradictorias.
2. Distribuciones radiales de 2s y 2p superpuestas al 1s, con la penetración del 2s en la zona interna sombreada.
3. Diagrama de niveles comparado: hidrogenoide (degenerado en $l$) vs polielectrónico (s<p<d<f).
4. Energías de ionización frente a $Z$ para los 20 primeros elementos, con las anomalías anotadas.
5. Diagrama de flujo del ciclo SCF de Hartree-Fock.
6. Singlete/triplete del He: niveles con la separación $2K$ marcada.

---

### Tema 8 — AUSENTE

- 🔴 **Decisión requerida antes de seguir.** Dos opciones:
  - **(a)** Escribirlo: *Términos espectroscópicos y acoplamiento
    Russell-Saunders* — microestados, $L$, $S$, $J$, símbolos $^{2S+1}L_J$, reglas
    de Hund completas, reglas de selección. Encaja perfectamente entre el 07
    (configuraciones) y el 09 (moléculas), y es lo que las tres reglas de Hund del
    tema 7 están pidiendo.
  - **(b)** Renumerar `tema09→tema08`, `tema10→tema09` y actualizar las
    referencias cruzadas.

  Mi recomendación es **(a)**: sin él, el salto de "configuración electrónica" a
  "enlace químico" deja fuera toda la espectroscopía atómica.
- 🔵 Figuras si se escribe: tabla de microestados de $p^2$ construida
  gráficamente; diagrama de desdoblamiento configuración → términos → niveles
  ($^3P_{0,1,2}$) → Zeeman; diagrama de Grotrian del sodio con el doblete D.

---

### Tema 9 — Moléculas diatómicas (`tema09.tex`, 690 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
> Números de línea **actualizados al estado post-sync** (`87b19c7`). El capítulo
> se reescribió a fondo (499 líneas modificadas) y cinco de mis hallazgos ya
> están resueltos.

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| ✅ | preámbulo | ~~`mathabx` + `physics` → no compila~~ | **arreglado**: `mathabx` comentado, `braket` añadido |
| ✅ | — | ~~Signo menos Unicode (U+2212)~~ | **eliminado** |
| ✅ | 508 | ~~"no más de **un** electrón puede ocupar un orbital"~~ | **reescrito** correctamente |
| ✅ | 541 | ~~"desestabilización del antienlazante > estabilización del **antienlazante**"~~ | **ahora "del enlazante"** |
| ✅ | — | ~~"se asume que se asume"~~ / ~~"inpar"~~ | **corregidos** |
| 🔴 | **402** | "En el caso del **H$^+$**" | **H$_2^+$** — sigue en pie |
| 🟠 | **132, 169** | $\sum_{A=1}^M\sum_{A>B}^M$ — índice mudo mal puesto | $\sum_{A=1}^{M}\sum_{B>A}^{M}$ — sigue en pie |
| 🟠 | **337** | Configuración del N: `2s$^2$2p$_x^1$p$_y^1$p$_z^1$` — faltan los "2" | `2s$^2$2p$_x^1$2p$_y^1$2p$_z^1$` — sigue en pie |
| 🟠 | **587** | "FCl" | **ClF** — sigue en pie |
| 🟠 | **540** | "La configuración resultante es $1\sigma_g^2$ y $1\sigma_u^2$" | $1\sigma_g^2 1\sigma_u^2$ |
| 🟠 | ~136 | Se define $r_{AB}$ pero en las ecuaciones se usa $R_{AB}$ | unificar (reverificar líneas) |
| 🟠 | ~90 | "(el catión H$_2^+$ hay que resolver" — paréntesis sin cerrar | reverificar |
| 🟠 | ~115 | $D_o$ y $D_e$ mencionados sin distinguirlos | $D_0=D_e-\tfrac12\hbar\omega$; usar $D_0$ |
| 🟠 | — | Mezcla $\psi_A$ / $1s_A$ / $\chi_A$ para lo mismo | unificar |
| 🟡 | — | Bloques comentados (Born-Oppenheimer alternativo, CO) | reverificar si sobreviven |

**⚠️ Pendiente de revisar en este capítulo:** el nuevo apéndice *"Derivación de
las ecuaciones de la energía para el H$_2^+$"* y la nueva `\subsection`
*"Moléculas diatómicas homonucleares y configuraciones electrónicas"*.

**Mejoras**

- 🔵 **Falta el orden de enlace** como fórmula: $b=\tfrac12(n-n^\star)$. Se usa el
  concepto ("orden de enlace 3" en N₂, línea 357) sin definirlo nunca.
- 🔵 **Falta la mezcla s-p** y la inversión del orden $\sigma_g/\pi_u$ entre
  N₂ y O₂. El §"Moléculas homonucleares del segundo periodo" termina diciendo
  "formamos ocho orbitales moleculares" y **se corta ahí** — no llega a construir
  el diagrama ni a discutir el paramagnetismo del O₂, que es el argumento estrella
  de la teoría de OM.
- 🔵 Falta la tabla de **configuración / orden de enlace / longitud / energía de
  enlace / magnetismo** para Li₂…F₂. Es la validación experimental del capítulo.
- 🔵 En la teoría de enlace de valencia, falta la **corrección iónica-covalente**
  (los términos que Heitler-London descartan en la línea 268 sí importan) y el
  concepto de resonancia, que reaparece en el Tema 10 con el benceno.
- 🔵 Falta explicar por qué la teoría OM **falla en la disociación** de H₂ (la
  configuración $\sigma_g^2$ contiene un 50% de carácter iónico a $R\to\infty$).
  Se menciona la CI como solución (línea 580) sin explicar el problema.

**Figuras** → `nb09_diatomicas.ipynb` — *el tercer notebook prioritario*
1. Curva de energía potencial molecular con $R_e$, $D_e$, $D_0$ y el nivel de punto cero marcados. Aclara la confusión $D_e$/$D_0$ de las líneas 115-116.
2. $\sigma_g$ y $\sigma_u$ del H₂⁺: $\psi$ a lo largo del eje internuclear y $|\psi|^2$, con la acumulación/deplección de densidad internuclear sombreada.
3. Mapas 2D de densidad electrónica del enlazante y del antienlazante, con el plano nodal.
4. $E_{1\sigma}(R)$ y $E_{2\sigma}(R)$ frente a $R$ en la misma gráfica, mostrando que el antienlazante sube más de lo que el enlazante baja.
5. Diagramas de correlación de OM completos para B₂→F₂, **con la inversión s-p entre N₂ y O₂** — figura central que hoy no existe ni en texto.
6. Diagrama de OM del HF, asimétrico, con los coeficientes proporcionales al tamaño de los lóbulos.

---

### Tema 10 — Moléculas poliatómicas (`tema10.tex`, 312 líneas)

**Correcciones**

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 241-243 | Determinante secular con `\alpha_A - ES` en la **diagonal** | debe ser $\alpha_A-E$ (ya que $S_{AA}=1$); sólo los términos **fuera** de la diagonal llevan $\beta-ES$. Además contradice las ecuaciones seculares de las líneas 231-232, que sí están bien |
| 🔴 | 283-287 | Determinante de Hückel con `\alpha-ES` | en Hückel se asume $S=0$: debe ser $\alpha-E$ en la diagonal y $\beta$ fuera |
| 🔴 | 112-115 | *"los cuatro enlaces del metano son idénticos, mientras que el concepto de **hibridación** sugeriría tres enlaces idénticos y uno diferente"* — invertido: eso es lo que sugiere la **promoción** | es la promoción la que da el problema y la hibridación la que lo resuelve (como dice la frase siguiente). Reescribir |
| 🟠 | 180 | "1.39 {\AA} y todos los ángulos" — **paréntesis sin abrir/cerrar** | corregir; y usar `\r{A}` o `\AA` de forma consistente |
| 🟠 | 198, 201, 202, 212 | "**Las** orbitales moleculares", "estas orbitales", "una orbital molecular" | *los/estos/un* orbital(es). 4 apariciones |
| 🟠 | 213 | "orbitales atómicos $A$ **and** $B$" | *y* |
| 🟠 | 260-261 | "capaz de tratar **sin sin** dificultad" | duplicado |
| 🟠 | 292 | Energías de Hückel del butadieno: $\pm1.62$, $\pm0.62$ | $\pm1.618$, $\pm0.618$ (números áureos); dar al menos 3 cifras |
| 🟠 | 248 | $E=\frac{\alpha\pm\beta}{1\pm S}$ sin decir qué signo corresponde a cuál | especificar: enlazante $(\alpha+\beta)/(1+S)$ |
| 🟠 | 95 | Configuración del C `(2s$^2$2p$^1_x$2p$_y^1$)` sin el core | `[He]2s$^2$2p$_x^1$2p$_y^1$` |
| 🟠 | 141 | "un electrón del orbital 2s **promueve** a uno de los orbitales p" | *se promueve* / *promociona* |
| 🟠 | 85, 89, 129, 181 | Grados escritos como `90$^o$`, `104.5º`, `109.47º`, `120º` — tres formas distintas | unificar con `\si{\degree}` o `$^\circ$` |
| 🟡 | 135 | $\sigma_\mathrm{C-H}$ sin normalizar | añadir el factor |
| 🟡 | 190 | "Se puede representar por dos estructuras de Lewis" — sujeto perdido | "El benceno se puede…" |

**Mejoras**

- 🔵 **Falta la comprobación de ortonormalidad de los híbridos** — que los cuatro
  $h_i$ de sp³ son ortogonales entre sí y que el ángulo sale 109.47°. Es un
  cálculo de tres líneas con el producto escalar y justifica los coeficientes, que
  ahora aparecen caídos del cielo.
- 🔵 Falta el tratamiento de **OM del H₂O por simetría** (orbitales adaptados,
  $a_1/b_1/b_2$, diagrama de Walsh). El capítulo introduce la teoría de OM
  poliatómica y luego sólo hace Hückel-π. El H₂O es el contraejemplo obligado a
  la hibridación.
- 🔵 Hückel: falta la **energía de deslocalización** calculada
  ($4\alpha+4.472\beta$ vs $4\alpha+4\beta$ para el butadieno = $0.472\beta$).
  Se afirma que "el método es capaz de explicar la estabilización adicional"
  (líneas 294-296) sin dar el número.
- 🔵 Falta el benceno resuelto por Hückel ($\alpha\pm2\beta$, $\alpha\pm\beta$
  doblemente degenerados) y la **regla de Hückel 4n+2**, que es la razón por la
  que un químico usa este método.
- 🔵 Falta la conexión **HOMO-LUMO ↔ espectro UV-Vis** de polienos: cierra el
  curso conectando con el Tema 3 (partícula en una caja aplicada a polienos).
- 🔵 Este tema es notablemente **más corto y menos formal** que los demás (312
  líneas, casi todo prosa). Merece equilibrarse.

**Figuras** → `nb10_poliatomicas.ipynb`
1. Los cuatro híbridos sp³ dibujados en 3D en geometría tetraédrica; ídem sp² (trigonal plana) y sp (lineal).
2. Construcción de un híbrido: $s+p_z$ representados por separado y su suma, mostrando la interferencia constructiva/destructiva que direcciona el orbital.
3. Diagrama de OM del H₂O por simetría + diagrama de Walsh (energía vs ángulo H-O-H, con el mínimo en ~104°).
4. Hückel del butadieno: niveles $\alpha\pm1.618\beta$, $\alpha\pm0.618\beta$ con los coeficientes dibujados como círculos de área proporcional y fase en color.
5. Hückel del benceno: diagrama de Frost y los seis OM π.
6. HOMO-LUMO frente al número de dobles enlaces conjugados, junto a $\lambda_{max}$ experimental de los polienos.

---

### `math01.tex` — Laboratorio Matemáticas 1: Vectores (341 líneas)

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🔴 | 335-339 | `\bibliographystyle{plainnat}` **dentro** de `thebibliography` → error natbib, **no compila** | sacarlo fuera, o eliminar natbib |
| 🔴 | 56, 251 | `Schr\=odinger` → compone *Schr̄odinger* | `Schr\"odinger` (2 apariciones) |
| 🟠 | 299, 305, 327 | `\braket{f(x)^\star}{g(x)}` — **el bra ya conjuga**; poner $\star$ dentro es incorrecto | `\braket{f}{g}` (3 apariciones) |
| 🟠 | 243 | $|f(x)|^2=\braket{f}{f}$ — confunde el módulo puntual con la norma | usar $\lVert f\rVert^2$ |
| 🟠 | 171, 173 | Mezcla `\braket{A}{B}` y `\bra{A}\ket{B}` | unificar |
| 🟠 | 320 | "una componentes del vector" | concordancia |
| 🟠 | 263 | "Números **de de** este tipo" | duplicado |
| 🟠 | 136 | "Estas propiedades nos **permite**" | concordancia |
| 🟠 | 293-294 | $|A|=\sqrt{\vec A\cdot\vec A}$ escrito con conjugados: para vectores complejos $\vec A\cdot\vec A\ne\lVert A\rVert^2$ | usar la notación de producto interno $\braket{A}{A}$ |

**Mejoras**

- 🔵 Falta **todo el bloque de matrices**: producto, determinante, autovalores y
  autovectores. Los Temas 6, 9 y 10 resuelven determinantes seculares sin que
  exista ningún sitio donde se haya explicado qué es un determinante secular.
  **Este es el hueco más importante del material de apoyo.**
- 🔵 Falta la **fórmula de Euler** y la exponencial compleja, que se usa desde la
  primera página del Tema 3.
- 🔵 Falta un repaso de **ecuaciones diferenciales de 2.º orden** con coeficientes
  constantes (justamente la ec. de Schrödinger de la caja y la partícula libre).
- 🔵 Falta el **conjunto completo / desarrollo en base ortonormal**, que es la
  formalización de la superposición del Tema 2.

**Figuras** → `nbM1_vectores.ipynb`
1. Proyección de $\vec B$ sobre $\vec A$ con el ángulo $\theta$: el producto escalar visualizado.
2. La transición vector→función: barras de $N=3,10,50,\infty$ componentes hasta convertirse en una curva continua (la idea central de las líneas 191-214, hoy sólo verbal).
3. Plano complejo con $z$, $z^\star$, $|z|$ y la interpretación de $e^{i\theta}$.
4. Dos funciones ortogonales y dos no ortogonales, con el área $\int f g$ sombreada en positivo y negativo.

---

### `math02.tex` — Laboratorio Matemáticas 2: Ondas (71 líneas)

- 🔴 Línea 16: una **URL de Overleaf pegada dentro del `\title`**
  (`\tithttps://www.overleaf.com/project/64fae9a08351c9f6abbd5772le[...]`) →
  no compila.
- 🔴 El documento está **vacío**: `abstract` en blanco y una `\section{Fundamentos}`
  sin contenido.
- 🔵 Contenido propuesto (es el complemento natural de `math01` y da soporte a los
  Temas 1-3): ondas armónicas, $\lambda$, $k$, $\nu$, $\omega$, velocidad de fase
  y de grupo; ecuación de ondas clásica y su relación con la de Schrödinger;
  superposición e interferencia; paquetes de onda y ancho de banda
  ($\Delta x\,\Delta k\ge1/2$ como resultado **puramente ondulatorio**, antes de
  llamarlo Heisenberg); ondas estacionarias y condiciones de contorno →
  cuantización.
- 🔵 Figuras: onda viajera animada; suma de dos ondas de frecuencias próximas
  (batidos, fase vs grupo); construcción de un paquete gaussiano; modos
  estacionarios de una cuerda fija comparados con la partícula en una caja
  (misma matemática, y sirve de gancho para el Tema 3).

---

### Hojas de problemas ⚠️ SECCIÓN OBSOLETA TRAS LA SINCRONIZACIÓN

> Esta sección se escribió contra las **dos** hojas de diciembre de 2023. Ahora
> hay **seis** en `ejercicios/`, y las antiguas se renombraron:
> `exercises01 → ejercicios_02`, `exercises02 → ejercicios_06`, ambas además
> modificadas (−83 y ±34 líneas). Las hojas 01, 03, 04 y 05 son nuevas y **no
> las he leído**. Los hallazgos de abajo hay que reverificar uno por uno; mi
> crítica *"no hay hojas para los temas 7, 9 y 10"* es probablemente obsoleta.

**`exercises01.tex` → ahora `ejercicios/ejercicios_02.tex`** (temas 1-4, 14 problemas)

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🟠 | 157 | Solución 5: "(a) No. **(d)** No. (c) Sí. (d) No. (e) Sí." — apartado **(b) etiquetado como (d)** | "(a) No. (b) No. (c) Sí. (d) No. (e) Sí." |
| 🟠 | 107 | Enunciado 8: "calcular el **valor propio** de $x$" cuando lo que se calcula (y se responde) es el valor **medio** | *valor esperado / valor medio* |
| 🟠 | 160-161 | Solución 8: la constante de normalización `N=(\frac{2}{\sqrt{\pi/(2a)^3}})^{1/2}` está confusa y mezcla $a$ con $\alpha$ | rehacer y unificar el símbolo |
| 🟠 | 164 | "$p_x^2$" donde debe ir $\langle p_x^2\rangle$; "nos hace **faltan**" | corregir |
| 🟡 | 130 | "el **especiamiento** entre dos niveles" | *espaciamiento* |
| 🟡 | 124 | "**Evalua**" | *Evalúa* |
| 🟡 | 151 | `\subsection{\textbf{Soluciones:}}` | `\section*{Soluciones}` |

*Verificados numéricamente y correctos:* problemas 1, 2, 3, 10, 12, 13.

**`exercises02.tex`** (temas 5-6, 5 problemas)

| Sev | Línea | Problema | Corrección |
|---|---|---|---|
| 🟠 | 65 | Potencial: "$\infty$ si $L<x<0$" — **intervalo vacío** | `si $x<0$ o $x>L$` |
| 🟠 | 89 | Solución 3: "2p: No tiene nodos (excepto $r=0$)" | $r=0$ **no** es un nodo radial de 2p (la función se anula ahí por el factor $\rho^l$, no por un cambio de signo). Precisar |
| 🟡 | 68 | `V_0,` con coma sobrante dentro del `cases` | limpiar |
| 🟡 | 85 | `\subsection{\textbf{Soluciones:}}` | ídem que arriba |

**Mejoras generales de problemas**

- 🔴 **No hay hojas para los temas 7, 9 y 10** (ni 8). Hay que crear
  `exercises03` (átomos polielectrónicos + términos) y `exercises04` (moléculas:
  orden de enlace, diagramas de OM, Hückel del butadieno y el benceno).
- 🔵 Las soluciones son sólo el **resultado final**. Para al menos 2-3 problemas
  por hoja, añadir el desarrollo completo.
- 🔵 Marcar cada problema con el **tema y la dificultad**, y añadir problemas de
  respuesta corta/conceptual (ahora son casi todos numéricos).
- 🔵 🔵 Cada hoja podría tener un **notebook de soluciones** que reproduzca los
  cálculos numéricos: el alumno cambia los parámetros y ve el efecto. Encaja
  especialmente con los problemas 11 y 12 de `exercises01` (límite clásico).

---

## 2. Programa de notebooks

### 2.1 Estructura propuesta

```
notebooks/
├── qf2figs.py              # estilo, paleta, savefig() con convenio de nombres
├── nb01_antecedentes.ipynb
├── nb02_postulados.ipynb
├── nb03_sistemas_modelo.ipynb      ← prioridad 1
├── nb04_momento_angular.ipynb
├── nb05_hidrogeno.ipynb            ← prioridad 2
├── nb06_metodos_aproximados.ipynb
├── nb07_polielectronicos.ipynb
├── nb09_diatomicas.ipynb           ← prioridad 3
├── nb10_poliatomicas.ipynb
├── nbM1_vectores.ipynb
└── nbM2_ondas.ipynb
figs/
└── <tema>_<observable>[_<variante>]_v<N>.pdf
```

### 2.2 Convenios

- Un módulo `qf2figs.py` con el estilo común: tamaño fijo pensado para el ancho
  de columna Tufte (~4.2 in) y para la **columna del margen** (~2.0 in), tipografía
  serif que case con el cuerpo del texto, y `savefig` en **PDF vectorial**.
- Nombres siguiendo el convenio del proyecto:
  `<sistema>_<observable>[_<variante>]_v<N>.pdf`
  → `caja1d_psi2_n1-4_v1.pdf`, `h_rdf_1s-3d_v2.pdf`, `n2_diagOM_v1.pdf`.
- Cada notebook **autocontenido**: numpy/scipy/matplotlib. `scipy.special` da
  gratis `eval_hermite`, `sph_harm`, `genlaguerre` — no hay que programar los
  polinomios a mano.
- Cada figura, una celda; la última línea guarda en `figs/`. Regenerar todo debe
  ser `jupyter nbconvert --execute`.

### 2.3 Integración en LaTeX

Tufte-handout tiene tres entornos y conviene usarlos deliberadamente:

- `marginfigure` — esquemas pequeños y de apoyo (el modelo vectorial, el ciclo
  SCF, el plano complejo). Es lo que le da su carácter a la plantilla y ahora
  mismo está **completamente desaprovechado**.
- `figure` — figuras de ancho de texto (funciones de onda, diagramas de OM).
- `figure*` — a ancho completo (diagramas de correlación B₂→F₂, mapas 2D).

Añadir al preámbulo común `\graphicspath{{figs/}{graphics/}}`.

### 2.4 Dependencias

`numpy`, `scipy`, `matplotlib`. Para las isosuperficies 3D de orbitales
(Tema 5, fig. 4) hará falta además `scikit-image` (marching cubes) o `plotly`
con exportación estática. Sugiero un `environment.yml` en `notebooks/`.

---

## 3. Orden de trabajo propuesto

**Fase −1 — Revisar el material nuevo (sin hacer).** Las 6 hojas de
`ejercicios/`, los 3 guiones de prácticas y las dos secciones nuevas de tema09.
Son ~1300 líneas que aún no he leído, y hasta hacerlo el plan está incompleto.

**Fase 0 — Desbloquear (una sesión).** Sin esto no se puede verificar nada más.
1. Arreglar los **4** fallos de compilación restantes: `bm` en 04, dobles
   superíndices en 06, natbib en math01, URL en math02.
2. Extraer `preamble.tex` común y limpiar los restos de la plantilla.
3. `.gitignore` + `Makefile` que compile **los 20 documentos** y falle si alguno
   rompe.
4. Fijar el flujo Overleaf↔git: el remoto ya usa token
   (`https://git@git.overleaf.com/...`) con `osxkeychain`. **Hacer `fetch` al
   empezar cada sesión** — este repo pasó 2,5 años sin sincronizar.

**Fase 1 — Errores de física (🔴), tema a tema.** Es lo que el alumno copia en
el examen. Por impacto: **03** (5 errores, incluidos dos $\hbar$ sin cuadrado y
la $\alpha$ del oscilador) → **04** (6) → **06** (6) → **05** (5) → **09** (5) →
**07** (3) → **01** (2) → **10** (3) → **02** (1).

**Fase 2 — Notebooks y figuras.** Por orden de retorno: `nb03` → `nb05` →
`nb09` → `nb04` → `nb02` → `nb10` → resto.

**Fase 3 — Contenido nuevo.** Decidir lo del Tema 8; escribir `math02`; el
bloque de matrices de `math01`; hojas de problemas 03 y 04.

**Fase 4 — Estilo y ortotipografía (🟡).** En una sola pasada al final, con
`chktex` y un corrector ortográfico en español, para no mezclarlo con lo anterior.

**Sugerencia de flujo:** una rama por tema (`feature/tema03-revision`), con la
Fase 1 y las figuras del mismo tema en el mismo commit, de modo que cada tema
quede cerrado y compilando antes de pasar al siguiente.

---

## 4. Resumen numérico

| | 🔴 | 🟠 | 🟡 | 🔵 |
|---|---|---|---|---|
| Global / infraestructura | 3 | 3 | 2 | 3 |
| Tema 1 | 2 | 5 | 4 | 5 |
| Tema 2 | 1 | 7 | 4 | 5 |
| Tema 3 | 5 | 7 | 4 | 4 |
| Tema 4 | 6 | 6 | 3 | 4 |
| Tema 5 | 5 | 10 | 3 | 5 |
| Tema 6 | 6 | 8 | 5 | 4 |
| Tema 7 | 3 | 8 | 3 | 5 |
| Tema 8 | 1 | — | — | 1 |
| Tema 9 | 5 | 10 | 3 | 5 |
| Tema 10 | 3 | 9 | 2 | 5 |
| math01 | 2 | 7 | — | 4 |
| math02 | 2 | — | — | 2 |
| Problemas | 1 | 6 | 4 | 4 |
| **Total (dic. 2023)** | **45** | **86** | **37** | **56** |
| *ya corregido en Overleaf* | *−6* | *−3* | — | — |
| **Total vigente** | **39** | **83** | **37** | **56** |

**Figuras: 44 construidas y verificadas** (ver §5). Quedan por hacer las de
`math01`/`math02` y las del tema 8 si se escribe.

**Cobertura:** los 20 documentos del repositorio.

---

## 5. Figuras — CONSTRUIDAS

Ya no son una propuesta: están generadas, inspeccionadas una a una y probadas
en LaTeX.

```
notebooks/
├── qf2figs.py            estilo, paleta, anchuras, save()
├── fig_tema01.py … fig_tema10.py, fig_practica_ir.py
└── README.md             uso, convenios y fragmentos LaTeX listos para pegar
figs/                     44 PDF vectoriales + PNG de inspección
Makefile                  make figuras · make comprobar · make limpiar
```

**Reparto:** tema01 5 · tema02 3 · tema03 7 · tema04 4 · tema05 5 · tema06 4 ·
tema07 5 · tema09 4 · tema10 4 · práctica IR 3.

**Anchuras** calibradas para `tufte-handout` y **verificadas compilando** los
tres entornos (`marginfigure` 2.0″, `figure` 4.2″, `figure*` 6.4″).

**Color:** paleta Okabe-Ito reordenada, validada para daltonismo (peor par
adyacente ΔE 9.6 en deuteranopía, ΔE 20.0 en visión normal). Etiquetas
directas sobre cada curva en lugar de leyenda.

### Figuras que resuelven un error del texto

| Figura | Corrige |
|---|---|
| `hidrogeno_radial_Rnl` | rotula los nodos como $n-l-1$, frente al $(n-l)$ del texto (tema05 L188) |
| `polielectronicos_hueco-fermi` | sustituye el párrafo autocontradictorio del hueco de Fermi (tema07 L354-363) |
| `diatomicas_diagrama-om_N2-O2` | aporta la inversión $s$–$p$ y el paramagnetismo del O$_2$, ausentes del tema09 |
| `h2_curva-potencial_De-D0` | distingue $D_e$ de $D_0$, confundidos en tema09 L115-116 |
| `variacional_oscilador_E-lambda` | recupera gráficamente el ejemplo comentado de tema06 L135-181 |
| `huckel_niveles` | da la energía de deslocalización que el tema10 afirma sin calcular |

### Comprobaciones numéricas (tests de regresión)

Los scripts imprimen valores que **confirman de forma independiente** datos de
los apuntes:

- $r_{\max}(1s)=1.00\,a_0$, $r_{\max}(2s)=5.24\,a_0$ ✓ (el texto dice $5.2a_0$),
  $\langle r\rangle_{1s}=1.50\,a_0$
- variacional del oscilador: **13.6 %** por encima de la exacta ✓ (el ejemplo
  comentado dice 14 %)
- He: $\zeta_{opt}=27/16=1.6875$ ✓, $E=-2.8477\,E_h$ ✓
- Hückel butadieno $\pm1.618,\pm0.618$ ✓ (el texto redondea a 1.62/0.62),
  deslocalización $0.472\beta$; benceno $2,1,1,-1,-1,-2$, deslocalización $2\beta$
- ángulo tetraédrico $109.47°$ ✓
- IR: el método de diferencias entre combinaciones recupera $B_0$ y $B_1$ exactos ✓

---

## 6. Material nuevo — revisión

Revisado el 2026-08-08, tras sincronizar con Overleaf.

### 6.1 Hojas de ejercicios (`ejercicios/`)

Reorganización acertada: ahora hay **una hoja por tema, 1–6**, en vez de dos
hojas agregadas. Las 20 soluciones numéricas que he comprobado son correctas
salvo lo indicado.

| Sev | Fichero | Problema |
|---|---|---|
| 🟠 | `ejercicios_01` #4 | Solución: para el electrón da $2.2\times10^{-2}$ m/s. El cálculo correcto es $\lambda=h/mv \Rightarrow v=6.626\times10^{-34}/(9.109\times10^{-31}\times0.03)=\mathbf{2.4\times10^{-2}}$ m/s. El valor del protón ($1.3\times10^{-5}$) sí es correcto |
| 🟠 | `ejercicios_01` #4-5 | Usa $\nu$ (frecuencia) como símbolo de la **velocidad**; debe ser $v$ |
| 🔴 | `ejercicios_02` #2 | **Sigue** la errata de etiquetado: "(a) No. **(d)** No. (c) Sí. (d) No. (e) Sí." → el segundo es **(b)** |
| 🟠 | `ejercicios_02` #5 | **Sigue**: enunciado pide "el valor propio de $x$" cuando es el valor **medio**; y $N=(\frac{2}{\sqrt{\pi/(2a)^3}})^{1/2}$ mezcla $a$ con $\alpha$ |
| 🟡 | `ejercicios_02` #6 | Solución en blanco ("--"). Igual en `_03` #7 y `_04` #2-3 |
| 🟠 | `ejercicios_02` #7 | $[\hat a,\hat a^\dagger]=\hbar$ es correcto con la definición dada, pero conviene advertir que en el convenio adimensional habitual el resultado es $1$ |
| 🟡 | `ejercicios_03` #3 | **Sigue** "especiamiento" → *espaciamiento*; y #2 "Evalua" → *Evalúa* |
| ✅ | `ejercicios_03` #1 | "nos hace faltan" → **corregido** a "nos hacen falta" |
| ✅ | `ejercicios_03` #4 | Caja cúbica, degeneración 1: **correcto** |
| 🟠 | `ejercicios_05` #3 | **Sigue**: "2p: No tiene nodos (excepto $r=0$)". $r=0$ no es un nodo radial —la función se anula por el factor $\rho^l$, sin cambio de signo |
| ✅ | `ejercicios_05` #4 | $\Delta E=9.274\times10^{-24}$ J y $E_{2p-1s}=1.635\times10^{-18}$ J: **verificados** |
| 🟠 | `ejercicios_06` #2 | **Sigue**: "$\infty$ si $L<x<0$" — intervalo vacío; debe ser $x<0$ o $x>L$ |
| 🟡 | todas | `\subsection{\textbf{Soluciones:}}` → `\section*{Soluciones}` |

🔵 **Siguen faltando hojas de los temas 7, 9 y 10** (mi crítica original se
mantiene, ajustada: existen 1–6, faltan 7–10).

### 6.2 Prácticas experimentales

Tres guiones nuevos, los tres compilan. Es un bloque de curso entero que no
estaba en la revisión previa.

**`practicas_exp_ir.tex`** (356 líneas) — el más sustancial. Espectroscopía
roto-vibracional del aire, con Morse, distorsión centrífuga y diferencias
entre combinaciones. Físicamente sólido; he **verificado numéricamente** que
las ecuaciones de las ramas P/R y las dos diferencias entre combinaciones son
mutuamente consistentes y recuperan $B_0$ y $B_1$ exactos.

| Sev | Línea | Problema |
|---|---|---|
| 🔴 | 212 | Distorsión centrífuga: $\tilde\nu_{J\to J+1}=2B(J+1)-4D_J\mathbf{J^3}$. Debe ser $-4D_J\mathbf{(J+1)^3}$ |
| 🟠 | 283-285 | "representando $(J+1/2)$ **frente a** $\tilde\nu_R-\tilde\nu_P$" invierte los ejes: así la pendiente sería $1/4B_1$, no $4B_1$. Debe ser al revés |
| 🟠 | 194, 213 | $\tilde\nu_{J\to J-1}=-2BJ$: número de onda negativo. Presentarlo en valor absoluto o como emisión |
| 🟠 | 120-142 | Mezcla $\tilde\nu$ y $\tilde\omega_e$ para lo mismo dentro de la misma página |
| 🟡 | 16 | `\title[Prá**t**icas...` → *Prácticas* |
| ✅ | 145 | $k_BT/hc=200$ cm$^{-1}$: correcto (207 a 298 K) |
| ✅ | 260-263, 290-297 | Fórmulas de ramas P/Q/R y diferencias entre combinaciones: **verificadas** |
| 🔵 | — | No hay ni una figura. Ya construidas: `hcl_rotovibracional_PR`, `hcl_diferencias-combinaciones`, `hcl_morse-vs-armonico` |

**`practicas_exp_uvvis.tex`** (201 líneas)

| Sev | Línea | Problema |
|---|---|---|
| 🟠 | 108 | Fila C=O: la banda intensa a 190 nm se etiqueta $n\to\sigma^\star$; en los carbonilos esa transición es $\pi\to\pi^\star$ |
| 🟠 | 113-114 | Fila C=C–C=O: la entrada "$\pi\to\pi^\star$ 210 intensa" está **duplicada** |
| 🟠 | 116-118 | Las tres bandas del benceno ocupan tres filas pero el `\chemfig` sólo aparece en la tercera; usar `\multirow` |
| 🟠 | 74 | Presenta $\varepsilon=A/cl$; pedagógicamente mejor la forma directa $A=\varepsilon cl$ |
| 🔵 | 138-146 | Los objetivos no anticipan **la dirección** del efecto: en $n\to\pi^\star$ los disolventes dadores de enlace de hidrógeno producen desplazamiento **hipsocrómico** (al azul). Merece una frase |
| ✅ | 135 | "prohibidas por simetría y por tanto débiles": correcto para $n\to\pi^\star$ |

**`practicas_exp_normativa.tex`** — normas y seguridad; sin contenido
científico que revisar. Compila.

### 6.3 Secciones nuevas de `tema09`

- Nueva `\subsection` "Moléculas diatómicas homonucleares y configuraciones
  electrónicas" — reescribe correctamente el enunciado de Pauli que yo había
  marcado como 🔴.
- Nuevo **apéndice** "Derivación de las ecuaciones de la energía para el
  H$_2^+$" — desarrolla $j$, $k$ y $S$. Buena adición: cubre parte del hueco que
  yo señalaba. 🔵 Sigue faltando conectar con el **orden de enlace** y con la
  **mezcla $s$–$p$**.
