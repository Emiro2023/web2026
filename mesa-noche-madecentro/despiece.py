# Empaquetado guillotina (maxrects simple) para verificar 1 lámina 2150x2440
# con refilado de 10 mm por borde y sierra de 4 mm.
import itertools
W, H, TRIM, K = 2440, 2150, 10, 4
W -= 2*TRIM; H -= 2*TRIM
comoda = [("Sobre",900,400,1),("Costado",785,380,2),("Piso",840,380,1),("División",652,380,1),
  ("Repisa",256,360,1),("Travesaño",840,80,2),("Zócalo",840,118,1),("Frente cajón",590,160,4),
  ("Puerta",649,277,1),("Costado cajón",350,110,8),("Frente/fondo int.",513,110,8)]
mesa = [("Tapa",400,373,1),("Costado",492,358,2),("Piso",370,358,1),("Repisa nicho",370,358,1),
  ("Zócalo",370,70,1),("Travesaño",370,80,1),("Frente cajón",397,141,2),
  ("Costado cajón",300,110,4),("Frente/fondo int.",314,110,4)]
pieces=[]
for tag,lst in (("C",comoda),("M",mesa)):
    for n,a,b,q in lst:
        for i in range(q): pieces.append((f"{tag}:{n}",a,b))
free=[(0,0,W,H)]; placed=[]
def fits(r,w,h): return w+K<=r[2]+K and h+K<=r[3]+K and w<=r[2] and h<=r[3]
for name,a,b in sorted(pieces,key=lambda p:-p[1]*p[2]):
    best=None
    for fi,r in enumerate(free):
        for w,h in ((a,b),(b,a)):
            if w<=r[2] and h<=r[3]:
                score=min(r[2]-w,r[3]-h)
                if best is None or score<best[0]: best=(score,fi,w,h)
    if not best: print("NO CABE:",name); continue
    _,fi,w,h=best; x,y,rw,rh=free.pop(fi); placed.append((name,x,y,w,h))
    # split guillotina por el lado más corto sobrante
    if rw-w < rh-h:
        free += [(x+w+K,y,rw-w-K,h),(x,y+h+K,rw,rh-h-K)]
    else:
        free += [(x+w+K,y,rw-w-K,rh),(x,y+h+K,w,rh-h-K)]
    free=[r for r in free if r[2]>0 and r[3]>0]
used=sum(w*h for _,_,_,w,h in placed)
print(f"piezas {len(placed)}/{len(pieces)}  uso {used/(W*H)*100:.0f}% del área útil")
import json; json.dump({"W":W,"H":H,"placed":placed},open('despiece.json','w'))
