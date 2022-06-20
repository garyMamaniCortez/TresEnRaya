import random
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def bloquear():
    for i in range(0,9):
        listaBotones[i].config(state="disable")

def cambiar(num):
    global nombreJugador,valorCasilla,ficha
    if valorCasilla[num]=="N":
        listaBotones[num].config(text=ficha)
        valorCasilla[num]=ficha
        if ficha=="X":
          listaBotones[num].config(bg="white")
          ganador()
          ficha="O"
          turnoJugador.set("Turno: Computadora")
        else: 
          listaBotones[num].config(bg="lightblue")
          ganador()
          ficha="X"
          turnoJugador.set("Turno: " + nombreJugador)
    listaBotones[num].config(state="disable")

def mensaje():
  if ficha=="X":
    bloquear()
    messagebox.showinfo(f'GANADOR',f'{nombreJugador} gano el juego')
  else: 
    bloquear()
    messagebox.showinfo("GANADOR","Computadora gano el juego")

def ganador():
  # horizontal
  if (valorCasilla[0]==ficha and valorCasilla[1]==ficha and valorCasilla[2]==ficha)or(valorCasilla[3]==ficha and valorCasilla[4]==ficha and valorCasilla[5]==ficha)or(valorCasilla[6]==ficha and valorCasilla[7]==ficha and valorCasilla[8]==ficha):
    mensaje()
  # Diagonal
  if (valorCasilla[0]==ficha and valorCasilla[4]==ficha and valorCasilla[8]==ficha)or(valorCasilla[2]==ficha and valorCasilla[4]==ficha and valorCasilla[6]==ficha):
    mensaje()
  # Vertical
  if (valorCasilla[0]==ficha and valorCasilla[3]==ficha and valorCasilla[6]==ficha)or(valorCasilla[1]==ficha and valorCasilla[4]==ficha and valorCasilla[7]==ficha)or(valorCasilla[2]==ficha and valorCasilla[5]==ficha and valorCasilla[8]==ficha):
    mensaje()

def iniciarJuego():
    for i in range(0,9):
        listaBotones[i].config(state="normal")
        listaBotones[i].config(bg="lightgrey")
        listaBotones[i].config(text="")
        valorCasilla[i]="N"
    global nombreJugador
    try:
      nombreJugador=simpledialog.askstring("Jugador","Nombre jugador:")
      nombreJugador=("").join(nombreJugador)
      turnoJugador.set("Turno: " + nombreJugador)
    except:
      bloquear()

ventana=Tk()
ventana.title("Tres en Raya")
ventana.geometry("400x500")
nombreJugador=("")
ficha="X"
listaBotones=[]
valorCasilla=[]
turnoJugador=StringVar()
for i in range(0,9):
    valorCasilla.append("N")

boton0=Button(ventana,width=9,height=3,command=lambda: cambiar(0))
listaBotones.append(boton0)
boton0.place(x=50,y=50)
boton1=Button(ventana,width=9,height=3,command=lambda: cambiar(1))
listaBotones.append(boton1)
boton1.place(x=150,y=50)
boton2=Button(ventana,width=9,height=3,command=lambda: cambiar(2))
listaBotones.append(boton2)
boton2.place(x=250,y=50)
boton3=Button(ventana,width=9,height=3,command=lambda: cambiar(3))
listaBotones.append(boton3)
boton3.place(x=50,y=150)
boton4=Button(ventana,width=9,height=3,command=lambda: cambiar(4))
listaBotones.append(boton4)
boton4.place(x=150,y=150)
boton5=Button(ventana,width=9,height=3,command=lambda: cambiar(5))
listaBotones.append(boton5)
boton5.place(x=250,y=150)
boton6=Button(ventana,width=9,height=3,command=lambda: cambiar(6))
listaBotones.append(boton6)
boton6.place(x=50,y=250)
boton7=Button(ventana,width=9,height=3,command=lambda: cambiar(7))
listaBotones.append(boton7)
boton7.place(x=150,y=250)
boton8=Button(ventana,width=9,height=3,command=lambda: cambiar(8))
listaBotones.append(boton8)
boton8.place(x=250,y=250)
turnoE=Label(ventana,textvariable=turnoJugador).place(x=120,y=20)
iniciar=Button(ventana,bg="dark blue",fg="white",text="Iniciar Juego",width=15,height=3,command=iniciarJuego).place(x=130,y=350)
bloquear()
ventana.mainloop()