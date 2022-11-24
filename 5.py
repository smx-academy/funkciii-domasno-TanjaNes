"""Da se kreira funkcija koja ke prima eden parametar lista i da moze da presmeta prosek na listata"""
def lista(y):
    x=sum(y)
    z=len(y)
    print(x,z)
    e=x/z
    print('prosekot od elementite vo listata e ', e)  
lst=[1,6,9,8,89,78,8,65]
lista(lst)
