"""Da se kreira funkcija so ime najdolgo ime koja ke prima lista kako parametar, da go njade najdolgoto 
ime od lista, da go ispecati i da kaze od kolku parametri e sostaveno. Korisnikot da gi vnesuva iminjata"""

def najdolgo_ime(i):
    m=max(i, key=len)
    print("Najdolgoto ime e  : {}, i ima {} karakteri".format(m,len(m)))
li=[]

while True:
    a=input("vnesi ime ili k za kraj ")
    if a=="k":
        break    
    else:
        li.append(a)

print(li)
najdolgo_ime(li)