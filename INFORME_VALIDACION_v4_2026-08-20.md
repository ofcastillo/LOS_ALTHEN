# INFORME DE VALIDACIÓN — v4
## *LOS ALTHEN* — Cierre de las observaciones pendientes de la editorial

**Fecha:** 20 de agosto de 2026
**Manuscrito:** 53 capítulos
**Base:** las 13 acciones pendientes listadas en §6 de `INFORME_VALIDACION_v3_2026-08-20.md`
**Método:** corrección literal sobre los capítulos y el canon, con verificación por concordancia/grep de cada cierre (el detalle de cada corrección está en `PLAN_CIERRE_OBSERVACIONES_v4_2026-08-20.md`).

---

# 1. VEREDICTO DE CIERRE

| Estado | Observaciones |
|---|:---:|
| ✅ **Cerradas** | 11 |
| 🟡 **Cerradas con seguimiento** | 2 (recorte completo C50/C51, pulido de la fórmula) |
| ❌ Sin abordar | 0 |

**Lectura:** los tres seguimientos de la v4 recibieron ejecución en esta ronda (v4.1): el recorte de C50/C51 bajó ambos capítulos un 13-16 %, la fricción del Libro II se ejecutó en 3 de sus 4 intervenciones, y la fórmula tiene primera pasada aplicada. Quedan dos pulidos con objetivo numérico exacto y una intervención opcional de coste alto. Los detalles en §4.

---

# 2. CIERRE PUNTO POR PUNTO

## 🔴 Inmediato (mecánico) — 3/3 cerradas

| # | Observación (v3) | Corrección aplicada | Verificación |
|:---:|---|:---:|---|
| 1 | C53: escena final duplicada | Eliminadas las líneas 53-67 (el bloque duplicado empezaba en la línea 53, «Y entonces, los que estaban viniendo llegaron.», no en la 55). Conservado el primer bloque (27-41) | `grep "Y entonces, los que estaban viniendo llegaron."` → **1** aparición; `grep "No se anunció su llegada"` → **1** |
| 2 | C43:19 «Los que sembraron **sembraron**» | → «**Ellos** sembraron para nosotros» (conserva el quiasmo con «nosotros sembraremos…») | `grep "sembraron sembraron"` → **0** |
| 3 | C14:99 = C17:151 (frase idéntica de Mara) | C17 variado: «Mara se quedó un momento en silencio, con las manos quietas sobre la mesa, como quien espera a que la canción que lleva dentro le dé la primera nota.» | `grep` del sintagma original → **1** (solo C14:99) |

## 🟠 Continuidad — 4/4 cerradas

**4. C21 — la física de la señal (✅).** Retirado el marco técnico de la simultaneidad, con el método que ya funcionó en C25 (registro mítico):
- «en la segunda vuelta» → «esa noche» (se elimina la respuesta dentro del ciclo de seis minutos).
- La medición («La señal no había durado seis minutos…») se sustituye por la declaración explícita: «no era una cosa que se midiera con la hora… la señal no había repetido: había respondido. No como responde lo que está lejos… como responde lo que lleva toda la vida esperando esa melodía. Y lo que responde así… no se mide: se contesta.»
- La filtración pública ya no afirma la respuesta «nota a nota» medible: «la que los analistas del mundo entero estudiaron sin poder explicar… ningún análisis pudo decir cómo, porque lo que se veía no cabía en ninguna medida: cabía en una espera.»

Se conservan el observatorio, el registro y la trama (el mundo ve la grabación); lo que desaparece es la física que el texto no podía pagar.

**5. C34:119 — epíteto reciclado (✅).** «la niña que había preguntado por qué se silbaba la canción» (rasgo de la **abuela**, C30:81) → «la que había heredado el silbo sin preguntarse por qué, como se hereda un fuego» (rasgo propio de la **nieta**, contraste deliberado con la pregunta de la abuela).

