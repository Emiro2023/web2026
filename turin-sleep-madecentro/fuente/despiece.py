"""Piezas y despiece: Cómoda Turín 80×86×40 (T) + Nochero Sleep 50×52×40 (N). Medidas en mm."""
import json, sys
K, TRIM = 4, 10
MEL = [
 ("T1","Cómoda","Tapa",800,400,1,[800,800,400,400]),
 ("T2","Cómoda","Costado",820,400,2,[820,400]),
 ("T3","Cómoda","Piso",770,400,1,[770]),
 ("T4","Cómoda","Entrepaño fijo (sobre las puertas)",770,370,1,[770]),
 ("T5","Cómoda","Travesaño superior acostado",770,80,2,[]),
 ("T6","Cómoda","Repisa interior regulable",770,360,1,[770]),
 ("T7","Cómoda","Frente de cajón (embutido)",766,155,2,[766,766,155,155]),
 ("T8","Cómoda","Puerta (embutida)",416,382,2,[416,416,382,382]),
 ("T9","Cómoda","Costado de cajón",350,110,4,[350]),
 ("T10","Cómoda","Frente/fondo interno de cajón",714,110,4,[714]),
 ("N1","Nochero","Tapa",500,400,1,[500,500,400,400]),
 ("N2","Nochero","Costado",480,400,2,[480,400]),
 ("N3","Nochero","Piso",470,400,1,[470]),
 ("N4","Nochero","Repisa (base del nicho)",470,400,1,[470]),
 ("N5","Nochero","Puerta (embutida)",466,256,1,[466,466,256,256]),
]
HDF = [
 ("TH1","Cómoda","Fondo",820,800,1,[]),
 ("TH2","Cómoda","Base de cajón",744,350,2,[]),
 ("NH1","Nochero","Fondo",500,480,1,[]),
]
def pack(items, W, H):
    W -= 2*TRIM; H -= 2*TRIM
    pcs=[(pid,a,b) for pid,_,_,a,b,q,_ in items for _ in range(q)]
    free=[(0,0,W,H)]; placed=[]
    for pid,a,b in sorted(pcs,key=lambda p:(-p[1]*p[2])):
        best=None
        for fi,r in enumerate(free):
            for w,h in ((a,b),(b,a)):
                if w<=r[2] and h<=r[3]:
                    sc=min(r[2]-w,r[3]-h)
                    if best is None or sc<best[0]: best=(sc,fi,w,h)
        if not best: return None, pid
        _,fi,w,h=best; x,y,rw,rh=free.pop(fi); placed.append((pid,x,y,w,h))
        if rw-w < rh-h: free += [(x+w+K,y,rw-w-K,h),(x,y+h+K,rw,rh-h-K)]
        else: free += [(x+w+K,y,rw-w-K,rh),(x,y+h+K,w,rh-h-K)]
        free=[r for r in free if r[2]>0 and r[3]>0]
    return placed, sum(w*h for *_,w,h in placed)/(W*H)
if False:
    for fmt in [(2440,2150),(2440,1830)]:
        for name,sel in [("ambos",MEL),("Cómoda",[p for p in MEL if p[1]=="Cómoda"]),("Nochero",[p for p in MEL if p[1]=="Nochero"])]:
            r,u=pack(sel,*fmt); print(fmt,name,"OK %.0f%%"%(u*100) if r else f"NO cabe ({u})")
    for fmt in [(2440,1830),(2440,1220)]:
        r,u=pack(HDF,*fmt); print("HDF",fmt,"OK %.0f%%"%(u*100) if r else f"NO ({u})")
    print("canto m:", sum(sum(e)*q for *_,q,e in MEL)/1000)

