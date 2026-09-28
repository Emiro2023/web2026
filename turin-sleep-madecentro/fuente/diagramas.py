# Dibujos de perforación (SVG) — medidas en mm
F='font-family="Liberation Sans, Arial, sans-serif"'
RED="#c0392b"; INK="#2b2622"; TEAL="#2f7d78"
def dim_v(x,y0,y1,label,side=1):
    return (f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="{RED}" stroke-width="1" marker-start="url(#a)" marker-end="url(#a)"/>'
            f'<text x="{x+6*side}" y="{(y0+y1)/2+4}" font-size="11" fill="{RED}" text-anchor="{"start" if side>0 else "end"}">{label}</text>')
def dim_h(y,x0,x1,label):
    return (f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{RED}" stroke-width="1" marker-start="url(#a)" marker-end="url(#a)"/>'
            f'<text x="{(x0+x1)/2}" y="{y-5}" font-size="11" fill="{RED}" text-anchor="middle">{label}</text>')
MARK='<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 2 L10 5 L0 8 z" fill="#c0392b"/></marker></defs>'
def costado(fname, title, W, H, bands, rails, rail_len, notes, rail_off=0, marks=()):
    """Cara interior de un costado. W=profundidad (frente a la derecha), H=alto. bands=(y0,y1,z0,z1,label) desde el piso/atrás."""
    s=0.55; px=90; py=40; w=W*s; h=H*s
    Y=lambda y: py+h-y*s; X=lambda z: px+z*s
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w+px+230} {h+py+50}" {F}>',MARK,
       f'<text x="{px}" y="18" font-size="13" font-weight="700" fill="{INK}">{title}</text>',
       f'<rect x="{px}" y="{py}" width="{w}" height="{h}" fill="#f4f1ec" stroke="{INK}" stroke-width="1.5"/>',
       f'<text x="{px+w+4}" y="{py+h+14}" font-size="10" fill="#777">FRENTE →</text><text x="{px-4}" y="{py+h+14}" font-size="10" fill="#777" text-anchor="end">← ATRÁS</text>']
    for y0,y1,z0,z1,lab in bands:
        o.append(f'<rect x="{X(z0)}" y="{Y(y1)}" width="{(z1-z0)*s}" height="{(y1-y0)*s}" fill="#cfe3e1" stroke="{INK}" stroke-width="0.8"/>')
        o.append(f'<text x="{X((z0+z1)/2)}" y="{Y(y1)-3}" font-size="10" text-anchor="middle" fill="{INK}">{lab}</text>')
        # tornillos (línea al centro del espesor)
        for zz in ([40,(W)/2,W-40] if z1-z0>200 else [(z0+z1)/2]):
            if z0<=zz<=z1: o.append(f'<circle cx="{X(zz)}" cy="{Y((y0+y1)/2)}" r="2.6" fill="{INK}"/>')
    for i,(yc,lab) in enumerate(rails):
        o.append(f'<rect x="{X(W-rail_off-rail_len)}" y="{Y(yc)-5}" width="{rail_len*s}" height="10" rx="2" fill="#b8bcc2" stroke="#666"/>')
        o.append(f'<line x1="{X(W-rail_off-rail_len)}" y1="{Y(yc)}" x2="{X(W-rail_off)}" y2="{Y(yc)}" stroke="{TEAL}" stroke-dasharray="4 3"/>')
        o.append(f'<text x="{px+w+10}" y="{Y(yc)+4}" font-size="11" fill="{TEAL}">{lab}: centro a {yc} mm</text>')
    for zz,yy,lab in marks:
        o.append(f'<rect x="{X(zz)-6}" y="{Y(yy)-9}" width="12" height="18" fill="#e6b089" stroke="#8a4b22"/>')
        o.append(f'<text x="{X(zz)-10}" y="{Y(yy)+4}" font-size="10" text-anchor="end" fill="#8a4b22">{lab}</text>')
    o.append(dim_v(px-30,py,py+h,f"{H}",-1)); o.append(dim_h(py+h+32,px,px+w,f"{W} mm"))
    for k,t in enumerate(notes): o.append(f'<text x="{px+w+10}" y="{py+h-50+k*15}" font-size="10" fill="#555">{t}</text>')
    o.append('</svg>'); open(fname,'w').write('\n'.join(o))
def panel(fname,title,W,H,holes,extra=[]):
    s=0.6 if W>400 else 0.8; px=60; py=36; w=W*s; h=H*s
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w+px+170} {h+py+46}" {F}>',MARK,
       f'<text x="{px}" y="18" font-size="13" font-weight="700" fill="{INK}">{title}</text>',
       f'<rect x="{px}" y="{py}" width="{w}" height="{h}" fill="#f4f1ec" stroke="{INK}" stroke-width="1.5"/>']
    for x,y,r,lab in holes:
        cx=px+x*s; cy=py+h-y*s
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{max(r*s,3)}" fill="none" stroke="{TEAL}" stroke-width="2"/>')
        o.append(f'<text x="{cx}" y="{cy-max(r*s,3)-4}" font-size="10" text-anchor="middle" fill="{TEAL}">{lab}</text>')
    o.append(dim_h(py+h+28,px,px+w,f"{W}")); o.append(dim_v(px-26,py,py+h,f"{H}",-1))
    for k,t in enumerate(extra): o.append(f'<text x="{px+w+12}" y="{py+14+k*15}" font-size="10" fill="#555">{t}</text>')
    o.append('</svg>'); open(fname,'w').write('\n'.join(o))
