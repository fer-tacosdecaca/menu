from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

a = Tk()
a.geometry("600x600")
a.title("arrozconpollo")


c = ImageTk.PhotoImage(Image.open("d.jpg"))


b =Label(a)
b["image"]=c
b.place(relx=0.5, rely=0.3, anchor=CENTER)

e =Label(a,text="Mexico", font=("times", 40, "bold"), fg="coral")
e.place(relx= 0.5, rely=0.4, anchor= CENTER)

f =Label(a,text="Arroz con pollo", font=("times", 17, "bold"), fg="#747f8a")
f.place(relx= 0.5, rely=0.5, anchor= CENTER)

g = ["comids","bebids"]
h = ttk.Combobox(a, values = g)
h.place(relx=0.5, rely=0.65, anchor=CENTER)

i=Label(a,text="selciona, comida o bebida",font=("danfo", 15, "bold"))
i.place(relx=0.5, rely=0.6, anchor=CENTER)

l=Label(a,text="este texto sera borrado mas tarde",font=("danfo", 12, "bold"))
l.place(relx=0.5, rely=0.7, anchor=CENTER)

j = []
k = ttk.Combobox(a, values = j)
k.place(relx=0.5, rely=0.75, anchor=CENTER)

m =Label(a,text="Cantidad:")
m.place(relx=0.5, rely=0.8, anchor=CENTER)



class q():
    print("solo para no dar error")
    def __init__(self):
        print("nada")
    
    def r(s):
        print("nada")
        if s== "comids":
            t = ["arroz con pollo","ollop noc zorra"]
            u = ttk.Combobox(a, values = t)
            u.place(relx=0.5, rely=1, anchor=CENTER)
        elif s=="bebids":
            t = ["aire"]
            u = ttk.Combobox(a, values = t)
            u.place(relx=0.5, rely=1, anchor=CENTER)
        else:
            print("come algo")

class v(q):
    print("text")
    def __int__(self,s):
        self.w = s
    def x(self):
        w = h.get()
        q.r(w)

z = v(h.get())
z.x()







n = Button(a,text="Revisar complementos",bg="Blue", fg="white",relief = FLAT,command=z.x)
n.place(relx=0.5,rely=0.85,anchor=CENTER)

p = Button(a,text="Cantidad",bg="Blue", fg="white",relief = FLAT)
p.place(relx=0.5,rely=0.9,anchor=CENTER)






        




























a.mainloop()


