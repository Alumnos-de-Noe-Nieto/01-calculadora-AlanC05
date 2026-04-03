"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""
# Constantes necesarias para la lógica del nivel
VALORES = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
SUSTRACCIONES_VALIDAS = { "IV", "IX", "XL", "XC", "CD", "CM"}

def validar_orden_descendente(cadena: str) -> bool:
    """
    Valida que los símbolos estén en orden descendente de valor (izquierda a derecha).

    Nivel 4: Análisis Sintáctico - Orden descendente

    💡 PISTA: Usa la constante VALORES con el valor numérico de cada símbolo
    💡 PISTA: Usa la constante SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    💡 PISTA: Recorre la cadena con un índice `i` usando un while loop
    💡 PISTA: Si cadena[i:i+2] está en SUSTRACCIONES_VALIDAS:
    💡 PISTA:   - Verifica que no haya repeticiones antes (ej: IIV es inválido, cadena[i-1] == cadena[i])
    💡 PISTA:   - Verifica que el símbolo anterior sea mayor al valor sustraído
    💡 PISTA:   - Verifica que después de la sustracción, el orden descendente continúe
    💡 PISTA: Si no es sustracción, verifica VALORES[cadena[i]] >= VALORES[cadena[i+1]]
    💡 PISTA: Ejemplo: "XVI" → X(10) >= V(5) >= I(1) → True
    💡 PISTA: Ejemplo: "IVX" → I(1) < V(5), pero luego V(5) < X(10) → False
    💡 PISTA: Ejemplo: "IIV" → I repetido antes de IV → False
    💡 PISTA: Ejemplo: "MCMXCIV" → varias sustracciones válidas → True

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-3

    Returns:
        bool: True si el orden es correcto, False en caso contrario

    Examples:
        >>> validar_orden_descendente("XVI")
        True
        >>> validar_orden_descendente("IVX")
        False
        >>> validar_orden_descendente("MCMXCIV")
        True
        >>> validar_orden_descendente("IIV")
        False
        >>> validar_orden_descendente("VIV")
        False
    """
    i = 0
    ultimo_valor = 1001 # Empezamos con un valor mayor al máximo, es decir M

    while i < len(cadena):
        simbolo_actual = cadena[i]
        valor_actual = VALORES[simbolo_actual]

        # Revisamos si estamos ante una posible sustracción
        sustraccion_detectada = False
        if i + 1 < len(cadena):
            par = cadena[i:i+2]
            if par in SUSTRACCIONES_VALIDAS:
                sustraccion_detectada = True
                valor_sustraccion = VALORES[cadena[i+1]] - VALORES[cadena[i]]

                # No puede haber repeticiones antes
                if i > 0 and cadena[i-1] == cadena[i]:
                    return False

                # El valor de la sustracción debe ser menor al anterior
                if valor_sustraccion >= ultimo_valor:
                    return False

                ultimo_valor = valor_sustraccion
                i += 2 # Saltamos los dos caracteres de la sustracción

        if not sustraccion_detectada:
            # Si no es sustracción, el valor debe ser menor o igual al anterior
            if valor_actual > ultimo_valor:
                return False

            ultimo_valor = valor_actual
            i += 1

    return True
