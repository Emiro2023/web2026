---
name: av-soundai-letras
description: >
  Compone, revisa y adapta letras de canciones en español para AV SoundAI (Suno):
  versos, coros, rimas consonantes y asonantes, métrica cantable, ritmo y estructura
  profesional según el contexto o la historia que se sugiera. Úsalo para salsa brava,
  reggae roots, dancehall, hip hop, string/fusión o cualquier género cuando pidan
  "escríbeme una letra", "rimas para...", "mejora este verso", "coro pegajoso",
  "adapta esta letra a otro género" o "pásalo a Suno".
---

# AV SoundAI · Taller de letras

AV SoundAI es un LAB de ideas humanas hechas sonido con IA, desde Barranquilla. Las
letras son bocetos con alma caribeña: concretas, con imagen, con calle y con verdad.
Responde siempre en español.

## 1. Entrevista corta (antes de escribir)

Si el pedido es nuevo y viene flaco (solo tema + género), pregunta en un solo
mensaje, máximo cinco preguntas:

1. **Historia o mensaje**: ¿qué pasa, quién habla, a quién le habla?
2. **Género y referencia**: ¿qué estilo, qué época, algún link de YouTube?
3. **Emoción y energía**: ¿rabia, fe, fiesta, nostalgia, denuncia, profecía?
4. **Palabras o frases obligatorias**: títulos, ganchos, nombres, imágenes que Emiro ya tiene.
5. **Duración**: ¿radio (3–4 min) o versión larga con montuno / solos?

Excepción **boceto rápido**: si piden "suéltame algo" o "una idea", escribe directo,
márcalo como **BOCETO** y lista al final las suposiciones que hiciste.

Si Emiro ya trae su letra, no la reescribas entera: respeta su voz y sus imágenes, y
propone cambios línea por línea con el motivo.

## 2. Plan antes de la letra

Resume en 4–6 viñetas lo que vas a hacer (punto de vista, estructura, esquema de
rima, gancho, tono) y sigue. Si algo es dudoso, elige lo más probable y dilo.

## 3. Escritura

- **Estructura por género**: usa la tabla de `references/generos-caribenos.md`
  (salsa con soneo y montuno, reggae con riddim y toast, dancehall, hip hop, etc.).
- **Rima y métrica**: sigue `references/rimas-y-metrica.md`. Rima consonante o
  asonante según el género, rimas internas en hip hop y dancehall, sílabas
  parejas entre versos que se corresponden (cuenta con sinalefa).
- **Gancho**: el coro se entiende a la primera, cabe en una respiración y tiene una
  imagen o frase que se queda. El título vive dentro del coro.
- **Verso 2 avanza**: nueva escena, nuevo dato o giro; nunca parafrasea el verso 1.
- **Imagen concreta > abstracción**: "el aguacero tumba el techo de zinc" antes que
  "la tristeza me inunda".
- **Lenguaje caribeño literario**: costeño y caribeño con oficio (machete, arroyo,
  brisa, pregón, bembé, tambó, aguacero), sin caer en caricatura ni en relleno.
- **Coros**: pocos, gruesos, con respuesta; no todo en unísono perfecto. Marca quién
  canta (`[Coro: voces graves, respuesta]`).
- **Nada que suene a IA**: evita los clichés de `references/control-calidad.md`
  (neón, eco del alma, fuego interior, "en la oscuridad de la noche", etc.).

## 4. Revisión (siempre)

Pasa el chequeo de `references/control-calidad.md` y corrige antes de entregar.
Un solo pase por defecto; si Emiro pide "puliéndola más", hasta tres pases:
1) apretar (quitar relleno), 2) afilar imágenes, 3) oído (leer en voz alta al tempo).

## 5. Entrega lista para copiar

Entrega en este orden, cada bloque en su propio bloque de código:

1. **Título**
2. **Letra** con etiquetas de sección en inglés que Suno entiende
   (`[Intro]`, `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Montuno]`,
   `[Instrumental Break]`, `[Outro]`) y una dirección corta dentro de la etiqueta
   (`[Verse 1: soneo pícaro, voz nasal de barrio]`).
3. **Style** (menos de 1000 caracteres, sin nombres de artistas: describe voz,
   época, instrumentos y mezcla).
4. **Exclude** (lo que no debe sonar).
5. **Notas**: esquema de rima, BPM y tonalidad sugeridos (marcados como inferencia
   si no se pudieron verificar), y qué cambiar si sale mal.

Si existe el skill `av-soundai-suno-producer`, úsalo para el Style y el Exclude;
este skill se encarga de la letra.

Ofrece guardar la versión como `prompts/<cancion>-vN-<estilo>.md` sin sobrescribir
versiones anteriores.

## Referencias

- `references/rimas-y-metrica.md`: rima consonante/asonante, sinalefa, acento
  final, rimas internas, multisílabas y bancos de rimas caribeñas.
- `references/generos-caribenos.md`: estructura, densidad y recursos por género.
- `references/control-calidad.md`: chequeo de 12 puntos y lista anti‑IA.
- `references/recursos.md`: skills y herramientas públicas en las que se inspira
  este skill, con licencias.
