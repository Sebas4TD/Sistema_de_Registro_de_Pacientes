#CREAMOS LA CLASE BASE PARA CADA TIPO DE REPORTE
class Reporte:
    #CONSTRUCTOR DEL REPORTE
    def __init__(self, id, fecha):
        self._id = id
        self._fecha = fecha

    #METODO QUE SE IMPLEMENTARAA LOS TIPOS DE REPORTE
    def generar(self):
        pass

#CREAMOS LA CLASE REPORTE RELACIONADO CON LAS ATENCIONES MEDICAS
class ReporteAtencion(Reporte):

    #GENERA EL REPORTE DE ATENCIÓN
    def generar(self):
        return f"Reporte de atención N° {self._id} - Fecha: {self._fecha}"

#CREAMOS LA CLASE REPORTE RELACIONADO CON LAS CITAS MEDICAS
class ReporteCitas(Reporte):

    #GENERA EL REPORTE DE CITA
    def generar(self):
        return f"Reporte de citas N° {self._id} - Fecha: {self._fecha}"

#FACTORY ENGARGADA DE CREAR LOS DIFERENTES TIPOS DE REPORTES
class ReporteFactory:
    #CREAMOS UN REPORTE SEGUN EL TIPO SOLICITADO
    @staticmethod
    def crear_reporte(tipo, id, fecha):

        if tipo == "atencion":
            return ReporteAtencion(id, fecha)

        elif tipo == "citas":
            return ReporteCitas(id, fecha)

        else:
            #SI NO ES VALIDO TIRA UN MENSAJE DE ERROR 
            raise ValueError("Tipo de reporte no válido") 