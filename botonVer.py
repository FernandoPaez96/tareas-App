from tkinter import *
from tkinter import messagebox, ttk
from sqlite3 import Error
import sqlite3, time, threading, sys
from addTarea import agregar

def cleanGrafico():
    try:

        db = sqlite3.connect('dbTareas.db')

    except Error:

        print(Error)
    
    cursorObj = db.cursor()
    cursorObj.execute('DROP TABLE tareas')
    cursorObj.execute("CREATE TABLE tareas(id integer PRIMARY KEY, tarea text, hora text )")
    cursorObj.fetchall()



def verGrafico():
    try:

        db = sqlite3.connect('dbTareas.db')

    except Error:

        print(Error)

    cursorObj = db.cursor()
    cursorObj.execute('SELECT * FROM tareas')
    tareas = cursorObj.fetchall()
    cursorObj.execute('SELECT hora FROM tareas')
    horas = cursorObj.fetchall()

    ventanaVer=Tk()
    ventanaVer.resizable(0,0)

    tabla = ttk.Treeview(ventanaVer, height=10, columns=2)

    tabla.pack(side="left")
    

    tabla.heading("#0", text="Tarea")
    tabla.heading("#1", text="Tiempo")
    
    
    
    for tarea in tareas:
        tabla.insert('', 0, text=tarea[1], value = tarea[2])





    verscrlbar = ttk.Scrollbar(ventanaVer, orient="vertical", command=tabla.yview)
    verscrlbar.pack(side='right', fill='y')
    tabla.configure(yscrollcommand=verscrlbar.set)
    btnPrueba = Button(ventanaVer,text="Hola")

    return