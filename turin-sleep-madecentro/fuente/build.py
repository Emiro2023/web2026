# Manual de corte y armado: réplicas de la Cómoda Turín (Just Home Collection) y el Nochero Sleep S-52 (Rta Design)
import json, html
D = json.load(open("piezas.json"))
svg = lambda f: open(f).read()

def tabla(mueble):
    rows = "".join(
        f"<tr><td class='id'>{p[0]}</td><td>{html.escape(p[2])}</td><td class='n'>{p[5]}</td><td class='n'>{p[3]} × {p[4]}</td>"
        f"<td class='c'>{' + '.join(str(x) for x in p[6]) if p[6] else '—'}</td></tr>" for p in D["MEL"] if p[1] == mueble)
    return f"<table><tr><th>ID</th><th>Pieza</th><th>Cant.</th><th>Medida (mm)</th><th>Canto en los bordes de (mm)</th></tr>{rows}</table>"

def paso(n, img, titulo, piezas, items, ojo=None):
    lis = "".join(f"<li>{t}</li>" for t in items)
    o = f"<div class='tip'>⚠ {ojo}</div>" if ojo else ""
    return (f"<div class='paso'><div class='pimg'><img src='{img}'><div class='pn'>{n}</div></div>"
            f"<div class='ptxt'><h3>{titulo}</h3><div class='pz'>Piezas: {piezas}</div><ol>{lis}</ol>{o}</div></div>")

def uniones(rows):
    tr = "".join(f"<tr><td>{a}</td><td class='id'>{b}</td><td>{c}</td><td class='n'>{d}</td><td class='c'>{e}</td></tr>" for a, b, c, d, e in rows)
    return f"<table><tr><th>Unión</th><th>Piezas</th><th>Herraje</th><th>Cant.</th><th>Cómo</th></tr>{tr}</table>"

CSS = open("../doc/guia.html").read().split("<style>")[1].split("</style>")[0]
canto = D["canto_T"] + D["canto_N"]

HTML = f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Manual Turín + Sleep</title><style>{CSS}</style></head><body>

<section class="page cover">
<div class="kick">Manual de corte y armado · réplicas para fabricar con Madecentro</div>
<h1>Cómoda Turín + nochero Sleep</h1>
<p class="sub">Melamina RH 15 mm · <b>1 sola lámina</b> de 2,15 × 2,44 m · frentes embutidos, sin manijas, sobre patas</p>
<img src="set2-hero.png">
<div class="kpis">
 <div class="kpi"><b>80×86×40</b><span>cómoda Turín (cm)</span></div>
 <div class="kpi"><b>50×52×40</b><span>nochero Sleep (cm)</span></div>
 <div class="kpi"><b>{D['nT']} + {D['nN']}</b><span>piezas de melamina</span></div>
 <div class="kpi"><b>≈ $535.000</b><span>el juego (blanco)</span></div>
</div>
<div class="box"><b>Contenido:</b> 1. Los originales y comparación de precio · 2. Compra · 3. Tablero y plano de corte ·
4. Lista de piezas y cantos · 5. Uniones: cómo se fija cada pieza · 6. Medidas de perforación · 7. Armado de la cómoda ·
8. Armado del nochero · 9. Herramientas, revisión y cuidados</div>
<p class="small">Medidas en mm. Sierra 4 mm, refilado 10 mm por borde. 💲 = precio visto en madecentro.com u homecenter.com.co (sept. 2026); lo demás es estimado.</p>
</section>

