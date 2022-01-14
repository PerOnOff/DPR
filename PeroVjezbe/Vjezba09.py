def prviZadatak():
    print()
    print("Vježba 9: Zadatak 1:")
    print()
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rSum(lista)
def rSum(x):
    if x:
        return x[0] + rSum( x[1:])
    return 0


def drugiZadatak():
    print()
    print("Vježba 9: Zadatak 2:")
    print()
    x=0
    x=input("Unesite broj 1-9")
    while x<1 or x>9:
        x = input("Unesite broj 1-9")
    rOwO(x)
def rOwO(x):
    print (x,end=' ')
    if(x==1):
        print(1,end=' ')
        return
    rOwO(x-1)
    print(x,end=' ')

