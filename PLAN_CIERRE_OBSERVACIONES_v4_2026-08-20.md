# PLAN DE CIERRE DE OBSERVACIONES — v4
## *LOS ALTHEN* — Cierre de las observaciones pendientes de la editorial (derivadas de INFORME_VALIDACION_v3)

**Fecha:** 20 de agosto de 2026
**Origen:** las 13 acciones pendientes listadas en §6 de `INFORME_VALIDACION_v3_2026-08-20.md` (19 ✅ resueltas · 8 🟡 parciales · 3 ❌ sin abordar).
**Método de cierre:** corrección literal sobre los 53 capítulos y los documentos de canon, con verificación posterior (grep/recuento) para cada observación.
**Estado de ejecución:** ✅ **ejecutado** — 11 de 13 cerradas; 2 con seguimiento de pulido (recorte fino C50/C51, fórmula) y la fricción del Libro II ejecutada en 3 de sus 4 intervenciones. Cierre punto por punto en `INFORME_VALIDACION_v4_2026-08-20.md` (incluye la ronda de seguimiento v4.1).

---

## 0. Principio rector

Cada observación se cierra con **la corrección más pequeña que la resuelve de verdad**, sin reescribir lo que ya funciona. Donde la editorial pedía "retirar el marco técnico y dejar el fenómeno como inexplicable" (física de la señal), se aplica exactamente ese método, que ya funcionó en C25.

---

## 1. 🔴 INMEDIATO (mecánico) — una tarde

| # | Observación (v3) | Corrección | Verificación de cierre |
|---|---|---|---|
| 1 | C53: escena final duplicada (la validación dice líneas 55-67; el bloque duplicado real empieza en la línea 53, «Y entonces, los que estaban viniendo llegaron.») | Eliminar las líneas 53-67 (segunda copia íntegra). Conservar el primer bloque (27-41), que enlaza con la despedida de Tolina (45-49) | `grep` de «Y entonces, los que estaban viniendo llegaron.» → 1 aparición; recuento de líneas de C53 = 142 − 15 |
| 2 | C43:19 «Los que sembraron **sembraron** para nosotros» | «Ellos sembraron para nosotros» (preserva el quiasmo con «nosotros sembraremos para los que vengan») | grep «sembraron sembraron» → 0 |
| 3 | C14:99 y C17:151, frase idéntica de Mara («Mara se detuvo un momento, con la cabeza ladeada…») | Variar la de C17 (segunda aparición, contexto de miedo/urgencia) por un gesto distinto | grep del sintagma → 1 aparición (C14) |

## 2. 🟠 CONTINUIDAD — lo último que quedaba

| # | Observación (v3) | Corrección | Verificación de cierre |
|---|---|---|---|
| 4 | C21: la señal responde en tiempo real dentro de un ciclo de seis minutos, narrada en entorno de rigor aparente (auriculares, grabadoras, analistas) | Retirar el marco técnico de la simultaneidad: la narración deja de afirmar que la señal "siguió" la melodía dentro de la misma vuelta medible y declara el fenómeno como inexplicable (método C25: «brillaba como se enciende lo que se espera»). Se conserva el observatorio y el registro (la trama los necesita), pero el texto ya no hace física que no puede pagar | Relectura de C21:75-107; 0 afirmaciones de respuesta en tiempo real medible |
| 5 | C34:119: la nieta hereda el epíteto de la abuela («la niña que había preguntado por qué se silbaba la canción», que es lo que hace la abuela en C30:81) | Sustituir por rasgo propio de la nieta: la que heredó el silbo sin preguntarse por qué, «como se hereda un fuego» (contraste deliberado con la pregunta de la abuela) | Relectura de C34:119; el epíteto «la niña que había preguntado…» queda en 0 apariciones |
| 6 | C25→C26: la Odra-guarda es «muy vieja» y tiene nieta propia sin que haya pasado el tiempo necesario; C26:37 hace envejecer a la guarda durante la aproximación, contradiciendo al círculo joven (Mara 15→17→18) | Reescribir el pasaje de C26:37: la guarda Odra **ya era vieja y ya tenía nieta** cuando se encendió la señal (heredó el puesto de la vieja Odra siendo ya mayor); la aproximación de la nave no comprime generaciones en la Tierra. La espera se hereda, pero no se acelera | Relectura de C26:37, 91, 101-103; coherente con C29 (Mara 17) y C38 (Mara 18) |
| 7 | Sira actúa en 7 capítulos (C42, C45-47, C51-53) y no existe en el canon | Añadir ficha de Sira en `BIBLIA.md` (Libro III) y en `PERSONAJES_Y_RELACIONES.md` (ficha + mapa de relaciones + arco) | grep «Sira» en ambos documentos → ≥ 3 apariciones |

## 3. 🟡 VOCES — el último tramo