<section class="page">
<h2><span class="n">1</span>Los originales y comparación de precio</h2>
<div class="grid2">
<div><img src="turin-open.png" style="width:100%;border-radius:8px">
<h3>Cómoda Turín · Just Home Collection</h3>
<p class="small">Homecenter, código 628936 · 80 × 86 × 40 cm · Niebla Blanco o madera · <b>2 cajones</b> (el de arriba con cerradura) +
<b>2 puertas</b> con repisa · frentes embutidos sin manijas (se abren por las ranuras) · patas pequeñas. 💲 $449.900 (armado opcional $92.900).</p></div>
<div><img src="sleep-open.png" style="width:100%;border-radius:8px">
<h3>Nochero Velador Sleep S-52 · Rta Design</h3>
<p class="small">Homecenter, código 677789, modelo MDB 7222 · alto 52, ancho 50, fondo 40 cm · nicho abierto arriba +
<b>1 puerta embutida</b> (bisagras a la derecha) sin manija · 4 patas negras · Duna por fuera, blanco por dentro. 💲 $174.900 (antes $289.900).</p></div>
</div>
<table>
<tr><th>Mueble</th><th>Comprado en Homecenter</th><th>Fabricado (estimado)</th><th>Ahorro</th></tr>
<tr><td>Cómoda Turín</td><td class="n">$449.900</td><td class="n"><b>≈ $405.000</b> ($355.000 – $455.000)</td><td class="n">≈ $45.000</td></tr>
<tr><td>Nochero Sleep (del sobrante de la misma lámina)</td><td class="n">$174.900</td><td class="n"><b>≈ $130.000</b> ($115.000 – $150.000)</td><td class="n">≈ $45.000</td></tr>
<tr><td><b>Juego</b></td><td class="n"><b>$624.800</b></td><td class="n"><b>≈ $535.000</b> ($470.000 – $605.000)</td><td class="n"><b>≈ $90.000 (14 %)</b></td></tr>
</table>
<div class="box small"><b>Ventajas de fabricarlo:</b> tablero <b>RH</b> (resiste humedad), rieles metálicos de balineras, bisagras de cierre lento,
canto en los bordes de abajo y el mismo color en los dos muebles.<br>
<b>Ojo:</b> un <b>segundo nochero</b> ya no cabe en la lámina; hacerlo solo cuesta ≈ $290.000, así que si quieres dos, el segundo sale mejor comprado.
El original es bicolor (Duna por fuera, blanco por dentro): eso exigiría 2 láminas; aquí se propone todo de un color.</div>
</section>

