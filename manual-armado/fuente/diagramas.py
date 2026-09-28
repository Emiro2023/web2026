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
def costado(fname, title, W, H, bands, rails, rail_len, notes):
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
        o.append(f'<rect x="{X(W-rail_len)}" y="{Y(yc)-5}" width="{rail_len*s}" height="10" rx="2" fill="#b8bcc2" stroke="#666"/>')
        o.append(f'<line x1="{X(W-rail_len)}" y1="{Y(yc)}" x2="{X(W)}" y2="{Y(yc)}" stroke="{TEAL}" stroke-dasharray="4 3"/>')
        o.append(f'<text x="{px+w+10}" y="{Y(yc)+4}" font-size="11" fill="{TEAL}">{lab}: centro a {yc} mm</text>')
    o.append(dim_v(px-30,py,py+h,f"{H}",-1)); o.append(dim_h(py+h+32,px,px+w,f"{W} mm"))
    for k,t in enumerate(notes): o.append(f'<text x="{px+w+10}" y="{py+h-50+k*15}" font-size="10" fill="#555">{t}</text>')
    o.append('</svg>'); open(fname,'w').write('\n'.join(o))
costado("costado-comoda.svg","Cómoda · costado izquierdo y división (cara interior)",380,785,
  [(118,133,0,380,"C3 piso"),(770,785,0,80,"C6 trav."),(770,785,300,380,"C6 trav.")],
  [(699,"Riel cajón 1"),(536,"Riel cajón 2"),(373,"Riel cajón 3"),(210,"Riel cajón 4")],350,
  ["• Rieles de 35 cm al ras del frente","• Alturas medidas desde el piso","• ● = tornillo 6×2\" (centro del canto)"])
costado("costado-mesa.svg","Mesa de noche · costados (cara interior)",358,492,
  [(70,85,0,358,"M3 piso"),(347,362,0,358,"M4 repisa nicho"),(412,492,0,15,"M6")],
  [(287,"Riel cajón 1"),(143,"Riel cajón 2")],300,
  ["• Rieles de 30 cm al ras del frente","• Alturas medidas desde el piso","• ● = tornillo 6×2\""])
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
panel("puerta-c9.svg","C9 Puerta · cara interior",277,649,[(277-22,100,17.5,"cazoleta"),(277-22,549,17.5,"cazoleta"),(37,327,3,"pomo")],
 ["Cazoleta Ø35 mm, 12 mm de","profundidad, centro a 22 mm","del borde derecho y a 100 mm","de arriba y de abajo.","Base en el costado derecho:","a 37 mm del frente, alturas","233 y 682 mm desde el piso.","Pomo: 37 mm del borde","izquierdo, 327 mm de abajo."])
panel("frente-c8.svg","C8 Frente de cajón (cómoda) ×4",590,160,[(145,80,3,"pomo"),(445,80,3,"pomo")],
 ["Pomos a 145 y 445 mm del","borde izquierdo, centrados","en altura (80 mm).","Fija el frente con 4 tornillos","6×1\" desde dentro del cajón."])
panel("frente-m7.svg","M7 Frente de cajón (mesa) ×2",397,141,[(198.5,70.5,3,"pomo")],
 ["Pomo centrado:","198 mm del borde, 70 mm","de altura.","4 tornillos 6×1\" desde dentro."])
# Caja de cajón (vista superior)
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
    for k,t in enumerate([f"Costados {side} (verde) por fuera",f"Frente/fondo {fb} (naranja) por dentro","2 tornillos 6×2\" por esquina","Verifica escuadra: diagonales","iguales antes de clavar la base.",f"Riel centrado en el costado",f"(a {55 if Wb>400 else 50} mm del borde inferior)."]):
        o.append(f'<text x="{px+w+14}" y="{py+12+k*15}" font-size="10" fill="#555">{t}</text>')
    o.append('</svg>'); open(fname,'w').write('\n'.join(o))
caja("caja-comoda.svg","Caja de cajón · cómoda (vista superior)",543,350,"C10 350×110","C11 513×110")
caja("caja-mesa.svg","Caja de cajón · mesa (vista superior)",344,300,"M8 300×100","M9 314×100")
print("ok")