| # | Observación (v3) | Corrección | Verificación de cierre |
|---|---|---|---|
| 8 | Mara: 1 pregunta en 48 parlamentos; la joven-oráculo no duda nunca | Aplicar el protocolo que funcionó con Ivo: 5-6 preguntas repartidas por la saga (C23, C25, C29, C38, C40, C46) + una vacilación real en la escena final de C53 (unida a la observación 13) | Recuento de preguntas de Mara ≥ 6; 1 vacilación en C53 |
| 9 | Fórmula definitoria «no es X: es Y» / «no… sino…»: 221 (objetivo ≤ 120); el Libro III bajó de 3,0 a 1,7/1.000 pero sigue siendo la voz más sentenciosa | Reducción quirúrgica priorizando: (a) parlamentos de herederos anónimos del Libro III, (b) las concentraciones de C50/C51 (se recortan también en la observación 10). No se toca a Aldor/Tolina (función aforística) | Recuento final < 221; densidad del Libro III < 1,7/1.000 |

## 4. 🟢 ESTRUCTURA

| # | Observación (v3) | Corrección | Verificación de cierre |
|---|---|---|---|
| 10 | C50 y C51: dos mitades unidas por `* * *` sin frase-puente; sin comprimir | (a) Frase-puente que dramatice el paso viento→brasa (C50) y pan→nombre (C51); (b) recorte ~20 % de cada capítulo (cortar redundancia anafórica, no escenas) | Relectura; recuento de palabras de C50 y C51 |
| 11 | C24:157: Aldor traduce el gesto de Vex en el acto; C27:163-167: el narrador repite la explicación de Tolina | C24: reducir la traducción a una confirmación emocional mínima («—Eso —dijo Aldor…—. Eso, hijo.»), dejando que el gesto hable; C27: eliminar las líneas 163-167 (repetición del narrador), cerrar en la imagen de 161 | Relectura de C24 y C27 |
| 12 | Libro II (19 capítulos) sin fricción externa; único volumen sin revisar | No es una corrección de una tarde: es una partida de 2-3 semanas. **Plan concreto** en §5: antagonismo institucional (la comisión) anticipado desde el Libro II, conflicto entre Adra y la vieja (C34) escalado, y un obstáculo real en C28. En esta ronda se entrega el plan; la ejecución completa queda como tarea del autor/editor | Documento §5 |
| 13 | C53: la objeción de Sira se responde de inmediato; la última noche vuelve al consenso | Reestructurar la escena: la objeción de Sira **no se resuelve en el acto**; nadie tiene la respuesta; Mara intenta responder y **vacila** (observación 8); la escena se cierra con la objeción en pie y la partida de los Ysann como lo único que queda por decir | Relectura de C53:27-41 |

## 5. PLAN DE FRICCIÓN PARA EL LIBRO II (observación 12)

El Libro II es el eslabón débil: solo C34 y C35 tienen fricción externa real. Propuesta de intervención, de menor a mayor coste:

1. **Anticipar a la comisión (coste bajo).** Hoy la comisión aparece de golpe en C40 (Libro III). Sembrar en el Libro II dos avisos: una carta o un equipo técnico que llega al valle a "inventariar la señal" tras el coro de manos (C25) y se va sin entender nada (C27-C30). Prepara el antagonista institucional sin cambiar el tono.
2. **Escalar C34 (coste medio).** La desconfianza de la vieja hacia Adra es la única fricción real; darle una segunda vuelta: que la vieja se lleve la semilla un momento (tensión de objeto), y que Adra tenga que recuperar la confianza con un acto, no con palabras.
3. **Reescribir C28 (coste medio).** «Una meditación sin escena de conflicto que narra hacia adelante la vida entera y la muerte de Veda»: convertir la muerte de Veda en una escena presente (el círculo la encuentra, alguien quiere impedirla, el archivo se resiste a soltar).
4. **Un obstáculo real en la custodia (coste alto).** Un conflicto entre los que quieren proteger la cueva de la curiosidad del mundo y los que quieren abrirla — dos posiciones defendibles, ninguno villano. Es el antagonismo que la saga sabe hacer.

## 6. ENTREGABLES DE ESTA RONDA

1. `PLAN_CIERRE_OBSERVACIONES_v4_2026-08-20.md` (este documento).
2. Correcciones aplicadas a los capítulos (C14, C17, C21, C24, C25, C26, C27, C34, C43, C50, C51, C53) y al canon (`BIBLIA.md`, `PERSONAJES_Y_RELACIONES.md`).
3. `INFORME_VALIDACION_v4_2026-08-20.md` con el cierre punto por punto y la verificación final.

---

*Plan elaborado sobre verificación literal de los 53 capítulos y los documentos de canon. Cada cierre lleva su criterio de verificación para que la siguiente ronda no necesite reinterpretar nada.*