<section class="page">
<h2><span class="n">2</span>Lista de compra</h2>
<table>
<tr><th>Producto</th><th>Cant.</th><th>Para qué</th><th>Precio</th></tr>
<tr><td>💲 Tablero melamina <b>blanco RH Primadera 15 mm, 2,15 × 2,44 m</b> (SKU AGPMRBS215)</td><td class="n">1</td><td>Todas las piezas de los dos muebles</td><td class="n">$266.410</td></tr>
<tr><td>HDF 3 mm blanco 1,83 × 2,44 m</td><td class="n">1</td><td>Fondos (2) y bases de cajón (2)</td><td class="n">≈ $55.000 – $85.000</td></tr>
<tr><td>Corte ({D['nT']+D['nN']} piezas) + enchape canto PVC blanco 19/22 mm (≈ {canto*1.1:.0f} m)</td><td class="n">—</td><td>"Tableros a la medida" en la web o en tienda</td><td class="n">≈ $90.000 – $170.000</td></tr>
<tr><td>💲 Riel extensión total carga media 38 kg (Mobile) <b>35 cm</b></td><td class="n">2 pares</td><td>Cajones cómoda</td><td class="n">desde $5.917 el par</td></tr>
<tr><td>💲 Bisagra cazoleta cierre lento Bonuit, aplicación <b>codo</b> (puerta embutida)</td><td class="n">2 pares</td><td>Puertas de la cómoda</td><td class="n">$3.137 el par*</td></tr>
<tr><td>💲 Bisagra cazoleta eco slide on (Mobile), <b>codo</b>, sin cierre lento</td><td class="n">2</td><td>Puerta del nochero (con push)</td><td class="n">$1.707 c/u</td></tr>
<tr><td>💲 Dispositivo push to open con imán (Bonuit)</td><td class="n">1</td><td>Abrir la puerta del nochero sin manija</td><td class="n">$3.030</td></tr>
<tr><td>💲 Tornillo de ensamble <b>6 × 2"</b> zincado, caja × 100</td><td class="n">1 caja</td><td>Carcasas y cajas (≈ 50)</td><td class="n">$6.419</td></tr>
<tr><td>Tornillo <b>6 × 1"</b></td><td class="n">≈ 16</td><td>Frentes de cajón y tapa de la cómoda</td><td class="n">≈ $5.000</td></tr>
<tr><td>💲 Cantonera 19 × 12 mm + tornillo 6 × 5/8"</td><td class="n">6</td><td>4 tapa nochero · 2 anclaje cómoda</td><td class="n">$296 c/u</td></tr>
<tr><td>Pata plástica negra ≈ 25 mm (con tornillo)</td><td class="n">8</td><td>4 por mueble</td><td class="n">≈ $1.500 – $3.000 c/u</td></tr>
<tr><td>Pines de repisa 5 mm · puntillas 3/4" · 2 tacos 6 mm · tapatornillos</td><td class="n">4 · ≈120 · 2 · ≈20</td><td>Repisa, fondos, anclaje</td><td class="n">≈ $8.000</td></tr>
<tr><td>Cerradura para cajón (opcional, como el original)</td><td class="n">1</td><td>Cajón superior</td><td class="n">≈ $10.000 – $20.000</td></tr>
</table>
<p class="small">* $3.137 es el precio de la versión "parche"; en el selector de la página elige <b>codo</b> (puerta embutida) y confirma el precio.
Si no hay codo con cierre lento, usa la eco slide on codo de Mobile.</p>
<div class="tip">El juego (≈ $535.000) supera los $500.001: aplica el envío a domicilio de Madecentro en ciudades principales.</div>
</section>

<section class="page">
<h2><span class="n">3</span>Tablero y plano de corte</h2>
<p><b>Tablero:</b> aglomerado melamínico RH 15 mm, laminado por las dos caras, 2150 × 2440 mm. Las {D['nT']+D['nN']} piezas caben en
<b>una lámina</b> (uso {D['uM']*100:.0f} %). <span class="legend"><span style="background:#cfe3e1"></span>Cómoda <span style="background:#f6d3bf"></span>Nochero</span></p>
<div class="fig">{svg('despiece-melamina.svg')}</div>
<div class="grid2" style="margin-top:8px">
<div class="fig">{svg('despiece-hdf.svg')}</div>
<div class="box small">Cortes tipo guillotina, como los de la seccionadora. Pide que corten <b>las dos listas en la misma lámina</b>,
que marquen cada pieza con su ID (T1…T10, N1…N5, TH, NH) y que te entreguen los retazos.<br><br>
Los frentes y puertas son <b>embutidos</b>: van <b>dentro</b> del mueble, con 2 mm de luz. Por eso sus medidas son exactas; revisa que
la tienda las corte bien antes de enchapar.</div>
</div>
</section>

<section class="page">
<h2><span class="n">4</span>Lista de piezas y cantos</h2>
<h3>Cómoda Turín · melamina RH 15 mm</h3>{tabla('Cómoda')}
<h3>Nochero Sleep · melamina RH 15 mm</h3>{tabla('Nochero')}
<h3>HDF 3 mm</h3>
<table><tr><th>ID</th><th>Pieza</th><th>Cant.</th><th>Medida (mm)</th></tr>
<tr><td class='id'>TH1</td><td>Cómoda · fondo</td><td class='n'>1</td><td class='n'>820 × 800</td></tr>
<tr><td class='id'>TH2</td><td>Cómoda · base de cajón</td><td class='n'>2</td><td class='n'>744 × 350</td></tr>
<tr><td class='id'>NH1</td><td>Nochero · fondo</td><td class='n'>1</td><td class='n'>500 × 480</td></tr></table>
<p class="small">Canto: cómoda ≈ {D['canto_T']:.1f} m · nochero ≈ {D['canto_N']:.1f} m (pide +10 %).</p>
<div class="grid2"><img src="turin-front.png" style="width:100%;border-radius:8px"><img src="sleep-front.png" style="width:100%;border-radius:8px"></div>
</section>

