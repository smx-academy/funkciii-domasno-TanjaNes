
    











"""a se napravi funkcija koja kako parametar ke prima nekoj string i da proveri dali toj string e 
palindrom t.e. dali toj string se cita od dvete strani
Primer ana, kalabalak"""

def palindrom(x):
    l=[]
    m=[]
    for i in x:
        l.append(i)
        m.insert(0,i)
    print(l)
    print(m)
    if m==l:
        print("zborot e palindrom")
    else:
        print("zborot ne e palindrom")
a=input('vnesi zbor :')
palindrom(a)

"""l=[]
for i in x:
    l.append(i)
print(l.reverse)"""


