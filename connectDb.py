from sqlite3 import Error
import sqlite3, time, threading, sys, os
def conectarDb(): 
    try:

        db = sqlite3.connect('dbTareas.db')
    except Error:

        print(Error)


    cursorObj = db.cursor()

    try:
        cursorObj.execute("CREATE TABLE tareas(id integer PRIMARY KEY, tarea text, hora text )")
    except:
        print("conectado")