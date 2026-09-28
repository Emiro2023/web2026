# Genera guia.html (manual de corte y armado) a partir de piezas.json y los SVG/PNG de la carpeta.
import json, html
D = json.load(open("piezas.json"))
svg = lambda f: open(f).read()

def fila(p):
    pid, mueble, nombre, L, A, q, cantos = p
    c = " + ".join(str(x) for x in cantos) if cantos else "—"
    return f"<tr><td class='id'>{pid}</td><td>{html.escape(nombre)}</td><td class='n'>{q}</td><td class='n'>{L} × {A}</td><td class='c'>{c}</td></tr>"

def tabla(items, mueble):
    rows = "".join(fila(p) for p in items if p[1] == mueble)
    return f"<table><tr><th>ID</th><th>Pieza</th><th>Cant.</th><th>Medida (mm)</th><th>Canto en los bordes de (mm)</th></tr>{rows}</table>"

def tabla_hdf():
    rows = "".join(f"<tr><td class='id'>{p[0]}</td><td>{p[1]} · {p[2]}</td><td class='n'>{p[5]}</td><td class='n'>{p[3]} × {p[4]}</td></tr>" for p in D["HDF"])
    return f"<table><tr><th>ID</th><th>Pieza</th><th>Cant.</th><th>Medida (mm)</th></tr>{rows}</table>"

def paso(n, mueble, img, titulo, piezas, items, ojo=None):
    lis = "".join(f"<li>{t}</li>" for t in items)
    o = f"<div class='tip'>⚠ {ojo}</div>" if ojo else ""
    return f"""<div class='paso'><div class='pimg'><img src='{img}'><div class='pn'>{n}</div></div>
<div class='ptxt'><h3>{titulo}</h3><div class='pz'>Piezas: {piezas}</div><ol>{lis}</ol>{o}</div></div>"""

