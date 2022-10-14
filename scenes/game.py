import turtle
from tkinter import *


def bot(): 
  pass

def Game():
  wn = turtle.Screen()
  canvas = wn.getcanvas()
  label = Label(canvas.master, text="Tu nombre", bg="#fff")
  label.pack()
  label.place(x=300, y=300)
  namePlayer = Entry(canvas.master)
  namePlayer.pack()
  namePlayer.place(x=370, y=300)

  def aceptar():
    wn.clear()
    return namePlayer

  button = Button(canvas.master, text="Aceptar", bg="#3554b7", width=15, height=3, bd=0, fg="#ffffff", command=aceptar)
  button.pack()
  button.place(x=330, y=400)
  wn.mainloop()



 




