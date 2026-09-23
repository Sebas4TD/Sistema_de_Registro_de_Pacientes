#IMPORTAMOS TKINTER
import tkinter as tk
from tkinter import messagebox

#IMPORTAMOS LA CLASE CITA
from modelos import Cita

#FUNCION PARA REGISTRAR CITA
def registrar_cita(ventana, sistema):

    #CREAMOS UNA VENTANA
    ventana_cita = tk.Toplevel(ventana)
    ventana_cita.title("Registrar cita")
    ventana_cita.geometry("400x400")

    #TITULO
    tk.Label(
        ventana_cita,
        text="Registro de cita",
        font=("Arial", 16)
    ).pack(pady=15)

    #DNI DEL PACIENTE
    tk.Label(ventana_cita, text="DNI del paciente:" ).pack()
    entrada_paciente = tk.Entry(ventana_cita)
    entrada_paciente.pack(pady=5)

    #ID DE LA CITA
    tk.Label(ventana_cita, text="ID de cita:").pack()
    entrada_id = tk.Entry(ventana_cita)
    entrada_id.pack(pady=5)

    #FECHA
    tk.Label(ventana_cita, text="Fecha:").pack()
    entrada_fecha =tk.Entry(ventana_cita)
    entrada_fecha.pack(pady=5)

    #HORA
    tk.Label(ventana_cita, text="Hora:").pack()
    entrada_hora = tk.Entry(ventana_cita)
    entrada_hora.pack(pady=5)

    #MOTIVO
    tk.Label(ventana_cita, text="Motivo:").pack()
    entrada_motivo = tk.Entry(ventana_cita)
    entrada_motivo.pack(pady=5)

    #FUNCIONM PARA GUARDAR LA CITA
    def guardar_cita():
        try:
            id_cita = entrada_id.get()
            paciente_id = entrada_paciente.get()
            fecha = entrada_fecha.get()
            hora = entrada_hora.get()
            motivo = entrada_motivo.get()

            #CREAMOS LA CITA
            cita = Cita(
                id_cita,
                paciente_id,
                fecha,
                hora,
                motivo
            )

            #REGISTRAMOS LA CITA
            sistema.registrar_cita(cita)

            messagebox.showinfo(
                "Registro exitoso",
                "Cita registrada correctamente."
            )
            ventana_cita.destroy

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    #BOTON PARA GUARDAR
    tk.Button(
        ventana_cita,
        text="Guardar cita",
        command=guardar_cita
    ).pack(pady=15)

#FUNCION PARA CONSULTAR CITAS
def consultar_citas(ventana, sistema):

    #CREAMOS LA VENTANA
    ventana_citas = tk.Toplevel(ventana)
    ventana_citas.title("Consultar citas")
    ventana_citas.geometry("500x350")

    #TITULO
    tk.Label(
        ventana_citas,
        text="Citas registradas",
        font=("Arial", 16)
    ).pack(pady=15)

    #OBTENEMOS LA CITA DEL SISTEMA
    citas = sistema.consultar_cita()

    #MOSTRAMOS CADA CITA
    if citas:
        for cita in citas:
            tk.Label(
                ventana_citas,
                text=cita.mostrar_datos()
            ).pack(pady=5)
    else:
        tk.Label(
            ventana_citas,
            text="No hay citas registradas."
        ).pack(pady=20)