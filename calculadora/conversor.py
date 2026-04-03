"""
Nivel 6: Generación de Código - Conversión de Romano a Entero
Este módulo contiene la función para convertir números romanos a enteros.
"""
from calculadora.error import ExpresionInvalida
from calculadora.validaciones.alfabeto import validar_simbolos
from calculadora.validaciones.orden_descendente import validar_orden_descendente
from calculadora.validaciones.repeticiones_icxm import validar_repeticiones_icxm
from calculadora.validaciones.repeticiones_vld import validar_repeticiones_vld
from calculadora.validaciones.restas import validar_restas

VALORES = {
    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def romano_a_entero(cadena: str) -> int:
    """
    Convierte una cadena de números romanos válida a su valor entero correspondiente.

    Nivel 6: Generación de Código - Conversión Romano → Entero

    💡 PISTA PRIMERO: Llama a todas las validaciones (Niveles 1-5) ANTES de convertir
    💡 PISTA: Usa validar_simbolos(cadena), validar_repeticiones_icxm(cadena), etc.
    💡 PISTA: Si alguna validación retorna False, lanza ExpresionInvalida con mensaje descriptivo (ej: 'contiene símbolos inválidos', 'repetición I/X/C/M', etc.)

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-5

    Returns:
        int: El valor entero correspondiente

    Examples:
        >>> romano_a_entero("I")
        1
        >>> romano_a_entero("V")
        5
        >>> romano_a_entero("IV")
        4
        >>> romano_a_entero("IX")
        9
        >>> romano_a_entero("XIV")
        14
        >>> romano_a_entero("MCMXCIV")
        1994
        >>> romano_a_entero("MMMCMXCIX")
        3999

    Raises:
        ExpresionInvalida: Si la cadena no es válida según las reglas de números romanos (símbolos inválidos, repeticiones inválidas, orden incorrecto, restas inválidas)
    """
    # 1. Validacones de los anteriores niveles. Si alguna falla, lanzamos la excepción con el mensaje descriptivo
    if not validar_simbolos(cadena):
        raise ExpresionInvalida("contiene símbolos inválidos")

    if not validar_repeticiones_icxm(cadena):
        raise ExpresionInvalida("repetición I/X/C/M")

    if not validar_repeticiones_vld(cadena):
        raise ExpresionInvalida("repetición V/L/D")

    if not validar_orden_descendente(cadena):
        raise ExpresionInvalida("orden incorrecto")

    if not validar_restas(cadena):
        raise ExpresionInvalida("restas inválidas")

    # 2. Lógica de conversión
    total = 0
    cadena_limpia = cadena.strip().upper()

    for i in range(len(cadena_limpia)):
        valor_actual = VALORES[cadena_limpia[i]]

        # Si no es el último símbolo y el actual es menor al siguiente, se resta
        if i + 1 < len(cadena_limpia) and valor_actual < VALORES[cadena_limpia[i+1]]:
            total -= valor_actual
        else:
            # En cualquier otro caso, se suma
            total += valor_actual

    return total