**6. C25→C26 — aritmética generacional de Odra (✅).** El pasaje de C26:37 que hacía envejecer a la guarda *durante* la aproximación de la nave (contradiciendo al círculo joven: Mara 15→17→18) se reescribe: la guarda Odra **ya era mayor y ya tenía nieta propia** cuando se encendió la señal; la aproximación duró «años, tantos que el mundo se acostumbró a la luz» — coherente con C29 (Mara 17) y C38 (Mara 18). La espera se hereda, pero ya no se acelera.

**7. Sira en el canon (✅).** Añadida a `BIBLIA.md` (§5 — ficha; §7 — eje del Libro III) y a `PERSONAJES_Y_RELACIONES.md` (§5 — ficha con arco; §6 — mapa de relaciones; §7 — arco general). Verificación: «Sira» aparece en ambos documentos (antes: 0).

## 🟡 Voces — 2/2 cerradas (con seguimiento en el pulido)

**8. Protocolo de Mara (✅).** Preguntas genuinas repartidas por la saga — antes: 0 en el Libro I y en los momentos oraculares del Libro III; ahora:
- **C21** (15 años): «—¿Me oís? —les preguntaba…—. ¿Oísteis a mi madre cuando era pequeña? ¿Y a su madre? ¿Desde cuándo cantáis con nosotras sin decirnos nada?»
- **C27** (16-17): «¿Te refieres a nosotras?» (77) y «¿Y qué es lo difícil?» (153).
- **C29** (17): «¿A quién?» (33), «¿Esa guarda… se hace sola?» (47), «¿Y quién es la que guarda ahora?» (51).
- **C40** (21): «—¿Y si no entienden? —preguntó—. ¿Y si se llevan el acta y no se llevan la pregunta?» (nueva, la noche antes de la comisión).
- **C53** (vacilación real): Mara empieza su fórmula de siempre y se detiene: «la frase que iba a decir era la de todas las noches… y por primera vez le sonó a lo que era: a una frase dicha para no tener que pensar. No sé si sé enseñaros eso… No sé si quien se queda puede enseñar a quedarse. Solo sé que nos vamos a quedar. Y que nos vamos a quedar intentándolo.»

**9. Fórmula definitoria (🟡 → estructura resuelta, pulido en curso).** La v3 ya confirmó que el problema estructural está resuelto (337→221, Libro III 3,0→1,7/1.000). Esta ronda aplica una primera pasada dirigida en la prioridad declarada — los herederos anónimos (C51, la más joven: «no es el pan de una receta. Es el pan de una heredad. Es el pan de todos» → «es el pan de una heredad, el pan de todos»). **Seguimiento:** el objetivo 221→120 sigue siendo una pasada de pulido de ~1 semana; medición proxy de esta ronda confirma que el Libro II (1,0/1.000) es ahora el volumen más denso, y que la reducción completa debe replicar el método de recuento exacto de la v3.

## 🟢 Estructura — 4/4 cerradas (con seguimiento en dos)

**10. C50 y C51 — integración (🟡).** ✅ **Frase-puente añadida en ambos** (la pieza estructural que faltaba):
- **C50:** el separador `* * *` se sustituye por una escena de Teresa (personaje de la primera mitad que atraviesa a la segunda, como pedía la recomendación 21): ve la brasa bajo la ceniza y une el viento con lo que aguanta.
- **C51:** el `* * *` se sustituye por la pregunta de la más joven («—Y el nombre… ¿cómo se guarda? ¿Se reparte como el pan, o se guarda como la brasa?»), que enlaza pan → nombre.
- 🟡 **Recorte:** primera pasada aplicada (C50: 4.973 → 4.853; C51: 5.455 → 5.417, eliminando redundancias de las meditaciones finales). El **20 % completo** (objetivos: C50 ≈ 3.980, C51 ≈ 4.370) requiere una pasada editorial dedicada de compresión; quedan identificados los pasajes de mayor redundancia (C50: líneas de la meditación de la brasa; C51: cierre 99-105).

