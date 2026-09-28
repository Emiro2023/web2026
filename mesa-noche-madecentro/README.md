# Mesa de noche 40 × 50,7 × 37,3 cm (juego con la cómoda)

> 📘 **Manual completo de corte y armado (PDF):** [manual-armado/manual-corte-y-armado.pdf](../manual-armado/manual-corte-y-armado.pdf)

Versión hecha en casa de la **Mesa de Noche Eter** de Bylmo: 2 cajones, un
nicho abierto arriba y zócalo abajo. Usa **las mismas medidas exteriores**
(40 cm de ancho, 50,7 cm de alto y 37,3 cm de fondo), pero el material, los
cantos y los pomos de estrella son los de la
[cómoda](../comoda-madecentro/README.md), para que hagan juego.

> Referencia: la Eter cuesta **$239.900** en Bylmo (antes $382.100) y aparece
> **agotada**. Hecha con el sobrante de la lámina de la cómoda sale más barata
> (ver presupuesto).

| Cerrada | Abierta | Frente |
|---|---|---|
| ![](renders/1-cerrada.png) | ![](renders/2-abierta.png) | ![](renders/3-frente.png) |

| En Cartagena | Juego blanco | Juego Cartagena |
|---|---|---|
| ![](renders/4-cartagena.png) | ![](renders/5-conjunto-blanco.png) | ![](renders/6-conjunto-cartagena.png) |

Renders 3D a escala real: `../comoda-madecentro/fuente/scene.html?model=mesa`
(o `model=set` para ver el juego).

## Diseño

| Parte | Medida |
|---|---|
| Tapa | 400 × 373 mm, al ras con los costados y con el frente de los cajones |
| Nicho abierto (arriba) | 370 mm de ancho × 130 mm de alto libre |
| Cajones | 2 frentes de **397 × 141 mm**, 3 mm de holgura |
| Zócalo | 70 mm, retrocedido 20 mm |
| Material | Melamina RH 15 mm (blanca o Cartagena) + fondo HDF 3 mm |

## Lista de cortes

### Melamina RH 15 mm (del mismo color que la cómoda)

| # | Pieza | Cant. | Medida (mm) | Canto |
|---|---|---|---|---|
| 1 | Tapa | 1 | 400 × 373 | 2L + 2C |
| 2 | Costado | 2 | 492 × 358 | 1L (frente) + 1C (abajo) |
| 3 | Piso | 1 | 370 × 358 | 1L |
| 4 | Repisa del nicho | 1 | 370 × 358 | 1L |
| 5 | Zócalo | 1 | 370 × 70 | 1L |
| 6 | Travesaño trasero | 1 | 370 × 80 | — |
| 7 | Frente de cajón | 2 | 397 × 141 | 2L + 2C |
| 8 | Costado de cajón | 4 | 300 × 100 | 1L (arriba) |
| 9 | Frente/fondo interno de cajón | 4 | 314 × 100 | 1L (arriba) |

### HDF 3 mm (del mismo HDF de la cómoda)

| # | Pieza | Cant. | Medida (mm) |
|---|---|---|---|
| 10 | Fondo | 1 | 400 × 492 |
| 11 | Base de cajón | 2 | 344 × 300 |

**Canto:** ~10 m más.

## Compra: **1 sola lámina** para cómoda + mesa de noche

| Lámina | Cantidad | Precio web |
|---|---|---|
| Melamina RH 15 mm **2,15 × 2,44 m** (el mismo color para los dos muebles) | **1** | $266.410 blanca / $365.872 Cartagena |
| HDF 3 mm | **1** | fondos y bases de cajón de ambos |

Las **47 piezas** (30 de la cómoda y 17 de la mesa) caben en la lámina con
**1 cm de refilado por borde** y **4 mm de sierra**. Todos los cortes son de
tipo guillotina, como los de la seccionadora de Madecentro, y se aprovecha el
**85 %** de la lámina.

![Despiece en 1 lámina](despiece-1-lamina.png)

Lleva este plano (`despiece-1-lamina.png`) con las dos listas de cortes y pide
que corten **las dos listas en la misma lámina**. El optimizador de la tienda
puede acomodar las piezas de otra forma; lo importante es que ya está
comprobado que caben. El cálculo está en `despiece.py`.

## Costo aproximado del juego (cómoda + mesa de noche, 1 lámina)

Precios de madecentro.com (sept. 2026) marcados con 💲. Lo demás es estimado.