def caja(fname,title,Wb,Db,side,fb):
    s=0.6; px=40; py=34; w=Wb*s; d=Db*s
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w+px+190} {d+py+50}" {F}>',MARK,
       f'<text x="{px}" y="18" font-size="13" font-weight="700" fill="{INK}">{title}</text>',
       f'<rect x="{px}" y="{py}" width="{15*s}" height="{d}" fill="#cfe3e1" stroke="{INK}"/>',
       f'<rect x="{px+w-15*s}" y="{py}" width="{15*s}" height="{d}" fill="#cfe3e1" stroke="{INK}"/>',
       f'<rect x="{px+15*s}" y="{py}" width="{w-30*s}" height="{15*s}" fill="#f6d3bf" stroke="{INK}"/>',
       f'<rect x="{px+15*s}" y="{py+d-15*s}" width="{w-30*s}" height="{15*s}" fill="#f6d3bf" stroke="{INK}"/>',
       f'<text x="{px+w/2}" y="{py+d/2}" font-size="11" text-anchor="middle" fill="#555">base HDF por debajo</text>',
       f'<text x="{px+w/2}" y="{py+d+14}" font-size="10" text-anchor="middle" fill="#777">FRENTE</text>']
    o.append(dim_h(py+d+36,px,px+w,f"{Wb} mm exterior")); 
    for k,t in enumerate([f"Costados {side} (verde) por fuera",f"Frente/fondo {fb} (naranja) por dentro","2 tornillos 6×2\" por esquina","Verifica escuadra: diagonales","iguales antes de clavar la base.",f"Riel centrado en el costado","(a 55 mm del borde inferior)."]):
        o.append(f'<text x="{px+w+14}" y="{py+12+k*15}" font-size="10" fill="#555">{t}</text>')
    o.append('</svg>'); open(fname,'w').write('\n'.join(o))

costado("costado-turin.svg","Cómoda Turín · costados (cara interior)",400,820,
  [(0,15,0,400,"T3 piso"),(435,450,0,370,"T4 entrepaño"),(805,820,0,80,"T5"),(805,820,300,380,"T5")],
  [(738,"Riel cajón 1"),(553,"Riel cajón 2")],350,
  ["• Alturas desde el borde inferior","  del costado (sin patas)","• Rieles 35 cm a 17 mm del frente","• Bisagras (naranja): base a 52 mm","  del frente, alturas 117 y 333","• ● = tornillo 6×2\""],rail_off=17,
  marks=((348,117,"bisagra"),(348,333,"bisagra")))
costado("costado-sleep.svg","Nochero Sleep · costados (cara interior)",400,480,
  [(0,15,0,400,"N3 piso"),(275,290,0,400,"N4 repisa")],[],0,
  ["• Alturas desde el borde inferior","• Bisagras solo en el costado","  DERECHO: base a 52 mm del","  frente, alturas 77 y 213 mm","• Push-to-open: costado izquierdo,","  por dentro, a 150 mm","• ● = tornillo 6×2\""],
  marks=((348,77,"bisagra"),(348,213,"bisagra")))
panel("frente-t7.svg","T7 Frente de cajón embutido ×2",766,155,[(383,127,10,"cerradura (opcional, solo el de arriba)")],
 ["Sin manija: se abre por la","ranura de 30 mm entre frentes.","Luz de 2 mm con los costados.","Fija con 4 tornillos 6×1\"","desde dentro del cajón."])
panel("puerta-t8.svg","T8 Puerta embutida ×2 (derecha; izquierda en espejo)",382,416,[(382-22,100,17.5,"cazoleta"),(382-22,316,17.5,"cazoleta")],
 ["Cazoleta Ø35, 12 mm de","profundidad, centro a 22 mm","del borde de la bisagra,","a 100 mm de arriba y abajo.","Bisagra CODO (puerta","embutida) cierre lento.","Se abre tomando el borde","superior (ranura de 45 mm)."])
panel("puerta-n5.svg","N5 Puerta embutida · nochero",466,256,[(466-22,60,17.5,"cazoleta"),(466-22,196,17.5,"cazoleta"),(30,150,6,"imán push")],
 ["Cazoletas a 22 mm del borde","derecho y a 60 mm de arriba","y de abajo. Bisagra CODO","(sin cierre lento, para que","funcione el push-to-open).","Placa del push en la puerta,","a 30 mm del borde izquierdo."])
caja("caja-turin.svg","Caja de cajón · Turín (vista superior)",744,350,"T9 350×110","T10 714×110")