hw = D["hdf_fmt"]
HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Manual de corte y armado</title>
<style>
@page {{ size: A4; margin: 13mm 12mm 14mm; }}
:root {{ --ink:#2b2622; --muted:#6f655b; --teal:#2f7d78; --or:#d9793f; --line:#e2d9cb; --bg:#f6f2ec; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; font-family:"Liberation Sans","DejaVu Sans",Arial,sans-serif; color:var(--ink); font-size:10.5pt; line-height:1.38; }}
h1 {{ font-size:28pt; line-height:1.05; margin:0 0 6px; letter-spacing:-.01em; }}
h2 {{ font-size:16pt; margin:0 0 10px; padding-bottom:6px; border-bottom:3px solid var(--teal); }}
h2 .n {{ display:inline-block; background:var(--teal); color:#fff; border-radius:50%; width:28px; height:28px; text-align:center; line-height:28px; font-size:13pt; margin-right:8px; }}
h3 {{ font-size:12pt; margin:0 0 4px; }}
.page {{ page-break-after: always; }}
.page:last-child {{ page-break-after: auto; }}
.kick {{ color:var(--teal); font-weight:700; letter-spacing:.14em; text-transform:uppercase; font-size:9pt; }}
.sub {{ color:var(--muted); font-size:12pt; margin:0 0 12px; }}
.cover img {{ width:100%; border-radius:10px; }}
.kpis {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:12px 0; }}
.kpi {{ background:var(--bg); border-radius:10px; padding:10px 12px; }}
.kpi b {{ display:block; font-size:17pt; }}
.kpi span {{ color:var(--muted); font-size:8.5pt; text-transform:uppercase; letter-spacing:.06em; }}
table {{ width:100%; border-collapse:collapse; margin:6px 0 12px; font-size:9.5pt; }}
th {{ text-align:left; background:var(--bg); color:var(--muted); font-size:8pt; text-transform:uppercase; letter-spacing:.05em; padding:5px 6px; }}
td {{ padding:4px 6px; border-bottom:1px solid var(--line); vertical-align:top; }}
td.id {{ font-weight:700; color:var(--teal); white-space:nowrap; }}
td.n {{ white-space:nowrap; text-align:right; font-variant-numeric:tabular-nums; }}
td.c {{ font-size:8.8pt; color:#444; }}
.box {{ background:var(--bg); border-radius:10px; padding:10px 14px; margin:8px 0; }}
.tip {{ background:#fff3e8; border-left:4px solid var(--or); padding:6px 10px; margin-top:6px; font-size:9.5pt; border-radius:4px; }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
.fig svg {{ width:100%; height:auto; }} .r1 svg {{ max-height:98mm; }} .r2 svg {{ max-height:78mm; }} .r3 svg {{ max-height:46mm; }}
.paso {{ display:grid; grid-template-columns:34% 1fr; gap:10px; margin:0 0 7px; font-size:9.6pt; break-inside:avoid; border:1px solid var(--line); border-radius:10px; padding:8px; }}
.pimg {{ position:relative; }} .pimg img {{ width:100%; border-radius:8px; display:block; }}
.pn {{ position:absolute; left:6px; top:6px; background:var(--or); color:#fff; font-weight:800; border-radius:50%; width:28px; height:28px; text-align:center; line-height:28px; }}
.pz {{ font-size:9pt; color:var(--teal); font-weight:700; margin-bottom:3px; }}
ol, ul {{ margin:4px 0 0 18px; padding:0; }} li {{ margin:2px 0; }}
.check li {{ list-style:none; margin-left:-18px; }} .check li:before {{ content:"☐ "; }}
.small {{ font-size:8.8pt; color:var(--muted); }}
.legend span {{ display:inline-block; width:12px; height:12px; border:1px solid #333; vertical-align:-2px; margin:0 4px 0 12px; }}
</style></head><body>

<section class="page cover">
<div class="kick">Manual de corte y armado · Madecentro</div>
<h1>Cómoda + mesa de noche</h1>
<p class="sub">Melamina RH 15 mm · 1 sola lámina de 2,15 × 2,44 m · para armar en casa</p>
<img src="portada.png">
<div class="kpis">
 <div class="kpi"><b>90×80×40</b><span>cómoda (cm)</span></div>
 <div class="kpi"><b>40×50,7×37,3</b><span>mesa de noche (cm)</span></div>
 <div class="kpi"><b>{D['n_mel']} + {D['n_hdf']}</b><span>piezas melamina + HDF</span></div>
 <div class="kpi"><b>≈ $580.000</b><span>costo del juego (blanco)</span></div>
</div>
<div class="box"><b>Contenido:</b> 1. Compra · 2. Tablero y plano de corte · 3. Lista de piezas y cantos · 4. Herramientas ·
5. Medidas de perforación · 6. Armado de la cómoda paso a paso · 7. Armado de la mesa paso a paso · 8. Revisión final y cuidados</div>
<p class="small">Medidas en milímetros. Sierra de 4 mm y 10 mm de refilado por borde. Precios de madecentro.com (sept. 2026) marcados con 💲; el resto es estimado.</p>
</section>

<section class="page">
<h2><span class="n">1</span>Lista de compra</h2>
<table>
<tr><th>Producto</th><th>Cant.</th><th>Para qué</th><th>Precio</th></tr>
<tr><td>💲 Tablero aglomerado melamina <b>blanco RH Primadera 15 mm, 2,15 × 2,44 m</b> (SKU AGPMRBS215)</td><td class="n">1</td><td>Todas las piezas de los dos muebles</td><td class="n">$266.410</td></tr>
<tr><td>HDF 3 mm blanco ({hw[0]} × {hw[1]} mm o el formato que tengan)</td><td class="n">1</td><td>Fondos y bases de cajón</td><td class="n">≈ $55.000 – $85.000</td></tr>
<tr><td>Servicio de <b>corte</b> ({D['n_mel']} piezas) + <b>enchape</b> canto PVC blanco 19 o 22 mm (≈ {D['canto_m']:.0f} m)</td><td class="n">—</td><td>Se pide con la lámina ("tableros a la medida")</td><td class="n">≈ $125.000 – $245.000</td></tr>
<tr><td>💲 Riel corredera extensión total carga media 38 kg (Mobile) — <b>35 cm</b></td><td class="n">4 pares</td><td>Cajones cómoda (incluye 12 tornillos/par)</td><td class="n">desde $5.917 el par</td></tr>
<tr><td>💲 Mismo riel — <b>30 cm</b></td><td class="n">2 pares</td><td>Cajones mesa</td><td class="n">desde $5.917 el par</td></tr>
<tr><td>💲 Bisagra de cazoleta cierre lento Bonuit, aplicación <b>parche</b></td><td class="n">1 par</td><td>Puerta cómoda (incluye tornillos)</td><td class="n">$3.137</td></tr>
<tr><td>💲 Tornillo de ensamble <b>6 × 2"</b> zincado, caja × 100</td><td class="n">1 caja</td><td>Carcasas y cajas de cajón (se usan ≈ 90)</td><td class="n">$6.419</td></tr>
<tr><td>Tornillo <b>6 × 1"</b> (caja pequeña)</td><td class="n">≈ 40</td><td>Frentes de cajón y sobre de la cómoda</td><td class="n">≈ $5.000</td></tr>
<tr><td>💲 Cantonera 19 × 12 mm + tornillos 6 × 5/8"</td><td class="n">8</td><td>4 tapa mesa · 2 zócalo cómoda · 2 anclaje a la pared</td><td class="n">$296 c/u</td></tr>
<tr><td>Pines de repisa 5 mm · puntillas 3/4" · 2 tacos 6 mm con tornillo</td><td class="n">4 · ≈150 · 2</td><td>Repisa, fondos, anclaje</td><td class="n">≈ $8.000</td></tr>
<tr><td>Pomos (se pueden reusar las estrellas de la cómoda vieja)</td><td class="n">11</td><td>8 cajones cómoda, 1 puerta, 2 cajones mesa</td><td class="n">$0 si se reusan</td></tr>
</table>
<div class="grid2">
<div class="box"><b>Costo aproximado (blanco)</b><br>Cómoda ≈ <b>$415.000</b> · Mesa ≈ <b>$165.000</b><br>Juego ≈ <b>$580.000</b> (en Cartagena ≈ $680.000)</div>
<div class="box"><b>Envío:</b> Madecentro despacha a domicilio en ciudades principales por compras de más de <b>$500.001</b> (3 a 8 días hábiles). Revisa el pedido frente al transportador y reporta faltantes dentro de 48 horas.</div>
</div>
<div class="tip">Pide en la tienda que corten <b>las dos listas en la misma lámina</b> (ver plano). Si también perforan cazoletas de bisagra, pide la de la puerta C9 (medidas en la sección 5).</div>
</section>

<section class="page">
<h2><span class="n">2</span>Tablero y plano de corte</h2>
<p><b>Tablero:</b> aglomerado melamínico RH (resistente a la humedad del ambiente, no al agua directa), 15 mm,
laminado por las dos caras, formato 2150 × 2440 mm. Uso de la lámina: <b>{D['uso_mel']*100:.0f} %</b>.
<span class="legend"><span style="background:#cfe3e1"></span>Cómoda <span style="background:#f6d3bf"></span>Mesa</span></p>
<div class="fig">{svg('despiece-melamina.svg')}</div>
<div class="grid2" style="margin-top:8px">
<div class="fig">{svg('despiece-hdf.svg')}</div>
<div class="box small">Cortes tipo guillotina (de lado a lado), como los hace la seccionadora.
El optimizador de la tienda puede reacomodar las piezas; lo importante es que <b>todas caben</b> en una lámina.
Pide que marquen cada pieza con su ID (C1…C11, M1…M9, H1…H4) y que te entreguen los retazos.</div>
</div>
</section>

<section class="page">
<h2><span class="n">3</span>Lista de piezas y cantos</h2>
<p class="small">"Canto en los bordes de" indica la longitud de cada borde que se enchapa. Ejemplo: C2 lleva canto en su borde de 785 (frente) y en el de 380 (el que toca el piso, para protegerlo al trapear).</p>
<h3>Cómoda · melamina RH 15 mm</h3>{tabla(D['MEL'],'Cómoda')}
<h3>Mesa de noche · melamina RH 15 mm</h3>{tabla(D['MEL'],'Mesa')}
<h3>HDF 3 mm</h3>{tabla_hdf()}
<p class="small">Total de canto ≈ {D['canto_m']:.1f} m (pide ~{D['canto_m']*1.1:.0f} m con desperdicio).</p>
</section>

<section class="page">
<h2><span class="n">4</span>Herramientas y preparación</h2>
<div class="grid2">
<div><ul class="check">
<li>Taladro atornillador + broca para madera de 3 mm (guía) y avellanador</li>
<li>Broca de 5 mm (pines de repisa y pomos)</li>
<li>Broca Forstner o sierra copa de 35 mm (cazoletas; o pídelo en la tienda)</li>
<li>Puntas Phillips PH2</li><li>Martillo pequeño (puntillas del fondo)</li>
<li>Metro, escuadra, lápiz, cinta de enmascarar</li>
<li>2 prensas o sargentos (ayudan mucho)</li>
<li>Cinta doble faz (para ubicar frentes)</li>
<li>Separadores de 3 mm (cartón o monedas)</li>
</ul></div>
<div class="box">
<b>Antes de empezar</b>
<ol>
<li>Revisa que estén todas las piezas contra la lista (sección 3).</li>
<li>Marca cada pieza con su ID en cinta de enmascarar, en la cara que queda por dentro.</li>
<li>Arma sobre una superficie limpia y plana (una cobija o cartón protege la melamina).</li>
<li><b>Siempre perfora guía de 3 mm</b> antes de cada tornillo 6 × 2": el aglomerado se abre si no.</li>
<li>Los tornillos van al centro del espesor del tablero que recibe (7,5 mm del borde) y a 40 mm de las esquinas.</li>
<li>No aprietes de más: cuando el tornillo asienta, para.</li>
</ol></div>
</div>
<div class="grid2" style="margin-top:10px">
<img src="comoda-abierta.png" style="width:100%;border-radius:8px">
<img src="mesa-abierta.png" style="width:100%;border-radius:8px">
</div>
</section>

<section class="page">
<h2><span class="n">5</span>Medidas de perforación</h2>
<div class="grid2">
<div class="fig r1">{svg('costado-comoda.svg')}</div>
<div class="fig r1">{svg('costado-mesa.svg')}</div>
</div>
<div class="grid2">
<div class="fig r2">{svg('puerta-c9.svg')}</div>
<div><div class="fig r3">{svg('frente-c8.svg')}</div><div class="fig r3">{svg('frente-m7.svg')}</div></div>
</div>
<div class="grid2">
<div class="fig r3">{svg('caja-comoda.svg')}</div>
<div class="fig r3">{svg('caja-mesa.svg')}</div>
</div>
</section>

<section class="page">
<h2><span class="n">6</span>Armado de la cómoda paso a paso</h2>
{paso(1,'c','st-comoda-1.png','Arma las 4 cajas de cajón','C10 ×8 · C11 ×8 · H2 ×4',
 ['Pon C11 (513) entre dos C10 (350), con el canto hacia arriba.',
  '2 tornillos 6 × 2" por esquina (a 25 y 85 mm del borde inferior), con guía de 3 mm.',
  'Mide las diagonales: deben ser iguales. Si no, empuja la esquina larga.',
  'Clava la base H2 por debajo con puntillas cada 10 cm: la base deja la caja a escuadra.',
  'Medida exterior final: 543 × 350 × 110 mm.'])}
{paso(2,'c','st-comoda-2.png','Arma la carcasa','C2 ×2 · C3 · C4 · C6 ×2',
 ['Con los costados C2 acostados, marca en su cara interior la línea del piso a 118–133 mm del borde inferior.',
  'Atornilla el piso C3 entre los costados (3 tornillos por lado, en la línea 125 mm).',
  'Coloca la división C4 a <b>569 mm libres</b> del costado izquierdo; atorníllala desde abajo del piso (3 tornillos).',
  'Atornilla los travesaños C6 acostados arriba (a ras del borde superior): uno al frente y otro atrás, 2 tornillos por extremo.',
  'Une la división a cada travesaño con 1 tornillo desde arriba.'],
 'Los travesaños quedan planos (80 mm hacia adentro), no parados.')}
{paso(3,'c','st-comoda-3.png','Clava el fondo (vista de atrás)','H1',
 ['Voltea la carcasa boca abajo. Mide las diagonales y corrige hasta que sean iguales.',
  'Apoya H1 (870 × 785) con la cara blanca hacia adentro, a ras de los bordes.',
  'Clava puntillas 3/4" cada 10–15 cm en costados, piso, división y travesaño trasero.'],
 'El fondo es lo que deja el mueble a escuadra: no lo claves torcido.')}
{paso(4,'c','st-comoda-4.png','Zócalo y sobre','C7 · C1 · 2 cantoneras',
 ['Pon el zócalo C7 bajo el piso, <b>20 mm hacia adentro</b> del frente; atorníllalo por los costados (2 por lado) y con 2 cantoneras al piso.',
  'Pon la carcasa de pie. Centra el sobre C1: sobresale 15 mm a cada lado, 20 mm al frente, y queda a ras atrás.',
  'Atorníllalo desde abajo a través de los travesaños con tornillos 6 × 1" (4 por travesaño).'])}
</section>

<section class="page">
{paso(5,'c','st-comoda-5.png','Rieles e instalación de cajones','4 pares rieles 35 cm',
 ['Separa cada riel en dos (palanca negra). La parte grande va al mueble y la pequeña a la caja.',
  'En el costado izquierdo y en la división traza las líneas de centro a <b>699, 536, 373 y 210 mm</b> desde el piso.',
  'Atornilla la parte grande con su borde delantero a ras del frente del mueble.',
  'En cada caja, atornilla la parte pequeña centrada en el costado (55 mm del borde inferior), a ras del frente.',
  'Mete las cajas: deben deslizar sin rozar.'])}
{paso(6,'c','st-comoda-6.png','Frentes, puerta, repisa y anclaje','C8 ×4 · C9 · C5 · bisagras · pomos',
 ['Frentes C8: empieza por el de abajo. Pégalo con doble faz dejando 3 mm entre frentes (usa separadores); luego abre el cajón y fíjalo con 4 tornillos 6 × 1" desde dentro.',
  'Perfora los pomos (145 y 445 mm del borde izquierdo, a media altura).',
  'Puerta C9: cazoletas Ø35 a 22 mm del borde derecho y 100 mm de arriba/abajo. Bases en el costado derecho a 37 mm del frente (alturas 233 y 682 mm). Engancha y ajusta los 3 tornillos de la bisagra hasta que la luz sea pareja.',
  'Repisa C5: 4 perforaciones de 5 mm (37 mm del frente y 50 mm de atrás) a la altura que quieras; pon los pines.',
  '<b>Ancla la cómoda a la pared</b> con 2 cantoneras al travesaño trasero, con taco y tornillo.'],
 'Con niños es obligatorio anclarla: una cómoda con los cajones abiertos se puede voltear.')}
</section>

<section class="page">
<h2><span class="n">7</span>Armado de la mesa de noche paso a paso</h2>
{paso(1,'m','st-mesa-1.png','Arma las 2 cajas de cajón','M8 ×4 · M9 ×4 · H4 ×2',
 ['M9 (314) entre dos M8 (300), canto arriba; 2 tornillos 6 × 2" por esquina.',
  'Revisa diagonales y clava la base H4 por debajo.','Medida exterior: 344 × 300 × 100 mm.'])}
{paso(2,'m','st-mesa-2.png','Arma la carcasa','M2 ×2 · M3 · M4 · M6',
 ['Piso M3 entre los costados con su cara de abajo a <b>70 mm</b> del piso (tornillos en la línea de 77 mm).',
  'Repisa del nicho M4 con su cara de arriba a <b>362 mm</b> (tornillos en la línea de 354 mm).',
  'Travesaño M6 parado atrás, arriba (412–492 mm), a ras del borde trasero: 2 tornillos por lado.'])}
{paso(3,'m','st-mesa-3.png','Clava el fondo (vista de atrás)','H3',
 ['Escuadra por diagonales y clava H3 (492 × 400) con puntillas cada 10 cm.'])}
{paso(4,'m','st-mesa-4.png','Zócalo y tapa','M5 · M1 · 4 cantoneras',
 ['Zócalo M5 bajo el piso, 20 mm hacia adentro; 2 tornillos por costado.',
  'Tapa M1 a ras de costados, atrás y del frente de los cajones (sobresale 15 mm del mueble).',
  'Fíjala desde adentro del nicho con 4 cantoneras (2 adelante, 2 atrás) y tornillos 6 × 5/8".'])}
</section>

<section class="page">
{paso(5,'m','st-mesa-5.png','Rieles e instalación de cajones','2 pares rieles 30 cm',
 ['En los dos costados traza las líneas de centro a <b>287 y 143 mm</b> desde el piso.',
  'Parte grande del riel a ras del frente; parte pequeña centrada en la caja (50 mm del borde inferior).',
  'Mete las cajas y prueba que deslicen.'])}
{paso(6,'m','st-mesa-6.png','Frentes y pomos','M7 ×2 · 2 pomos',
 ['Frente de abajo primero: el borde inferior queda a 73 mm del piso; 3 mm entre frentes.',
  'Doble faz, abre el cajón y fija con 4 tornillos 6 × 1" desde dentro.',
  'Pomo centrado (198 mm del borde, 70 mm de altura).'])}

<h2 style="margin-top:14px"><span class="n">8</span>Revisión final y cuidados</h2>
<div class="grid2">
<ul class="check">
<li>Todos los cajones abren completos y cierran sin rozar</li>
<li>Luz pareja de 3 mm entre frentes; la puerta cierra alineada</li>
<li>La cómoda está anclada a la pared</li>
<li>No quedan puntas de tornillo salidas por dentro de los cajones</li>
<li>Guarda los retazos: sirven para repisas extra o reparaciones</li>
</ul>
<div class="box small">
<b>Cuidados de la melamina RH:</b> resiste manchas, rayas y alcohol, pero <b>no el agua directa</b>.
Al trapear, escurre bien el trapeador y no dejes agua junto al zócalo. Limpia con paño húmedo y jabón suave.
Si un canto se despega, pégalo con pegante de contacto.<br><br>
<b>Ajustes:</b> los rieles tienen ranuras alargadas para subir o bajar el cajón unos milímetros; las bisagras se ajustan con sus 3 tornillos.
</div>
</div>
</section>
</body></html>"""
open("guia.html", "w").write(HTML)
print("ok", len(HTML))