<section class="page">
<h2><span class="n">5</span>Uniones: cómo se fija cada pieza</h2>
<div class="box small"><b>Sistema recomendado: tornillo de ensamble 6 × 2" directo.</b> Atraviesa la pieza de 15 mm y entra 35 mm en el canto
de la otra. Siempre con <b>guía de 3 mm</b> y avellanado, al centro del espesor (7,5 mm de la línea de unión) y a 40 mm de las esquinas.
Las cabezas visibles en los costados se cubren con <b>tapatornillos adhesivos</b>.<br>
<b>Alternativa como el original (RTA):</b> los muebles armables usan <b>minifix</b> (excéntrica + perno) y <b>tarugos de 8 × 30 mm</b>; la unión
queda invisible y se puede desarmar, pero hay que perforar con la plantilla del minifix. Si la usas, cambia cada tornillo de carcasa por 1 minifix + 1 tarugo.</div>
<h3>Cómoda Turín</h3>
{uniones([
 ("Costado ↔ piso", "T2 + T3", "Tornillo 6 × 2&quot;", "3 por lado", "Piso al ras del borde inferior: línea a 7 mm"),
 ("Costado ↔ entrepaño", "T2 + T4", "Tornillo 6 × 2&quot;", "3 por lado", "Línea a 442 mm del borde inferior; entrepaño 30 mm hacia atrás"),
 ("Costado ↔ travesaños", "T2 + T5", "Tornillo 6 × 2&quot;", "2 por extremo (8)", "Acostados arriba, línea a 812 mm; delantero 20 mm atrás del frente"),
 ("Tapa ↔ travesaños", "T1 + T5", "Tornillo 6 × 1&quot;", "4 por travesaño (8)", "Desde abajo: no se ven"),
 ("Fondo", "TH1", "Puntilla 3/4&quot;", "cada 10–15 cm", "Escuadra el mueble"),
 ("Patas", "piso T3", "Pata + su tornillo", "4", "A 40 mm de cada esquina"),
 ("Caja de cajón", "T9 + T10", "Tornillo 6 × 2&quot;", "8 por caja (16)", "2 por esquina desde el costado"),
 ("Base de cajón", "TH2", "Puntilla 3/4&quot;", "cada 10 cm", "Por debajo"),
 ("Rieles", "costados + cajas", "Tornillos del riel", "incluidos", "A 17 mm del frente (detrás del frente embutido)"),
 ("Frente ↔ caja", "T7 + T10", "Tornillo 6 × 1&quot;", "4 por frente (8)", "Desde dentro, con 2 mm de luz alrededor"),
 ("Puertas", "T8 + T2", "Bisagra codo cierre lento", "2 pares", "Cada puerta en su costado exterior"),
 ("Repisa interior", "T6", "Pin 5 mm", "4", "Altura regulable"),
 ("Anclaje a la pared", "T5 trasero", "Cantonera + taco 6 mm", "2", "Obligatorio con niños"),
])}
<h3>Nochero Sleep</h3>
{uniones([
 ("Costado ↔ piso", "N2 + N3", "Tornillo 6 × 2&quot;", "3 por lado", "Línea a 7 mm del borde inferior"),
 ("Costado ↔ repisa", "N2 + N4", "Tornillo 6 × 2&quot;", "3 por lado", "Línea a 282 mm del borde inferior"),
 ("Tapa ↔ carcasa", "N1", "Cantonera 19 × 12", "4", "Dentro del nicho (2 adelante, 2 atrás)"),
 ("Fondo", "NH1", "Puntilla 3/4&quot;", "cada 10 cm", "Rigidiza el mueble (no lleva travesaño)"),
 ("Patas", "piso N3", "Pata + su tornillo", "4", "A 40 mm de cada esquina"),
 ("Puerta ↔ costado derecho", "N5 + N2", "Bisagra codo eco", "2", "Sin cierre lento (por el push)"),
 ("Apertura", "N5 + N2 izq.", "Push to open con imán", "1", "Costado izquierdo, por dentro"),
])}
</section>