def svg(placed, W, H, title, fname, colors):
    s=0.4; pad=30
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W*s+2*pad:.0f} {H*s+2*pad:.0f}" font-family="Liberation Sans, Arial, sans-serif">',
         f'<rect x="{pad}" y="{pad}" width="{W*s}" height="{H*s}" fill="#efe8dd" stroke="#2b2622" stroke-width="2"/>',
         f'<text x="{pad}" y="20" font-size="14" font-weight="700" fill="#2b2622">{title}</text>',
         f'<text x="{pad+W*s/2}" y="{pad+H*s+20}" font-size="11" text-anchor="middle" fill="#666">{W} mm</text>',
         f'<text x="{pad-10}" y="{pad+H*s/2}" font-size="11" text-anchor="middle" fill="#666" transform="rotate(-90 {pad-10} {pad+H*s/2})">{H} mm</text>']
    for pid,x,y,w,h in placed:
        X=pad+(x+TRIM)*s; Y=pad+(y+TRIM)*s; ww=w*s; hh=h*s
        out.append(f'<rect x="{X:.1f}" y="{Y:.1f}" width="{ww:.1f}" height="{hh:.1f}" fill="{colors.get(pid[:2],colors[pid[0]])}" stroke="#2b2622" stroke-width="0.8"/>')
        big=max(w,h); sm=min(w,h); rot = hh>ww and ww<60
        cx,cy=X+ww/2,Y+hh/2; tr=f' transform="rotate(-90 {cx:.1f} {cy:.1f})"' if rot else ''
        fs=12 if min(ww,hh)>30 else 9
        lab=pid.replace('b','')
        out.append(f'<text x="{cx:.1f}" y="{cy-1:.1f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="#2b2622"{tr}>{lab}</text>')
        out.append(f'<text x="{cx:.1f}" y="{cy+fs-1:.1f}" font-size="{fs-2}" text-anchor="middle" fill="#444"{tr}>{big}×{sm}</text>')
    out.append('</svg>'); open(fname,'w').write('\n'.join(out))

def generar():
    col={"T":"#cfe3e1","N":"#f6d3bf","TH":"#e6dcc8","NH":"#f0e1d0"}
    T=[p for p in MEL if p[1]=="Cómoda"]; N=[p for p in MEL if p[1]=="Nochero"]
    N2=[(a,b,c,d,e,q*2,f) for a,b,c,d,e,q,f in N]
    pa,ua=pack(T,2440,1830); svg(pa,2440,1830,"Lámina A · melamina RH 15 mm 2440 × 1830 · cómoda Turín","despiece-A.svg",col)
    pb,ub=pack(N2,2440,1830); svg(pb,2440,1830,"Lámina B · melamina RH 15 mm 2440 × 1830 · 2 nocheros Sleep","despiece-B.svg",col)
    H=[p for p in HDF]+[("NH1b","Nochero","Fondo (2.º nochero)",505,500,1,[])]
    ph,uh=pack(H,2440,1830); svg(ph,2440,1830,"HDF 3 mm 2440 × 1830 · cómoda + 2 nocheros","despiece-HDF.svg",col)
    canto_T=sum(sum(e)*q for _,m,_,_,_,q,e in MEL if m=="Cómoda")/1000
    canto_N=sum(sum(e)*q for _,m,_,_,_,q,e in MEL if m=="Nochero")/1000
    json.dump({"MEL":MEL,"HDF":HDF,"uA":ua,"uB":ub,"uH":uh,"canto_T":canto_T,"canto_N":canto_N,
      "nT":sum(p[5] for p in T),"nN":sum(p[5] for p in N)},open("piezas.json","w"),ensure_ascii=False,indent=1)
    print(f"A {ua*100:.0f}%  B {ub*100:.0f}%  HDF {uh*100:.0f}%  canto T {canto_T:.1f} N {canto_N:.1f}")

def generar():
    col={"T":"#cfe3e1","N":"#f6d3bf","TH":"#e6dcc8","NH":"#f0e1d0"}
    pm,um=pack(MEL,2440,2150); svg(pm,2440,2150,"Melamina RH 15 mm · 2440 × 2150 · 1 lámina · cómoda Turín + nochero Sleep","despiece-melamina.svg",col)
    ph,uh=pack(HDF,2440,1830); svg(ph,2440,1830,"HDF 3 mm · 2440 × 1830 · 1 lámina","despiece-hdf.svg",col)
    cT=sum(sum(e)*q for _,m,_,_,_,q,e in MEL if m=="Cómoda")/1000
    cN=sum(sum(e)*q for _,m,_,_,_,q,e in MEL if m=="Nochero")/1000
    json.dump({"MEL":MEL,"HDF":HDF,"uM":um,"uH":uh,"canto_T":cT,"canto_N":cN,
      "nT":sum(p[5] for p in MEL if p[1]=="Cómoda"),"nN":sum(p[5] for p in MEL if p[1]=="Nochero")},
      open("piezas.json","w"),ensure_ascii=False,indent=1)
    print(f"melamina {um*100:.0f}%  hdf {uh*100:.0f}%  canto T {cT:.1f} N {cN:.1f}")
if __name__=="__main__": generar()
