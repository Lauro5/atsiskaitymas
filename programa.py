from tkinter import *
import string
import random
import pyperclip

def sudaryti():
    mazosios=string.ascii_lowercase
    didziosios=string.ascii_uppercase
    skaiciai=string.digits
    simboliai=string.punctuation

    visi=mazosios+didziosios+skaiciai+simboliai
    ilgis=int(uzrasas3.get())

    if kintamasis.get()==1:
        ivedimas.insert(0,random.sample(mazosios+didziosios,ilgis))

    if kintamasis.get()==2:
        ivedimas.insert(0,random.sample(mazosios+didziosios+skaiciai,ilgis))

    if kintamasis.get()==3:
        ivedimas.insert(0,random.sample(visi,ilgis))

def kopijuoti():
    random_slaptazodis=ivedimas.get()
    pyperclip.copy(random_slaptazodis)

def istrinti():
    ivedimas.delete(0, END)

def uzdaryti():
    langas.destroy()

langas=Tk()
langas.title('                     Slaptažodžių generatorius')
langas.geometry("400x530")
langas.config(bg='AntiqueWhite3')
kintamasis=IntVar()
Font=('Verdana',15,'bold')

uzrasas1=Label(langas,text='Slaptažodis',font=('Helvetica',18,'bold'),bg='gray20',fg='white',anchor=CENTER)
uzrasas1.grid(pady=5)

silpnas=Radiobutton(langas,text='Silpnas',value=1,variable=kintamasis,font=('Arial',15,'bold'),selectcolor='red')
silpnas.grid(pady=5)

vidutinis=Radiobutton(langas,text='Vidutinis',value=2,variable=kintamasis,font=('Arial',15,'bold'),selectcolor='yellow')
vidutinis.grid(pady=5)

stiprus=Radiobutton(langas,text='Stiprus',value=3,variable=kintamasis,font=('Arial',15,'bold'),selectcolor='green')
stiprus.grid(pady=5)

uzrasas2=Label(langas,text='Slaptažodžio ilgis',font=('Helvetica',18,'bold'),bg='gray20',fg='white')
uzrasas2.grid(pady=5)

uzrasas3=Spinbox(langas,from_=0,to_=15,width=5,font=Font,justify='center')
uzrasas3.grid(pady=5)

mygtukas1=Button(langas,text='Sudaryti',font=Font,command=sudaryti)
mygtukas1.grid(pady=5)

ivedimas=Entry(langas,width=30,bd=2,font=Font, justify='center')
ivedimas.grid()

mygtukas2=Button(langas,text='Kopijuoti',font=Font,command=kopijuoti)
mygtukas2.grid(pady=5)

istrinimas=Button(langas,text="Ištrinti", font=Font, command=istrinti)
istrinimas.grid(pady=5)

isejimas=Button(langas, text='Išėjimas iš programos', font=Font, command=uzdaryti)
isejimas.grid(pady=20)

langas.mainloop()
