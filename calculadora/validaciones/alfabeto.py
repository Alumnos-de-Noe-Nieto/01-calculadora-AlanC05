"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    """
    Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.

    💡 PISTA: Usa .strip() para eliminar espacios en blanco laterales
    💡 PISTA: Retorna False si la cadena está vacía después de eliminar espacios
    💡 PISTA: Recuerda: espacios en blanco laterales NO deben afectar la validación

    Args:
        cadena (str): La cadena a evaluar. Ej: "XIV"

    Returns:
        bool: True si la cadena es completamente válida, False en caso contrario.

    Examples:
        >>> validar_simbolos("XIV")
        True
        >>> validar_simbolos("MCMXCIV")
        True
        >>> validar_simbolos("ABCD")
        False
        >>> validar_simbolos("X-IV")
        False
        >>> validar_simbolos("")
        False
        >>> validar_simbolos("  XIV  ")
        True
    """
    # 1. Aplicamos la pista de eliminar espacios laterales
    cadena_limpia = cadena.strip()

    # 2. Pista: si está vacía después del strip, no es válida
    if not cadena_limpia:
        return False

    # 3. Definimos las letras permitidas (el alfabeto romano)
    alfabeto = "IVXLCDM"

    # 4. Manera de decir que se revise que todo el contenido esté en el alfabeto
    return all(caracter in alfabeto for caracter in cadena_limpia)
