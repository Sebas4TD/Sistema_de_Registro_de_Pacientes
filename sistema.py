#IMPORTAMOS LAS CLASES QUE VAMOS UTILIZAR
from modelos import Paciente, Cita, Atencion
from reportes import ReporteFactory
from functools import reduce    

#CLASE PRINCIPAL QUE ADMINISTRA EL SISTEMA
class SistemaSalud:

    #VARIABLE QUE ALMACENARA LA UNICA INSTANCIA DEL SISTEMA
    _instancia = None

    #CONSTRUCTOR PRIVADO
    def __init__(self):
        self._pacientes = []
        self._citas = []
        self._atenciones = []

    #OBITNE LA UNICA INSTANCIA DEL SISTEMA
    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()

        return cls._instancia

    #REGISTA UN PACIENTE EN EL SISTEMA Y VERIFICA QUE NO EXISTA EL MISMO ID
    def registrar_paciente(self, paciente):
        if self.buscar_paciente(paciente._id) is not None:
            raise ValueError("Ya existe un paciente con ese DNI")
        
        self._pacientes.append(paciente)

    #BUSCA PACIENTE POR ID INDICADO CON **FILTER**
    def buscar_paciente(self, id):
        resultados = list(
            filter(lambda paciente: paciente._id == id, self._pacientes)
        )

        if resultados:
           return resultados[0] 

        return None

    #UTILIZAMOS **MAP** PARA OBTENER LOS NOMBRES DE TODOS LOS PACIENTES
    def obtener_nombres_pacientes(self):
        return list(
            map(lambda paciente: paciente._nombre, self._pacientes)
        )

    #UTILIZAMOS **REDUCE** PARA CONTAR LA CANTIDAD TOTAL 
    #DE LA LISTA DE PACIENTES REGISTRADOS
    def contar_pacientes(self):
        return reduce(
            lambda total, paciente: total + 1,
            self._pacientes,
            0
        )

    #BUSCAR UNA CITA CON SU ID MEDIANTE FILTER
    def buscar_cita(self, id):
        resultados = list(
            filter(lambda cita: cita._id == id, self._citas)
        )

        if resultados:
            return resultados[0]
        return None
    
    #REGISTRA UNA CITA EN EL SISTEMA
    def registrar_cita(self, cita):

        if self.buscar_paciente(cita._paciente_id) is None:
            raise ValueError("No existe un paciente con ese DNI")
        if self.buscar_cita(cita._id) is not None:
            raise ValueError("Ya existe una cita con ese ID")
        
        self._citas.append(cita)

    #DEVUELVE TODAS LAS CITAS REGISTRADAS
    def consultar_cita(self):
        return self._citas

    #REGISTRA UNA ATENCION MEDICA
    def registrar_atencion(self, atencion):

        if self.buscar_cita(atencion._cita_id) is None:
            raise ValueError("No existe una cita con ese ID")
        
        self._atenciones.append(atencion)

    #GENERA UN REPORTE UTILIZANDO FACTORY
    def generar_reporte(self, tipo, id, fecha):
        return ReporteFactory.crear_reporte(tipo, id, fecha)