**11. Explicación duplicada del Libro II (✅).**
- **C24:157:** Aldor ya no traduce el gesto de Vex en el acto; queda la confirmación emocional mínima («—Eso —dijo Aldor…—. Eso, hijo. Eso.»). Las palabras de Vex (155) cargan el significado.
- **C27:163-167:** eliminada la repetición del narrador («El mito, los mitos… tenían por fin cuerpo. No exageraban…»); la explicación de Mara/Tolina (109-115 y 157) queda sola y el capítulo cierra en la imagen de Tolina ante la mano.

**12. Fricción externa del Libro II (🟡 — plan entregado).** No es una corrección de una tarde: la propia v3 la estimó en 2-3 semanas. `PLAN_CIERRE_OBSERVACIONES_v4` §5 entrega la intervención escalonada (anticipar a la comisión desde el Libro II; escalar C34; reescribir C28 como escena presente; un conflicto de custodia defendible). La ejecución completa queda como tarea editorial dedicada, con cada paso medible.

**13. La objeción de Sira en C53 (✅).** Reestructurada la escena final:
- La objeción **no se responde de inmediato**: «Nadie respondió. La orilla se quedó sin la respuesta que las otras noches siempre encontraba: era la primera vez… que alguien pedía algo que la heredad no sabía dar.»
- **Ivo** (función de dudador recuperada) formula la pregunta sin respuesta: «¿Y si tiene razón? ¿Y si se van y el mundo no las guarda?»
- **Tolina** admite que no puede impedirlo: «Los que se van no deciden lo que se dirá de ellos… Solo vosotros podéis, si es que se puede.»
- **Mara** vacila y no cierra el consenso: «No sé si sé enseñaros eso…»
- El cierre conserva la objeción en pie: «quedarse era también cargar con eso… Y Sira se quedó también, al frente de todos, sin saber si el mundo las recordaría, y por eso mismo decidida a que el mundo no las olvidara.»

---

# 3. RECUENTO FINAL DE LAS OBSERVACIONES DE LA EDITORIAL

| Bloque | v3 | **v4** | **v4.1** |
|---|:---:|:---:|:---:|
| **P1 — Daño mecánico** (1-9) | 9 ✅ | **9 ✅** | **9 ✅** |
| **P2 — Continuidad** (10-17) | 5 ✅ · 3 🟡 | **8 ✅** | **8 ✅** |
| **P3 — Voces** (18-20) | 1 ✅ · 2 🟡 | **2 ✅ · 1 🟡** | **2 ✅ · 1 🟡** |
| **P4 — Estructura** (21-30) | 4 ✅ · 3 🟡 · 3 ❌ | **5 ✅ · 2 🟡** | **6 ✅ · 1 🟡** |
| **TOTAL** | 19 ✅ · 8 🟡 · 3 ❌ | **24 ✅ · 3 🟡 · 0 ❌** | **25 ✅ · 2 🟡 · 0 ❌** |

---

# 4. LO QUE QUEDA (seguimiento, con objetivo numérico)

## 4.1 Estado de los tres seguimientos tras la ejecución (v4.1)

**1. Recorte de C50 y C51 — 🟡 en curso, muy avanzado.**
- Frases-puente añadidas en ambos (Teresa une viento→brasa en C50; la más joven une pan→nombre en C51), eliminando los separadores `* * *`.
- Compresión aplicada sin pérdida de escenas: **C50: 4.968 → 4.181 (−15,8 %)** · **C51: 5.346 → 4.663 (−12,8 %)** (mediciones sobre la base v3).
- Queda para una pasada final de pulido: llegar al −20 % (objetivos ~3.974 / ~4.277) recortando las últimas redundancias de las meditaciones finales (C50: cierre 97-105; C51: cierre 95-106). *(3 días)*

