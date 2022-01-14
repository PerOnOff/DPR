import os
import sys

def prviZadatak():
    print()
    print("Vježba 6: Zadatak 1:")
    print()

    #Služi za čitanje
    rf = open("myfile.txt", "r")
    print(rf.read())
    rf.close()

    #Gazi preko postojećeg sadržaja
    wf = open("myemptyfile.txt", "w")
    wf.write("why so serious")
    wf.close()

    rf2 = open("myemptyfile.txt","r")
    print(rf2.read())
    rf2.close()

def drugiZadatak():
    print()
    print("Vježba 6: Zadatak 2:")
    print()

    f = open("myfile.txt", "a")
    data = ("str1 ", "str2 ", "str3 ")
    data2 = [1,2,3,4,5]

    f.write("".join(data))
    f.write("{} {} {} {} {}", data2)
    f.close()

    f = open("myfile.txt", "r")
    print(f.read())


def treciZadatak():
    print()
    print("Vježba 6: Zadatak 3:")
    print()

    path = os.path.abspath("myfile.txt")
    print(path)

    print(os.path.exists(path))
    print(os.path.isdir(path))

def cetvrtiZadatak():
    print()
    print("Vježba 6: Zadatak 4:")
    print()

    print(sys.path)
    sys.path.append('/C:/Users/thepe/PycharmProjects/PeroVjezbe/directory')
    print(sys.path)
    from directory.modul import funkcija

    path = os.path.abspath("myfile.txt")
    funkcija(path)

