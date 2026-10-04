#CREAMOS LAS CLASES PACIENTE, CITA Y ATENCION
class Paciente:
    #CONSTRUCTOR QUE RECIBE LOS DATOS DE PACIENTE
    def __init__(self, id, nombre, edad, telefono):

        #EL ID CORRESPONDE AL DNI DEL PACIENTE
        if not str(id).isdigit() or len(str(id)) != 8:
            raise ValueError("El DNI debe ser de 8 dígitos")
        
        self._id = id

        #VALIDAMOS QUE SE PERMITA SOLO LETRAS EN EL NOMBRE
        if not nombre.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras")
        
        self._nombre = nombre

        #VALIDAMOS QUE LA EDAD SEA UN NUMERO POSITIVO
        if not str(edad).isdigit() or int(edad) <= 0:
            raise ValueError("La edad debe ser un número positivo")
        
        self._edad = edad

        #VALIDAMOS QUE EL TELEFONO SEA UN NUMERO DE 9 DIGITOS
        if not str(telefono).isdigit() or len(str(telefono)) != 9:
            raise ValueError("El número telefónico debe ser de 9 dígitos")
        
        self._telefono = telefono

        #MUESTRA LOS DATOS DEL PACIENTE
    def mostrar_datos(self):
        return (
            f"DNI: {self._id}\n"
            f"Nombre: {self._nombre}\n"
            f"Edad: {self._edad}\n"
            f"Teléfono:{self._telefono}"
        )

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