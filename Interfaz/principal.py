#IMPORTAMOS TKINTER
import tkinter as tk

#IMPORTAMOS SISTEMA
from sistema import SistemaSalud

#IMPORTAMOS LAS FUNCIONES DE PACIENTE
from Interfaz.pacientes import registrar_paciente, buscar_paciente
from Interfaz.citas import registrar_cita, consultar_citas
from Interfaz.atenciones import registrar_atencion
from Interfaz.ventana_reportes import generar_reporte

#OBTENEMOS INSTANCIA DEL SISTEMA
sistema = SistemaSalud.get_instancia()

#CREAMOS LA VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Centro de Salud \"Santa Rosa\"")
ventana.geometry("700x500")

#TITULO PRINCIPAL
titulo = tk.Label(
    ventana,
    text="Sistema de Registro de Pacientes",
    font=("Arial", 20)
)
titulo.pack(pady=20)

#BOTON REGISTRAR PACIENTE
boton_registrar_paciente = tk.Button(
    ventana,
    text="Registrar paciente",
    command=lambda: registrar_paciente(ventana, sistema)
)
boton_registrar_paciente.pack(pady=5)

#BOTON BUSCAR PACIENTE
boton_buscar_paciente = tk.Button(
    ventana,
    text="Buscar paciente",
    command=lambda: buscar_paciente(ventana, sistema)
)
boton_buscar_paciente.pack(pady=5)

#BOTON REGISTRAR CITA
boton_registrar_citas = tk.Button(
    ventana,
    text="Registrar cita",
    command=lambda: registrar_cita(ventana, sistema)
)
boton_registrar_citas.pack(pady=5)

#BOTON CONSULTAR CITA
boton_consultar_citas = tk.Button(
    ventana,
    text="Consultar citas",
    command=lambda: consultar_citas(ventana, sistema)
)
boton_consultar_citas.pack(pady=5)

#BOTON REGISTRAR ATENCION
boton_registrar_atencion = tk.Button(
    ventana,
    text="Registrar atención",
    command=lambda: registrar_atencion(ventana, sistema)
)
boton_registrar_atencion.pack(pady=5)

#BOTON GENERAR REPORTE
boton_generar_reporte = tk.Button(
    ventana,
    text="Generar reporte",
    command=lambda: generar_reporte(ventana, sistema)
)
boton_generar_reporte.pack(pady=5)

#BOTON SALIR
boton_salir = tk.Button(
    ventana,
    text="Salir",
    command=ventana.destroy
)
boton_salir.pack(pady=15)

#INICIAMOS LA INTERFAZ
ventana.mainloop()