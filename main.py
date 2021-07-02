from tkinter import *
import tkinter as tk
from tkinter import messagebox,Tk, ttk  
from sqlite3 import Error
import sqlite3, time, threading, sys, os
from addTarea import agregar
from ventanaTarea import ventanaT
from botonVer import verGrafico, cleanGrafico
from timeVen import venTime
from connectDb import conectarDb


#Timer para preguntarte la tarea
def ejecucion_horaria(segundos):
    segundos
    n_ventana = True
    while n_ventana == True:
        ventanaT()
        time.sleep(segundos)

    else:
        messagebox.showinfo(message="Adios!", title="Adios")

class MyWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        root.geometry("180x75")
        root.resizable(0,0)
        root.iconbitmap("media/tuerca.png")
        root.title("")
        root.wm_attributes("-topmost", True)
        self.imgAdd = PhotoImage(file="media/add-button.png")
        btnAdd = tk.Button(self,image=self.imgAdd, command=ventanaT)
        btnAdd.pack()
        btnVer = tk.Button(self,text="Ver", command=verGrafico)
        btnClean = tk.Button(self,text="Limpiar", command=cleanGrafico)
        btnVer.pack(side="left")
        btnClean.pack(side="right")

    
        

if __name__ == "__main__":
    conectarDb()
    segundos = venTime()
    print(segundos)
    segundos=int(segundos)*60
    root = tk.Tk()
    MyWindow(root).pack()


    hilo = threading.Thread(target=ejecucion_horaria, args=(segundos,))
    hilo.start()

    root.mainloop()
    os._exit(1)

    
    