<section class="page">
<h2><span class="n">6</span>Medidas de perforación</h2>
<div class="grid2">
<div class="fig r1">{svg('costado-turin.svg')}</div>
<div class="fig r1">{svg('costado-sleep.svg')}</div>
</div>
<div class="grid2">
<div class="fig r2">{svg('puerta-t8.svg')}</div>
<div><div class="fig r3">{svg('frente-t7.svg')}</div><div class="fig r3">{svg('puerta-n5.svg')}</div></div>
</div>
<div class="fig r3" style="max-width:60%">{svg('caja-turin.svg')}</div>
</section>

<section class="page">
<h2><span class="n">7</span>Armado de la cómoda Turín</h2>
{paso(1,'st-turin-1.png','Arma las 2 cajas de cajón','T9 ×4 · T10 ×4 · TH2 ×2',
 ['T10 (714) entre dos T9 (350), canto hacia arriba; 2 tornillos 6 × 2" por esquina.','Diagonales iguales → clava la base TH2 por debajo.',
  'Medida final: 744 × 350 × 110 mm.'])}
{paso(2,'st-turin-2.png','Arma la carcasa','T2 ×2 · T3 · T4 · T5 ×2',
 ['Piso T3 al ras del borde inferior de los costados (3 tornillos por lado).',
  'Entrepaño T4 con su cara de arriba a 450 mm del borde inferior, <b>30 mm hacia atrás</b> del frente (deja la ranura para abrir las puertas).',
  'Travesaños T5 acostados arriba: el delantero 20 mm hacia atrás (queda detrás del cajón embutido) y el trasero al ras de atrás.'])}
{paso(3,'st-turin-3.png','Fondo (vista de atrás)','TH1',['Boca abajo, escuadra por diagonales y clava TH1 (820 × 800) cada 10–15 cm.'],
 'Si el fondo queda torcido, los frentes embutidos no cierran parejo.')}
{paso(4,'st-turin-4.png','Patas y tapa','T1 · 4 patas',
 ['Atornilla las 4 patas bajo el piso, a 40 mm de las esquinas.',
  'De pie: tapa T1 a ras de costados, frente y atrás; fíjala desde abajo con tornillos 6 × 1" a través de los travesaños.'])}
</section>

<section class="page">
{paso(5,'st-turin-5.png','Rieles y cajones','2 pares rieles 35 cm',
 ['Líneas de centro en ambos costados a <b>738 y 553 mm</b> del borde inferior del costado.',
  'Riel a <b>17 mm del borde frontal</b> (el frente embutido ocupa esos 15 mm + 2 de luz).','En la caja: riel centrado (55 mm del borde inferior), a ras del frente de la caja.'])}
{paso(6,'st-turin-6.png','Frentes, puertas, repisa y anclaje','T7 ×2 · T8 ×2 · T6',
 ['Frentes T7: con los cajones cerrados, ubícalos con 2 mm de luz a los lados (separadores), doble faz, abre y fija con 4 tornillos 6 × 1".',
  'Cerradura (opcional) en el frente de arriba: centrada, a 28 mm del borde superior.',
  'Puertas T8: cazoletas Ø35 a 22 mm del borde de la bisagra; bases en cada costado a 52 mm del frente (alturas 117 y 333 mm). Ajusta hasta tener 2 mm de luz.',
  'Repisa T6 sobre 4 pines. <b>Ancla la cómoda a la pared</b> con 2 cantoneras al travesaño trasero.'])}
