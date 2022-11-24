
"""Da se kreira funkcija plostina i funkcija perimetar koi ke primaat dva paremtri, da presmetuvaat 
plostinata i perimetarot na pravoagolnik. Korisnikot da gi vnesuva broevite i korisnikot da izbere 
koja presmetka da se izvrsi. DA NE SE IZVRSUVAAT DVETE"""

def plostina(a,b):
    print('plostinata e ',a*b)
def obikolka(a,b):
    o=2*(a+b)
    print('obikolkata e ',o)
x=int(input('vnesi str1 '))
y=int(input('vnesi str2 '))
k=input('plostina ili obikolka? p/o ')
if k=="p":
    plostina(x,y)
elif k=='o':
    obikolka(x,y)
     