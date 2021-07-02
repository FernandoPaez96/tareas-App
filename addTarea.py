from sqlite3 import Error
import sqlite3
import time

def agregar(texto):
    try:

        db = sqlite3.connect('dbTareas.db')

    except Error:

        print(Error)

    cursorObj = db.cursor()
    tarea= texto
    hora = time.strftime("%H:%M:%S")

    cursorObj.execute("insert into tareas(tarea, hora) values (?, ?);", (tarea, str(hora)))

    #INSERT INTO tareas(tarea, hora) VALUES ("TAREA DEPRUEBA", datetime('localtime'))

    db.commit()

def mismaAgregar():
    try:

        db = sqlite3.connect('dbTareas.db')

    except Error:

        print(Error)

    cursorObj = db.cursor()
    cursorObj.execute('select tarea from tareas where id=(select MAX(id) from tareas)')
    tareaa = cursorObj.fetchall()
    comparacion=["'","(",")","[","]"]
    tarea=str(tareaa)
    hora = time.strftime("%H:%M:%S")
    final=""
    for x in tarea:
        if x in comparacion:
            continue
        else:
            final=final+x

    cursorObj.execute("insert into tareas(tarea, hora) values (?, ?);", (final[:-1], str(hora)))

    #INSERT INTO tareas(tarea, hora) VALUES ("TAREA DEPRUEBA", datetime('localtime'))

    db.commit()