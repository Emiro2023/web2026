"""Lista de piezas y despiece (guillotina) de la cómoda + mesa de noche.
Genera piezas.json, despiece-melamina.svg y despiece-hdf.svg."""
import json
K, TRIM = 4, 10  # sierra y refilado por borde (mm)
# id, mueble, nombre, largo, ancho, cant, cantos (lista de longitudes de borde a enchapar por pieza)
MEL = [
 ("C1","Cómoda","Sobre (tapa)",900,400,1,[900,900,400,400]),
 ("C2","Cómoda","Costado",785,380,2,[785,380]),
 ("C3","Cómoda","Piso",840,380,1,[840]),
 ("C4","Cómoda","División",637,380,1,[637]),
 ("C5","Cómoda","Repisa (puerta)",360,256,1,[256]),
 ("C6","Cómoda","Travesaño superior",840,80,2,[]),
 ("C7","Cómoda","Zócalo",840,118,1,[840]),
 ("C8","Cómoda","Frente de cajón",590,160,4,[590,590,160,160]),
 ("C9","Cómoda","Puerta",649,277,1,[649,649,277,277]),
 ("C10","Cómoda","Costado de cajón",350,110,8,[350]),
 ("C11","Cómoda","Frente/fondo interno de cajón",513,110,8,[513]),
 ("M1","Mesa","Tapa",400,373,1,[400,400,373,373]),
 ("M2","Mesa","Costado",492,358,2,[492,358]),
 ("M3","Mesa","Piso",370,358,1,[370]),
 ("M4","Mesa","Repisa del nicho",370,358,1,[370]),
 ("M5","Mesa","Zócalo",370,70,1,[370]),
 ("M6","Mesa","Travesaño trasero",370,80,1,[]),
 ("M7","Mesa","Frente de cajón",397,141,2,[397,397,141,141]),
 ("M8","Mesa","Costado de cajón",300,100,4,[300]),
 ("M9","Mesa","Frente/fondo interno de cajón",314,100,4,[314]),
]
HDF = [
 ("H1","Cómoda","Fondo",870,785,1,[]),
 ("H2","Cómoda","Base de cajón",543,350,4,[]),
 ("H3","Mesa","Fondo",492,400,1,[]),
 ("H4","Mesa","Base de cajón",344,300,2,[]),
]
def pack(items, W, H):
    W -= 2*TRIM; H -= 2*TRIM
    pcs=[(pid,a,b) for pid,_,_,a,b,q,_ in items for _ in range(q)]
    free=[(0,0,W,H)]; placed=[]
    for pid,a,b in sorted(pcs,key=lambda p:-p[1]*p[2]):
        best=None
        for fi,r in enumerate(free):
            for w,h in ((a,b),(b,a)):
                if w<=r[2] and h<=r[3]:
                    sc=min(r[2]-w,r[3]-h)
                    if best is None or sc<best[0]: best=(sc,fi,w,h)
        if not best: raise SystemExit(f"NO CABE {pid}")
        _,fi,w,h=best; x,y,rw,rh=free.pop(fi); placed.append((pid,x,y,w,h))
        if rw-w < rh-h: free += [(x+w+K,y,rw-w-K,h),(x,y+h+K,rw,rh-h-K)]
        else: free += [(x+w+K,y,rw-w-K,rh),(x,y+h+K,w,rh-h-K)]
        free=[r for r in free if r[2]>0 and r[3]>0]
    use=sum(w*h for *_,w,h in placed)/(W*H)
    return placed,use
def svg(placed, W, H, title, fname, colors):
    s=0.4; pad=30
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*s+2*pad:.0f} {H*s+2*pad:.0f}" font-family="Liberation Sans, Arial, sans-serif">',
         f'<rect x="{pad}" y="{pad}" width="{W*s}" height="{H*s}" fill="#efe8dd" stroke="#2b2622" stroke-width="2"/>',
         f'<text x="{pad}" y="20" font-size="14" font-weight="700" fill="#2b2622">{title}</text>',
         f'<text x="{pad+W*s/2}" y="{pad+H*s+20}" font-size="11" text-anchor="middle" fill="#666">{W} mm</text>',
         f'<text x="{pad-10}" y="{pad+H*s/2}" font-size="11" text-anchor="middle" fill="#666" transform="rotate(-90 {pad-10} {pad+H*s/2})">{H} mm</text>']
    for pid,x,y,w,h in placed:
        X=pad+(x+TRIM)*s; Y=pad+(y+TRIM)*s; ww=w*s; hh=h*s
        out.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{ww:.1f}" height="{hh:.1f}" fill="{colors[pid[0]]}" stroke="#2b2622" stroke-width="0.8"/>')
        big=max(w,h); sm=min(w,h); rot = hh>ww and ww<48
        cx,cy=X+ww/2,Y+hh/2; tr=f' transform="rotate(-90 {cx:.1f} {cy:.1f})"' if rot else ''
        fs=12 if min(ww,hh)>30 else 9
        out.append(f'<text x="{cx:.1f}" y="{cy-1:.1f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="#2b2622"{tr}>{pid}</text>')
        out.append(f'<text x="{cx:.1f}" y="{cy+fs-1:.1f}" font-size="{fs-2}" text-anchor="middle" fill="#444"{tr}>{big}×{sm}</text>')
    out.append('</svg>'); open(fname,'w').write('\n'.join(out))
col={"C":"#cfe3e1","M":"#f6d3bf","H":"#e6dcc8"}
pm,um=pack(MEL,2440,2150); svg(pm,2440,2150,"Melamina RH 15 mm · 2440 × 2150 mm · 1 lámina","despiece-melamina.svg",col)
# HDF: probar 2440x1830 (formato más común); si no cabe, 2440x2150
try: ph,uh=pack(HDF,2440,1830); HW,HH=2440,1830
except SystemExit: ph,uh=pack(HDF,2440,2150); HW,HH=2440,2150
svg(ph,HW,HH,f"HDF 3 mm · {HW} × {HH} mm · 1 lámina","despiece-hdf.svg",col)
canto=sum(sum(e)*q for *_,q,e in MEL)/1000
json.dump({"MEL":MEL,"HDF":HDF,"uso_mel":um,"uso_hdf":uh,"hdf_fmt":[HW,HH],"canto_m":canto,
  "n_mel":sum(i[5] for i in MEL),"n_hdf":sum(i[5] for i in HDF)},open("piezas.json","w"),ensure_ascii=False,indent=1)
print(f"melamina uso {um*100:.0f}%  hdf {HW}x{HH} uso {uh*100:.0f}%  canto {canto:.1f} m  piezas {sum(i[5] for i in MEL)} + {sum(i[5] for i in HDF)}")
