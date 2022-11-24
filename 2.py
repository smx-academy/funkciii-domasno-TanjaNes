"""Da se kreira funkcija so ime zbir koja ke prima dva broevi kako parametar, da se presmeta 
zbirot i da se ispecati dali zbirot e paren ili ne paren. Broevite da gi vnese korisnikot."""
def zbir(a,b):
    if(a+b)%2==0:
        print('zbirot na broevite e paren')
    else:
        print('zbirot na broevite e neparen')
x=int(input('vnesi br1 '))
y=int(input('vnesi br2 '))
zbir(x,y)