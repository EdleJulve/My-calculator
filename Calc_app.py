import tkinter as tk

#------------VENTANA-----------------
ventana = tk.Tk() #crear ventana
ventana.title('Edle Calculator') #titulo
ventana.geometry("360x360") #Window Size
ventana.configure(bg="#3B97BE") #color ventana


#-----------PANTALLA--------------------
pantalla = tk.Entry(ventana, font=("Arial bold", 30), justify="right", bg="#3B97BE", fg="#F2F2F2", relief="flat")
pantalla.grid( row=0, column=0, columnspan=11, padx=0, pady=0)

#-----------ETIQUETA LABEL------

etiqueta = tk.Label(ventana, text="ENTER:", font=('Arial', 12, "bold"), bg="#2E9DC0", fg="white")
etiqueta.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

#-------LOGICA-----------

def agregar_numero(num):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + str(num))

def calcular():
    expresion = pantalla.get()
    try:
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, tk.END)                                        
        pantalla.insert(0, 'Error')  
def agregar(valor):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + str(valor))  

def borrar_todo():
    pantalla.delete(0, tk.END)

#-------------campo de texto (pantalla)-----------
pantalla = tk.Entry(ventana, width=20, font=('Arial', 14), justify='left', bg="#289FFA", fg="#F7F720", insertbackground="#87DE6E", relief="flat")
pantalla.grid(row=0, column=0, columnspan=8, padx=1, pady=1)

#-----------BOTONES NUMBERS-----------
boton1 = tk.Button(ventana, text='1', width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(1),bd=0, relief="flat", bg="#C12A96", fg="#F7F720" )
boton1.grid(row=1, column=0)

boton2 = tk.Button(ventana, text="2", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(2),bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton2.grid(row=1, column=1)

boton3 = tk.Button(ventana, text="3", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(3), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton3.grid(row=1, column=2)

boton4 = tk.Button(ventana, text="4", width=6, height=2,font=('Arial bold', 15), command=lambda: agregar_numero(4), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton4.grid(row=2, column=0)

boton5 = tk.Button(ventana, text="5", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(5), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton5.grid(row=2, column=1)

boton6 = tk.Button(ventana, text="6", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(6), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton6.grid(row=2, column=2)

boton7 = tk.Button(ventana, text="7", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(7), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton7.grid(row=3, column=0)

boton8 = tk.Button(ventana, text="8", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(8), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton8.grid(row=3, column=1)

boton9 = tk.Button(ventana, text="9", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(9), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton9.grid(row=3, column=2)

boton0 = tk.Button(ventana, text="0", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar_numero(0),bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
boton0.grid(row=4, column=0)

# --------------BOTONES SIMBOLOS Y ERASE-------
botonpunto = tk.Button(ventana, text=".", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("."),  bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonpunto.grid(row=4, column=1)

botonigual = tk.Button(ventana, text="=", width=6, height=2, font=('Arial bold', 15), command=calcular, bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonigual.grid(row=5, column=2)

botonadd = tk.Button(ventana, text="+", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("+"), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonadd.grid(row=1, column=4)

botonrest = tk.Button(ventana, text="-", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("-"), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonrest.grid(row=2, column=4)

botondivide = tk.Button(ventana, text="/", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("/"), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botondivide.grid(row=3, column=4)

botonby = tk.Button(ventana, text="x", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("*"), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonby.grid(row=4, column=4)

botonerase = tk.Button(ventana, text="Del", width=6, height=2, font=('Arial bold', 15), command=borrar_todo, bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonerase.grid(row=4, column=2)

botonopen = tk.Button(ventana, text="(", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar("("), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonopen.grid(row=5, column=0)

botonclose = tk.Button(ventana, text=")", width=6, height=2, font=('Arial bold', 15), command=lambda: agregar(")"), bd=0, relief="flat", bg="#C12A96", fg="#F7F720")
botonclose.grid(row=5, column=1)

#-------------Mantener la ventana abierta-------------

ventana.mainloop() 
