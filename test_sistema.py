#IMPORTAMOS PYTEST PARA TESTEAR NUESTRO SISTEMA
import pytest

#IMPORTAMOS LOS MODELOS Y SISTEMA
from modelos import Paciente, Cita, Atencion
from sistema import SistemaSalud

#OBTENEMOS UNA ISNTANCIA LIMPIA DEL SISTEMA PARA CADA PRUEBA
def obtener_sisteam():
    sistema = SistemaSalud.get_instancia()

    #LIMPIAMOS LOS REGISTROS ANTERIORES
    sistema._pacientes.clear()
    sistema._citas.clear()
    sistema._atenciones.clear()

    return sistema

#COMPROBAMOS QUE SE PUEDA REGISTRAR Y BUSCAR UN PACIENTE
def test_registrar_paciente():
    sistema = obtener_sisteam()

    paciente = Paciente(
        "12345678",
        "Luis Fernandez",
        25,
        "999999999"
    )

    sistema.registrar_paciente(paciente)
    resultado = sistema.buscar_paciente("12345678")

    assert resultado is not None

#COMPROBAMOS QUE EL SISTEMA RECHACE UN DNI INCORRECTO
def test_dni_invalido():
    with pytest.raises(ValueError):
        Paciente(
            "123",
            "Luis Fernandez",
            25,
            "999999999"
        )

#COMPROBRAMOS QUE EL SISTEMA RECHACE NOMBRE CON NUMEROS O CARACTERES ESPECIALES
def test_nombre_invalido():
    with pytest.raises(ValueError):
        Paciente("12345678", "Juan123", 20, "987654321")

#COMPROBAMOS QUE LA EDAD SEA UN NUMERO POSITIVO
def test_edad_invalida():
    with pytest.raises(ValueError):
        Paciente("12345678", "Juan Perez", -5, "987654321")

#COMPROBAMOS QUE EL TELEFONO SEA UN NUMERO DE 9 DIGITOS
def test_telefono_invalido():
    with pytest.raises(ValueError):
        Paciente("12345678", "Telefono", 30, "12345")

#COMPROBAMOS QUE NO SE PUEDA REGISTRAR EL MISMO PACIENTE DOS VECES
def test_no_registrar_paciente_repetido():
    sistema = obtener_sisteam()

    paciente = Paciente(
        "12345678",
        "Luis Fernandez",
        25,
        "999999999"
    )

    sistema.registrar_paciente(paciente)

    with pytest.raises(ValueError):
        sistema.registrar_paciente(paciente)

#COMPROBAMOS QUE UNA CITA NECESITE UN PACIENTE EXISTENTE
def test_no_registrar_cita_sin_paciente():
    sistema = obtener_sisteam()

    cita = Cita(
        "1",
        "99999999",
        "20/09/2026",
        "10:00",
        "Consulta"
    )

    with pytest.raises(ValueError):
        sistema.registrar_cita(cita)

#COMPROBAMOS QUE UNA ATENCION NECESITE UNA CITA EXISTENTE
def test_no_registrar_atencion_sin_cita():
    sistema = obtener_sisteam()

    atencion = Atencion(
        "1",
        "999",
        "Gripe",
        "Reposo"
    )

    with pytest.raises(ValueError):
        sistema.registrar_atencion(atencion)
