"""Da se napravi funkcija koja ke presmetuva prosek na ucenik, otcenite da gi prima kako parametar vo 
lista. Da ima druga funkcija koja kako parametri ke gi prima prosekot i imeto na ucenikot, ke 
presmetuva uspeh na ucenik spored prosekot i da ispecati so kakov uspeh e toj ucenik"""


def prosek(lista_oceni):
        avg=sum(lista_oceni)/len(lista_oceni)
        return avg
def uspeh(prosek, ime):
    if prosek<=1.5:
        print('Ucenikot  {} e so nedovolen uspeh'.format(ime))
    elif prosek>1.5 and prosek<=2.5:
        print('Ucenikot  {} e so dovolen uspeh'.format(ime))
    elif prosek>2.5 and prosek<=3.5:
        print('Ucenikot  {} e so dobar uspeh'.format(ime))
    elif prosek>3.5 and prosek<=4.5:
        print('Ucenikot  {} e so mnogu dobar uspeh'.format(ime))
    elif prosek>4.5 and prosek<=5.0:
        print('Ucenikot  {} e so odlicen uspeh'.format(ime))

ime_ucenik=input('vnesi ime i prezime na ucenik: ')
oceni=[]

while True:
    k=input('vnesi ocenka (od 1 do 5) ili k za kraj: ')
    if k=='k':
        break
    else:
        oceni.append(int(k))
print(prosek(oceni))
avg=prosek(oceni)
uspeh(avg, ime_ucenik)

