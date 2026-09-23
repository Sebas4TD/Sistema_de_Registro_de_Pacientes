#IMPORTAMOS TKINTER PARA LA INTERFAZ
import tkinter as tk
from tkinter import messagebox

#FUNCION PARA REGISTRAR PACIENTE
def registrar_paciente(ventana, sistema):
    #CREAMOS UNA VENTANA
    ventana_paciente = tk.Toplevel(ventana)
    ventana_paciente.title("Registrar paciente")
    ventana_paciente.geometry("400x350")

    #TITULO
    tk.Label(
        ventana_paciente,
        text="Registro de paciente",
        font=("Arial", 16)
    ).pack(pady=15)

    #DNI
    tk.Label(ventana_paciente, text="DNI:").pack()
    entrada_dni = tk.Entry(ventana_paciente)
    entrada_dni.pack(pady=5)

    #NOMBRE
    tk.Label(ventana_paciente, text="Nombre:").pack()
    entrada_nombre = tk.Entry(ventana_paciente)
    entrada_nombre.pack(pady=5)

    #EDAD
    tk.Label(ventana_paciente, text="Edad:").pack()
    entrada_edad = tk.Entry(ventana_paciente)
    entrada_edad.pack(pady=5)

    #TELEFONO
    tk.Label(ventana_paciente, text="Teléfono:").pack()
    entrada_telefono = tk.Entry(ventana_paciente)
    entrada_telefono.pack(pady=5)

    #FUNCION PARA GUARDAR LOS DATOS
    def guardar_paciente():
        try:
            dni = entrada_dni.get()
            nombre = entrada_nombre.get()
            edad = entrada_edad.get()
            telefono = entrada_telefono.get()

            #IMPORTAMOS PACIENTE
            from modelos import Paciente

            paciente = Paciente(
                dni,
                nombre,
                edad,
                telefono
            )

            #REGISTRAMOS PACIENTE
            sistema.registrar_paciente(paciente)

            messagebox.showinfo(
                "Registro exitoso",
                "Paciente registrado correctamente."
            )

            ventana_paciente.destroy()

        #FUNCION POR SI EL USUARIO SE EQUIVOCA AL TIPEAR
        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    #BOTON PARA GUARDAR
    tk.Button(
        ventana_paciente,
        text="Guardar paciente",
        command=guardar_paciente
    ).pack(pady=15)

def buscar_paciente(ventana, sistema):

    #CREAMOS UNA VENTANA
    ventana_busqueda = tk.Toplevel(ventana)
    ventana_busqueda.title("Buscar paciente")
    ventana_busqueda.geometry("400x300")

    #TITULO
    tk.Label(
        ventana_busqueda,
        text="Buscar paciente",
        font=("Arial", 16)
    ).pack(pady=5)

    #DNI
    tk.Label(ventana_busqueda, text="DNI:").pack()
    entrada_dni = tk.Entry(ventana_busqueda)
    entrada_dni.pack(pady=5)

    #AREA PARA MOSTRAR RESULTADO
    resultado = tk.Label(
        ventana_busqueda,
        text="",
        font=("Arial", 11)
    )
    resultado.pack(pady=15)

    #FUNCION PARA REALIZAR LA BUSQUEDA
    def realizar_busqueda():

        dni = entrada_dni.get()
        paciente = sistema.buscar_paciente(dni)

        if paciente:
            resultado.config(
                text="Paciente encontrado:\n" +
                paciente.mostrar_datos()
            )
        else:
            resultado.config(
                text="No se encontró ningún paciente."
            )

    #BOTON BUSCAR
    tk.Button(
        ventana_busqueda,
        text="Buscar",
        comman=realizar_busqueda
    ).pack(pady=10)