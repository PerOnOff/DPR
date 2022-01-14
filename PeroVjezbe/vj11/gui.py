from tkinter import *

root = Tk()
root.geometry("600x600")
root.title(" Q&A ")


def Take_input():
    br1 = inputtxt1.get("1.0", END)
    br2 = inputtxt2.get("1.0", END)
    br3 = inputtxt3.get("1.0", END)

    br1 = str(br1)
    br2 = str(br2)
    br3 = str(br3)


    br1 = br1[0:len(br1)-1]
    br2 = br2[0:len(br2)-1]
    br3 = br3[0:len(br3)-1]
    br1 = int(br1)
    br2 = int(br2)
    br3 = int(br3)
    lista = [br1, br2, br3]
    lista.sort()
    l1["text"] = "Najmanji broj je " + str(lista[0])
    l2["text"] = "Najveci broj je " + str(lista[1])
    l3["text"] = "Srednja vrijednost je " + str(sum(lista) / len(lista))



l1 = Label(text="Unesi broj")
inputtxt1 = Text(root, height=3,
                width=25,
                bg="light yellow")
l2 = Label(text="Unesi broj")
inputtxt2 = Text(root, height=3,
                width=25,
                bg="light yellow")
l3 = Label(text="Unesi broj")
inputtxt3 = Text(root, height=3,
                width=25,
                bg="light yellow")


Display = Button(root, height=2,
                 width=20,
                 text="Show",
                 command=lambda: Take_input())

l1.pack()
inputtxt1.pack()
l2.pack()
inputtxt2.pack()
l3.pack()
inputtxt3.pack()
Display.pack()



mainloop()