| Concepto | Cómoda | Mesa | Juego |
|---|---|---|---|
| 💲 Lámina blanca RH 15 mm 2,15 × 2,44 ($266.410, repartida 72 / 28 %) | $192.900 | $73.500 | $266.410 |
| HDF 3 mm (1 lámina, 78 / 22 %) | $43.000 – $66.000 | $12.000 – $19.000 | $55.000 – $85.000 |
| Corte (47 piezas) | $22.000 – $48.000 | $13.000 – $27.000 | $35.000 – $75.000 |
| Canto + enchape (25 m + 10 m) | $65.000 – $120.000 | $25.000 – $50.000 | $90.000 – $170.000 |
| 💲 Rieles extensión total Mobile 38 kg (desde $5.917 el par*) | 4 pares 35 cm ≈ $24.000 – $36.000 | 2 pares 30 cm ≈ $12.000 – $18.000 | $36.000 – $54.000 |
| 💲 Bisagras cierre lento Bonuit parche ($3.137 el par) | 1 par $3.137 | — | $3.137 |
| 💲 Tornillo ensamble 6 × 2" caja × 100 ($6.419, alcanza para los dos) | $4.300 | $2.100 | $6.419 |
| 💲 Cantonera 19 × 12 mm ($296 c/u): 4 para el sobre + 2 anti-volteo / 2 para la tapa | $1.776 | $592 | $2.368 |
| Pines de repisa, tacos para pared | ≈ $4.000 | — | ≈ $4.000 |
| Pomos | $0 (reusar estrellas) | $0 (reusar estrellas) | $0 – $30.000 si compras nuevos |

\* $5.917 es el precio del riel de **25 cm**. En "Selecciona tu medida" elige
**35 cm** (cómoda) y **30 cm** (mesa); pueden costar un poco más. Cada par trae
12 tornillos, igual que las bisagras, así que no hace falta comprar tornillos
pequeños aparte.

### ¿Cuánto cuesta cada mueble?

| Mueble | Rango (blanco) | **Blanco realista** | **Cartagena realista** |
|---|---|---|---|
| Cómoda 90 × 80 × 40 | $360.000 – $495.000 | **≈ $410.000** | **≈ $480.000** |
| Mesa de noche 40 × 50,7 × 37,3 | $140.000 – $200.000 | **≈ $160.000** | **≈ $190.000** |
| **Juego completo** | $500.000 – $695.000 | **≈ $570.000** | **≈ $670.000** |

Los rieles reales de Mobile ($5.917 el par) resultaron mucho más baratos de lo
estimado, por eso el total bajó unos $110.000. Lo único que sigue estimado es
el **HDF, el corte y el enchape**, que se cotizan con el servicio de tableros a
la medida de la página.

El juego completo (≈ $570.000) supera los $500.001, así que **aplica el envío
a domicilio**.

**Opcional: patas en lugar de zócalo.** La pata de acero diagonal de 100 mm
(Mobile, $2.394 c/u, cromada o negra) deja el mueble elevado y permite
**trapear por debajo**, que fue lo que dañó la cómoda anterior. Para la cómoda
son 4 patas ($9.576) y para la mesa otras 4 ($9.576); con eso sobran los
zócalos. Si la quieres, ajusto el diseño y los renders.

### Datos de madecentro.com que afectan la compra (sept. 2026)

- **Lámina blanca RH Primadera 2,15 × 2,44, 15 mm:** $266.410 (SKU AGPMRBS215).
  En la misma página se pueden pedir los **tableros cortados, con cantos y
  servicios incluidos**. Si tienes tarjeta de cliente Diamante, Oro o Plata,
  aplica el mismo descuento que en la tienda.
- **Bisagra de cazoleta cierre lento Bonuit (parche):** $3.137 **por par**,
  con 12 tornillos y 3 kg por par. Es la adecuada para la puerta de la cómoda:
  "parche" es la puerta que tapa el costado, y 1 par alcanza.
- **Canto flexible blanco 19 mm, rollo de 200 m:** $167.200. Para 15 mm sirve
  el de 19 o el de 22 mm. **No conviene comprar el rollo**: solo se necesitan
  ~35 m y pegarlo bien en casa es difícil. Mejor pide el **enchape en tienda**.
- **Envío:** llevan a domicilio en ciudades principales si la compra pasa de
  **$500.001**; si no, se recoge en un almacén. La entrega tarda de 3 a 8 días
  hábiles. Comprando **los dos muebles juntos** (≈ $680.000) sí aplica el
  envío; solo la cómoda (≈ $480.000) no alcanza. Revisa el pedido frente al
  transportador y reporta faltantes en 48 horas.

## Herrajes

| Herraje | Cant. | Nota |
|---|---|---|
| Riel extensión total carga media 38 kg (Mobile) **30 cm** | 2 pares | Cajón de 344 mm de ancho exterior; cada par trae 12 tornillos |
| Pomo de estrella | 2 | Uno centrado por cajón (o una manija como la Eter) |
| Tornillo de ensamble 6 × 2" | ~24 | De la misma caja × 100 de la cómoda |

No lleva bisagras ni necesita anclaje a la pared, porque es baja.

## Armado

1. Arma los 2 cajones y clava las bases de HDF por debajo.
2. Une los costados con el piso (a 70 mm del suelo), la repisa del nicho
   (su cara de arriba a 362 mm) y el travesaño trasero.
3. Clava el fondo de HDF para escuadrar.
4. Atornilla el zócalo retrocedido y la tapa desde el travesaño y la repisa.
5. Instala los rieles y los cajones, con 3 mm de holgura entre los frentes.
