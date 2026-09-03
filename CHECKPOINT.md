# CHECKPOINT

## Current Goal

Revisar y completar los apuntes de Química Física II siguiendo `REVIEW_PLAN.md`,
tema por tema. Temas 1 y 2 terminados; siguen las mejoras 🔵 de tema01 y el
tema 3.

## Work Done

### Session 2026-09-03 — Tema 2

Revisión completa de `tema02.tex`, item por item, discutiendo cada cambio y
regenerando el PDF en cada paso. Resultado: 8 páginas, 0 overfull, sin
referencias sin resolver.

- **Los 12 hallazgos del plan, cerrados**, salvo uno rechazado: el 🟡 que pedía
  cambiar "es proporcional" por "es igual a" en la interpretación de Born. En
  ese punto $\psi$ todavía no está normalizada, así que *proporcional* era lo
  correcto. Queda anotado como rechazado en `REVIEW_PLAN.md`.
- **Convenio de normalización fijado**: se mantiene $N$ en `eq:norm`, se añade
  $N=(\int\psi^\star\psi\,dx)^{-1/2}$ —el texto introducía $N$ pero nunca decía
  cómo obtenerla— y se declara que de ahí en adelante $\psi$ ya está
  normalizada. Decisión de David: mostrar cómo se normaliza importa, porque es
  el primer contacto del alumno con la función de onda. Sin ejemplo concreto de
  momento, sólo la expresión general.
- **Postulado de la medida reescrito**: el recuadro decía que una medida
  devuelve el valor promedio, mientras que el párrafo de debajo decía bien que
  devuelve un autovalor $\omega_k$. Ahora el recuadro enuncia el autovalor y el
  promedio llega después como consecuencia, con $P(\omega_k)=|c_k|^2$ y
  $\langle\Omega\rangle$ como ecuaciones numeradas.
- **Añadida la ecuación de Schrödinger independiente del tiempo.** No estaba en
  ninguna parte del tema: la separación de variables sólo explotaba la rama
  temporal. Ahora $\hat{H}\psi=E\psi$ es `eq:schro-independiente`.
- **$|\Psi|^2$ con módulo**, y la cancelación de fases escrita. Antes se
  argumentaba con $\Psi^2$, que conserva $e^{-2iEt/\hbar}$ y no demuestra nada.
- **Pauli condensado y metido en `theorem`** (decisión de David). Era el único
  postulado en prosa, y por eso la numeración se quedaba en cinco. Ahora hay
  seis postulados numerados y el desarrollo vive en el Tema 7.
- **Las 7 secciones numeradas** (la primera era `\section*`).
- **Cuatro figuras colocadas y citadas desde el texto.** Tres ya existían sin
  usar; la cuarta (`postulados_psi-psi2_v1.pdf`) se escribió en esta sesión.
- **`incertidumbre_x-k` renombrada a `incertidumbre_x-p`**: $k$ no se define en
  ningún tema y chocaba con el número de onda $\tilde\nu=1/\lambda$ de tema01.
  La figura habla ahora de $p$ y enuncia $\Delta x\,\Delta p\geq\hbar/2$.
- **La figura de $\psi$ frente a $|\psi|^2$, rehecha.** La primera versión era una
  gaussiana, positiva en todo punto, así que $|\psi|^2$ parecía sólo una copia
  estrecha de $\psi$. David señaló que faltaba lo esencial: que el cuadrado hace
  la densidad positiva donde $\psi$ era negativa, y que aparecen nodos donde
  $\psi$ cambia de signo. Ahora usa un paquete modulado por un coseno.
- **Tres retratos nuevos**: Born, Schrödinger y Pauli, en el margen de sus
  secciones respectivas, con la macro `\retrato` copiada del preámbulo de
  tema01. Todos de dominio público y verificados contra la API de Commons; dos
  candidatos mejores se descartaron por licencia (CC BY-SA y *Attribution*).
  Heisenberg no se repite porque ya está en tema01.

### Pasada de redacción

Al final de la sesión se revisó la prosa entera, no ya la corrección. Los
cambios que afectan a lo que entiende el alumno:

- El postulado de Born decía «un volumen $\tau$ en el punto $r$» y la fórmula
  usaba $d\tau$: ahora es «un elemento de volumen $d\tau$ alrededor del punto».
