from tkinter import *
from tkinter import messagebox


def venTime():
    ventanaTime = Tk()
    ventanaTime.wm_attributes("-topmost", True)
    ventanaTime.resizable(0,0)
    ventanaTime.wm_attributes("-topmost", True)
    ventanaTime.overrideredirect(True)
    def aceptarTime():
        global time
        time=txtTime.get()
        try:
            if int(time):
                messagebox.showinfo(message="Tiempo ingresado correctamente!", title="Genial!")
                ventanaTime.destroy()
                return time
        except:
            messagebox.showinfo(message="Tiempo ingresado no valido!", title="Error!")
            ventanaTime.destroy()
            venTime()

            
    #DECLARACIONES
    lbl1 = Label(ventanaTime, text="Cada cuantos minutos quieres que te pregunte?")
    txtTime = Entry(ventanaTime ,width=5)
    txtTime.focus()
    botonAceptar = Button(ventanaTime, text="Aceptar", command=aceptarTime)

    
    #posicionamiento
    lbl1.pack()
    txtTime.pack()
    botonAceptar.pack()
    ventanaTime.mainloop()
    return time