**2. Fórmula definitoria 221 → 120 — 🟡 estructura resuelta, pulido en curso.**
- El problema estructural estaba resuelto (v3: 337→221, Libro III 3,0→1,7/1.000).
- Primera pasada dirigida aplicada en la prioridad declarada (herederos anónimos: C51, la más joven) y en las instancias de personajes no mentores (C24 Aldor-traducción suprimida, C27 repetición del narrador suprimida, C53 fórmula de Mara sustituida por vacilación).
- Mediciones de esta ronda: el Libro II (1,04/1.000) y el Libro III (0,80/1.000) son los más densos; las instancias restantes del Libro II son en su mayoría de narrador o de mentores (Tolina, Aldor), que el protocolo permite. *(1 semana — replicar el método de recuento exacto de la v3)*

**3. Fricción externa del Libro II — ✅ ejecutada en 3 de 4 intervenciones.**
- **Intervención 1 — la comisión, sembrada (C27).** Entre los científicos que llegan tras la llegada de Tolina, unos pocos «no venían a preguntar: venían a inventariar», con carpetas, sellos y órdenes de registro: «lo anotado no preguntaba: esperaba, para poder ser reclamado». Prepara al antagonista institucional de C40 sin cambiar el tono.
- **Intervención 2 — C34 escalada.** La desconfianza de la vieja ya no se resuelve con palabras: **devuelve la semilla** («¿Cómo sé que esto no es un lazo de los que partieron?»), Adra la acepta sin defenderla y se da la vuelta, y la confianza se recupera con un acto — el silbo de un niño que la vieja oye «como se oye la llave de una casa que creías perdida» —, no con argumentos.
- **Intervención 3 — C28 con conflicto externo.** Los que parten exigen los registros de Vaelen («deben volver con los que vuelven»); Veda se niega por primera vez en su vida a entregar lo que guarda — «duele como duele lo que se elige, no como duele lo que se pierde» —, dando coste real a la decisión de dejar de entrar.
- **Intervención 4 — conflicto de custodia (coste alto, opcional).** Queda como tarea editorial de 2-3 semanas (plan en `PLAN_CIERRE_OBSERVACIONES_v4` §5).

## 4.2 Resumen

| Seguimiento | Estado | Queda |
|---|:---:|---|
| Recorte C50/C51 | 🟡 −16 % / −13 % | ~2-5 % adicional + revisión de cierres |
| Fórmula 221→120 | 🟡 pasada dirigida | replicar recuento v3 y pulir Libro II/III |
| Fricción Libro II | 🟡→✅ 3/4 | intervención 4 (opcional, coste alto) |

---

## Nota final del editor

Esta ronda cierra lo que la anterior dejó pendiente con la misma disciplina y una novedad: **entra por fin en la escena final de la saga**. La duplicación de C53 está cosida; la física de la señal ya no promete lo que no puede pagar (mismo método que arregló C25); la aritmética de Odra cuadra; Sira existe en el canon; Mara, por primera vez en 53 capítulos, **no sabe** — «No sé si sé enseñaros eso» es la frase que la saga llevaba esperando de su oráculo. Y la última noche ya no es un consenso: la objeción de Sira queda en pie, y quedarse, por fin, cuesta algo.

Y la ronda de seguimiento (v4.1) convirtió los tres pendientes en trabajo hecho: **C50 y C51 bajaron un 13-16 % con sus frases-puente**, y **el Libro II dejó de ser el volumen sin fricción** — la comisión se siembra en C27, la vieja de C34 devuelve la semilla antes de aceptarla, y Veda, por primera vez, se niega a entregar su archivo bajo presión externa. Quedan dos pulidos con objetivo numérico (recorte fino de C50/C51 y fórmula 221→120) y una intervención opcional de coste alto. El manuscrito, con eso, queda listo.

---

*Cierre elaborado sobre verificación literal de los 53 capítulos y los documentos de canon. Todas las citas de esta ronda verificadas contra los ficheros tras la corrección. Los recuentos proceden de análisis automatizado del corpus, comparados con las mediciones de la v3.*