- Se integraba «en una pequeña región $d\tau$», es decir, sobre aquello con lo
  que se integra. Ahora se integra sobre una región finita.
- «En la medida en que» como conector, en un tema cuya sección central se
  titula «El resultado de una medida»: sustituido por «Puesto que».
- «podemos medir los operadores que conmuten con el hamiltoniano»: se miden
  observables, y lo que ocurre es que tienen valor definido y constante.
- Al principio de incertidumbre le faltaba **simultáneamente**; sin esa palabra
  el enunciado es falso.
- La *two-valuedness* de Pauli era «una dualidad», la misma palabra que tema01
  dedica a la dualidad onda-partícula. Ahora es «bivalencia», con nota al
  margen que lo distingue.
- La completitud del conjunto de funciones propias se enunciaba dos veces sin
  conectarlas; ahora la segunda remite a la primera.

**Lección de maquetación:** fijar un flotante con `[!b]` ató la página a la
longitud del texto de ese momento. Al reescribir la prosa, la Figura 4 dejó de
caber al pie y se llevó una página entera para ella sola (9 páginas). Con
`[!htb]` LaTeX vuelve a resolverlo solo. No conviene clavar flotantes.

### Dos trampas de maquetación, para los temas 03--10

Ninguna de las dos aparece en el `.log`: `make comprobar` da OK y la página
está mal. Sólo se ven mirando el PDF renderizado.

1. **El pie de un flotante y una `\sidenote` pueden imprimirse uno encima del
   otro.** Los dos quieren el margen y sus mecanismos de colocación no se
   coordinan. Los avisos «Marginpar on page N moved» son la única pista, y son
   tan frecuentes (tema01 tiene 17) que es fácil descartarlos. Solución: no
   competir por el mismo hueco; aquí la nota se integró en el texto corrido.
2. **Un título de sección se queda solo al pie de página** cuando hay un
   flotante pendiente: la clase vacía los flotantes *después* de componer el
   título. Solución: `\FloatBarrier` explícito antes del `\section`, y
   `[!b]` en el flotante para que caiga al pie de la página anterior en vez de
   saltar a la siguiente y dejar un hueco.

## Current State

| Qué | Estado |
|---|---|
| tema01 | terminado, 8 páginas, 0 overfull |
| tema02 | terminado, 8 páginas, 0 overfull, 4 figuras |
| Compilación global | sigue fallando en tema04, tema06, math01, math02 |
| Remotos | **sin sincronizar**: nada commiteado de esta sesión |
| Estilo QF2 | aplicado a tema01 y tema02 |

**Árbol de trabajo sin commitear:**

```
 D figs/incertidumbre_x-k_v1.pdf     (renombrada a x-p)
 M notebooks/nb02_postulados.ipynb
 M tema02.tex
 M REVIEW_PLAN.md
 M CHECKPOINT.md
?? CLAUDE.md
?? figs/gaussiana_psi-psi2_v1.pdf
?? figs/incertidumbre_x-p_v1.pdf
```

## Next Steps

1. **Commitear el trabajo del tema 2** y decidir si se empuja a Overleaf
   (`origin` es el proyecto vivo).
2. Las 5 mejoras 🔵 de tema01: Stefan-Boltzmann, límite Planck→Rayleigh-Jeans,
   potencial de frenado, condición de Bragg, tabla-resumen.
3. Arreglar los 4 documentos que no compilan (tema04, tema06, math01, math02).
4. Revisar el tema 3 según `REVIEW_PLAN.md`.
5. Pendiente de tema02: ejemplo resuelto de normalización y notación de Dirac
   con referencia cruzada a `math01`.
6. **Colocar las figuras en los temas 03–10.** Están todas generadas pero
   ningún tema salvo 01 y 02 las usa. Cada uno necesita además
   `\graphicspath{{figs/}...}` en el preámbulo, que ahora apunta sólo a
   `graphics/`.

## Key Files

- `CLAUDE.md` — convenciones del repositorio (nuevo, sin commitear)
- `REVIEW_PLAN.md` — plan de revisión; sus números de línea son de 2023 y ya no
  cuadran: localizar por contenido
- `tema01.tex`, `tema02.tex` — terminados; exemplars de estilo
- `notebooks/nb02_postulados.ipynb` — genera las 4 figuras de tema02
- `Makefile` — `make`, `make figuras`, `make comprobar`
