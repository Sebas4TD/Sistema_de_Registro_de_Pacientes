#IMPORTAMOS TKINTER
import tkinter as tk
from tkinter import messagebox

#IMPORTAMOS LA CLASE ATENCION
from modelos import Atencion

#FUNCION PARA REGISTRAR ATENCION
def registrar_atencion(ventana, sistema):

    #CREAMOS VENTANA NUEVA
    ventana_atencion = tk.Toplevel(ventana)
    ventana_atencion.title("Registrar atención")
    ventana_atencion.geometry("450x400")

    #TITULO
    tk.Label(
        ventana_atencion,
        text="Registro de atención",
        font=("Arial", 16)
    ).pack(pady=15)

    #ID DE LA CITA arreglarlo
    tk.Label(ventana_atencion, text="ID de cita:").pack()
    entrada_cita = tk.Entry(ventana_atencion)
    entrada_cita.pack(pady=5)

    #DIAGNOSTICO
    tk.Label(ventana_atencion, text="Diagnóstico:").pack()
    entrada_diagnostico = tk.Entry(ventana_atencion)
    entrada_diagnostico.pack(pady=5)

    #OBSERVACIONES
    tk.Label(ventana_atencion, text="Observaciones:").pack()
    entrada_observaciones = tk.Entry(ventana_atencion)
    entrada_observaciones.pack(pady=5)

    #FUNCION PARA GUARDAR LA ATENCION
    def guardar_atencion():
        try:
            cita_id = entrada_cita.get()
            diagnostico = entrada_diagnostico.get()
            observaciones = entrada_observaciones.get()

            #VERIFICAMOS QUE EXISTA LA CITA
            if sistema.buscar_cita(cita_id) is None:
                raise ValueError("No existe una cita con ese ID")

            #GENERAMOS AUTOMATICAMENTE EL ID DE ATENCION
            id_atencion = str(len(sistema._atenciones) + 1)

            #CREAMOS LA ATENCION
            atencion = Atencion(
                id_atencion,
                cita_id,
                diagnostico,
                observaciones
            )

            #REGISTRAMOS LA ATENCION
            sistema.registrar_atencion(atencion)

            messagebox.showinfo(
                "Registro exitoso",
                f"Atención registrada correctamente.\n"
                f"ID de atención: {id_atencion}"
            )
            ventana_atencion.destroy()

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    #BOTON GUARDAR
    tk.Button(
        ventana_atencion,
        text="Guardar atención",
        command=guardar_atencion
    ).pack(pady=15)