<h2 style="margin-top:10px"><span class="n">8</span>Armado del nochero Sleep</h2>
{paso(1,'st-sleep-2.png','Carcasa','N2 ×2 · N3 · N4',
 ['Piso N3 al ras del borde inferior (3 tornillos por lado).','Repisa N4 con su cara de arriba a 290 mm del borde inferior (línea de tornillos a 282 mm).'])}
</section>

<section class="page">
{paso(2,'st-sleep-3.png','Fondo (vista de atrás)','NH1',['Escuadra por diagonales y clava NH1 (500 × 480) cada 10 cm: es lo que rigidiza el mueble.'])}
{paso(3,'st-sleep-4.png','Patas y tapa','N1 · 4 patas · 4 cantoneras',
 ['4 patas bajo el piso a 40 mm de las esquinas.','Tapa N1 a ras por todos los lados; fíjala con 4 cantoneras dentro del nicho.'])}
{paso(4,'st-sleep-6.png','Puerta con push','N5 · 2 bisagras codo · push',
 ['Cazoletas a 22 mm del borde derecho y a 60 mm de arriba y abajo.','Bases en el costado derecho a 52 mm del frente, alturas 77 y 213 mm.',
  'Push-to-open en el costado izquierdo por dentro, a ≈150 mm; placa metálica en la puerta. Ajusta para que la puerta quede al ras.'],
 'Con push se usan bisagras sin cierre lento: el cierre lento impide que el push empuje la puerta.')}
<div class="grid2" style="margin-top:6px">
<div><img src="sleep-color.png" style="width:100%;border-radius:8px"><p class="small">Nochero en color madera clara (tipo Duna).</p></div>
<div><img src="set2-color.png" style="width:100%;border-radius:8px"><p class="small">Juego en madera clara.</p></div>
</div>
</section>

<section class="page">
<h2><span class="n">9</span>Herramientas, revisión y cuidados</h2>
<div class="grid2">
<div><h3>Herramientas</h3><ul class="check">
<li>Taladro + broca 3 mm (guía) y avellanador</li><li>Broca 5 mm (pines) y 20 mm si pones cerradura</li>
<li>Broca Forstner 35 mm (cazoletas) o pedir perforación en tienda</li><li>Puntas PH2, martillo, metro, escuadra</li>
<li>2 prensas, cinta doble faz, separadores de 2 mm (para frentes embutidos)</li></ul>
<h3>Revisión</h3><ul class="check">
<li>Cajones y puertas con luz pareja de 2 mm, sin rozar</li><li>El push abre la puerta del nochero con un toque</li>
<li>Cómoda anclada a la pared</li><li>Patas firmes (el mueble no cojea)</li><li>Tapatornillos puestos</li></ul></div>
<div class="box small"><b>Cuidados:</b> la melamina RH resiste la humedad del ambiente, manchas y rayas, pero no el agua directa.
Las patas dejan el mueble 25 mm arriba del piso: al trapear no se moja el aglomerado.<br><br>
<b>Frentes embutidos:</b> son más exigentes que los superpuestos. Si el mueble no está a escuadra se nota en la luz. Por eso el fondo va
clavado con el mueble bien escuadrado.<br><br>
<b>Fuentes:</b> Homecenter (Cómoda Turín 4 cajones 80×86×40, cód. 628936, $449.900; Nochero Velador Sleep S-52, cód. 677789, $174.900),
madecentro.com (lámina, rieles, bisagras, push, tornillos, cantoneras). Verifica precios antes de comprar.</div>
</div>
<img src="turin-color.png" style="width:58%;display:block;margin:10px auto;border-radius:8px">
</section>
</body></html>"""
open("guia.html", "w").write(HTML)
print("ok")
