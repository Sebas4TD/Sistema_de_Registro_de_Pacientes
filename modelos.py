#CREAMOS LAS CLASES PACIENTE, CITA Y ATENCION
class Paciente:
    #CONSTRUCTOR QUE RECIBE LOS DATOS DE PACIENTE
    def __init__(self, id, nombre, edad, telefono):

        #EL ID CORRESPONDE AL DNI DEL PACIENTE
        if not str(id).isdigit() or len(str(id)) != 8:
            raise ValueError("El DNI debe ser de 8 dígitos")
        
        self._id = id
        self._nombre = nombre
        self._edad = edad
        self._telefono = telefono

        #MUESTRA LOS DATOS DEL PACIENTE
    def mostrar_datos(self):
        return f"{self._id} - {self._nombre} - {self._edad} - {self._telefono}"

class Cita:
    #CONSTRUCTOR QUE RECIBE LOS DATOS DE CITA
    def __init__(self, id, paciente_id, fecha, hora, motivo):
        self._id = id
        self._paciente_id = paciente_id
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo

        #MUESTRA LOS DATOS DE LA CITA
    def mostrar_datos(self):
        return (
            f"Cita {self._id} - DNI: {self._paciente_id} - "
            f"{self._fecha} - {self._hora} - {self._motivo}"
        ) 
    
class Atencion:
    #CONSTRUCTOR QUE RECIBE LOS DATOS DE ATENCION revisar
    def __init__(self, id, cita_id, diagnostico, observaciones):
        self._id = id
        self._cita_id = cita_id
        self._diagnostico = diagnostico
        self._observaciones = observaciones

        #MUESTRA LOS DATOS DE LA ATENCION
    def mostrar_datos(self):
        return (
            f"Atención {self._id} - Cita: {self._cita_id} - "
            f"{self._diagnostico} - {self._observaciones}"
        )