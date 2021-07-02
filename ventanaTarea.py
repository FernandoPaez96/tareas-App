from tkinter import *
from tkinter import messagebox
from sqlite3 import Error
import sqlite3, time, threading, sys
from addTarea import agregar, mismaAgregar

def ventanaT():
    
    ventanaAdd = Tk()
    ventanaAdd.wm_attributes("-topmost", True)
    ventanaAdd.resizable(0,0)
    def aceptarTarea():
        texto=txtTarea.get()
        agregar(texto)
        messagebox.showinfo(message="Tarea ingresada", title="Genial!")
        ventanaAdd.destroy()
        return
    def mismaTarea():
        mismaAgregar()
        messagebox.showinfo(message="Tarea ingresada", title="Genial!")
        ventanaAdd.destroy()
        return
    #DECLARACIONES
    lbl1 = Label(ventanaAdd, text="Que tarea has estado realizando?")
    txtTarea = Entry(ventanaAdd ,width=100)
    txtTarea.focus()
    botonAceptar = Button(ventanaAdd, text="Aceptar", command=aceptarTarea)
    botonMisma = Button(ventanaAdd, text="Misma Tarea", command=mismaTarea)

    
    #posicionamiento
    lbl1.pack()
    txtTarea.pack()
    botonAceptar.pack()
    botonMisma.pack()
    ventanaAdd.mainloop()
    return 