"""Da se kreira funkcija so ime najgolem_broj koja ke prima 3 parametri, da se najde najgolemiot 
broj i da se ispecati. Broevite da gi vnese korisnikot"""

def najgolem_broj(a,b,c):
    if a>b:
        if a>c:
            print('najgolemiot broj e ', a)
        else:
            print('najgolemiot broj e ', c)
    else:
        if b>c:
            print('najgolemiot broj e ', b)
        else:
            print('najgolemiot broj e ', c)
x=int(input('vnesi br1 '))
y=int(input('vnesi br2 '))
z=int(input('vnesi br3 '))
najgolem_broj(x,y,z)
