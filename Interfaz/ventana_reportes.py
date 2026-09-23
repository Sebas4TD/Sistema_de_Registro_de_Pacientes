#IMPORTAMOS TKINTER
import tkinter as tk
from tkinter import messagebox

#FUNCION PARA GENERAR REPORTE
def generar_reporte(ventana, sistema):

    ventana_reporte = tk.Toplevel(ventana)
    ventana_reporte.title("Generar reporte")
    ventana_reporte.geometry("450x350")

    #TITULO
    tk.Label(
        ventana_reporte,
        text="Generar reporte",
        font=("Arial", 16)
    ).pack(pady=15)

    #ID DEL REPORTE
    tk.Label(ventana_reporte, text="ID del reporte:").pack()
    entrada_id = tk.Entry(ventana_reporte)
    entrada_id.pack(pady=5)

    #FECHA
    tk.Label(ventana_reporte, text="Fecha:").pack()
    entrada_fecha = tk.Entry(ventana_reporte)
    entrada_fecha.pack(pady=5)

    #TIPO DE REPORTE
    tk.Label(ventana_reporte, text="Tipo de reporte:").pack()
    tipo_reporte = tk.StringVar()
    tipo_reporte.set("atencion")

    tk.OptionMenu(
        ventana_reporte,
        tipo_reporte,
        "atencion",
        "citas"
    ).pack(pady=5)

    #FUNCION PARA GENERAR EL REPORTE
    def crear_reporte():
        try:
            id_reporte = entrada_id.get()
            fecha = entrada_fecha.get()
            tipo = tipo_reporte.get()

            #GENEREAMOS EL REPORTE MEDIANTE FACTORY
            reporte = sistema.generar_reporte(
                tipo,
                id_reporte,
                fecha
            )

            resultado.config(
                text=reporte.generar()
            )

        except ValueError as error:
            messagebox.showerror("Error", str(error))

    #BOTON GENERAR
    boton_generar = tk.Button(
        ventana_reporte,
        text="Generar reporte",
        command=crear_reporte
    )
    boton_generar.pack(pady=15)

    #RESULTADO
    resultado = tk.Label(
        ventana_reporte,
        text="",
        font=("Arial", 11)
    )
    resultado.pack(pady=15)