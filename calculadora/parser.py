"""
Nivel 7: Parsing de Expresiones
Este módulo contiene las funciones para parsear expresiones aritméticas con números romanos.
"""

from dataclasses import dataclass

from calculadora.error import ExpresionInvalida


@dataclass
class Token:
    """
    Representa un token en una expresión aritmética de números romanos.

    Attributes:
        tipo: El tipo de token ("ROMANO", "SUMA", "RESTA", "ESPACIO")
        valor: El valor del token (cadena)
        posicion: La posición del token en la expresión original
    """

    tipo: str
    valor: str
    posicion: int


def evaluar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza y valida una expresión aritmética de números romanos.

    Nivel 7.1: Parsing completo de expresiones aritméticas de números romanos.

    💡 PISTA: Primero llama a tokenizar_expresion(expresion) para obtener los tokens
    💡 PISTA: Luego llama a validar_estructura_tokens(tokens) para validar la estructura
    💡 PISTA: Si validar_estructura_tokens(tokens) retorna False, lanza ExpresionInvalida
    💡 PISTA: Si la expresión está vacía (no tokens), retorna lista vacía []
    💡 PISTA: Usa try-except para capturar errores de tokenizar_expresion
    💡 PISTA: Mensaje de error: f'La expresión "{expresion}" tiene una estructura inválida'

    Args:
        expresion (str): La expresión a parsear

    Returns:
        List[Token]: La lista de tokens encontrados (vacía si la expresión es vacía)

    Raises:
        ExpresionInvalida: Si la expresión contiene caracteres inválidos o tiene estructura inválida

    Examples:
        >>> evaluar_expresion("XIV + LX")
        [Token("ROMANO", "XIV", 0), Token("ESPACIO", " ", 3), Token("SUMA", "+", 4), ...]
        >>> evaluar_expresion("")
        []
    """
    # Si la expresión está vacía, retorna lista vacía
    if not expresion or expresion.strip() == "":
        return []

    try:
        # Primero llama a tokenizar_expresion
        tokens = tokenizar_expresion(expresion)

        # Luego llama a validar_estructura_tokens
        if not validar_estructura_tokens(tokens):
            # Mensaje de error específico
            raise ExpresionInvalida(f'La expresion "{expresion}" tiene una estructura inválida')

        return tokens

    except ExpresionInvalida as e:
        # Usa try-except para capturar errores de tokenización
        raise e


def tokenizar_expresion(expresion: str) -> list[Token]:
    """
    Tokeniza una expresión de texto en una lista de tokens.

    Nivel 7.2: Tokenización de expresiones aritméticas.

    💡 PISTA: Recorre la expresión caracter por caracter con un índice `i` usando while
    💡 PISTA: Usa if-elif para identificar el tipo de cada caracter:
    💡 PISTA:   - Espacio (' ') → Token('ESPACIO', ' ', i)
    💡 PISTA:   - Suma ('+') → Token('SUMA', '+', i)
    💡 PISTA:   - Resta ('-') → Token('RESTA', '-', i)
    💡 PISTA:   - Romano ('IVXLCDM') → Lee todos los caracteres romanos consecutivos
    💡 PISTA: Para números romanos:
    💡 PISTA:   - Guarda la posición inicial: inicio = i
    💡 PISTA:   - Avanza i mientras el caracter actual esté en 'IVXLCDM'
    💡 PISTA:   - Crea Token('ROMANO', expresion[inicio:i], inicio)
    💡 PISTA: Si el caracter no es ninguno de los anteriores, lanza ExpresionInvalida
    💡 PISTA: Mensaje de error: f"Carácter inválido '{expresion[i]}' en posición {i}"
    💡 PISTA: Ejemplo "XIV + LX":
    💡 PISTA:   - X(0) → ROMANO "XIV", i=3
    💡 PISTA:   - espacio(3) → ESPACIO, i=4
    💡 PISTA:   - +(4) → SUMA, i=5
    💡 PISTA:   - espacio(5) → ESPACIO, i=6
    💡 PISTA:   - L(6) → ROMANO "LX", i=8

    Args:
        expresion (str): La expresión a tokenizar

    Returns:
        List[Token]: La lista de tokens encontrados

    Raises:
        ExpresionInvalida: Si la expresión contiene caracteres inválidos

    Examples:
        >>> tokenizar_expresion("XIV + LX")
        [Token("ROMANO", "XIV", 0), Token("ESPACIO", " ", 3), Token("SUMA", "+", 4), ...]
        >>> tokenizar_expresion("X+V")
        [Token("ROMANO", "X", 0), Token("SUMA", "+", 1), Token("ROMANO", "V", 2)]
    """
    tokens = []
    i = 0
    # Recorre la expresión con un índice "i" usando while
    while i < len(expresion):
        caracter = expresion[i]

        # Espacio
        if caracter == " ":
            tokens.append(Token("ESPACIO", " ", i))
            i += 1

        # Suma
        elif caracter == "+":
            tokens.append(Token("SUMA", "+", i))
            i += 1

        # Resta
        elif caracter == "-":
            tokens.append(Token("RESTA", "-", i))
            i += 1

        # Romano
        elif caracter.upper() in "IVXLCDM":
            inicio = i
            # Avanza mientras el caracter sea romano
            while i < len(expresion) and expresion[i].upper() in "IVXLCDM":
                i += 1
            tokens.append(Token("ROMANO", expresion[inicio:i], inicio))
        else:
            # Si el carácter no es válido
            raise ExpresionInvalida(f'Carácter inválido "{expresion[i]}" en posición {i}')

    return tokens

def validar_estructura_tokens(tokens: list[Token]) -> bool:
    """
    Valida que la expresión tenga una estructura válida.

    Nivel 7.3: Validación de estructura de tokens.

    💡 PISTA: Filtra tokens de tipo 'ESPACIO' para facilitar la validación
    💡 PISTA: Usa list comprehension: [t for t in tokens if t.tipo != 'ESPACIO']
    💡 PISTA: Verifica que haya al menos 3 tokens (ROMANO, OPERADOR, ROMANO)
    💡 PISTA: Verifica que el número de tokens sea impar (alternancia correcta)
    💡 PISTA: Verifica que el primer token sea de tipo 'ROMANO'
    💡 PISTA: Verifica que el último token sea de tipo 'ROMANO'
    💡 PISTA: Recorre los tokens con enumerate(i, token):
    💡 PISTA:   - Posiciones pares (0, 2, 4, ...) deben ser 'ROMANO'
    💡 PISTA:   - Posiciones impares (1, 3, 5, ...) deben ser 'SUMA' o 'RESTA'
    💡 PISTA: Ejemplo [ROMANO, SUMA, ROMANO] → True (alternancia correcta)
    💡 PISTA: Ejemplo [SUMA, ROMANO] → False (empieza con operador)
    💡 PISTA: Ejemplo [ROMANO, SUMA, ROMANO, RESTA, ROMANO] → False (dos operadores seguidos)

    Args:
        tokens (List[Token]): La lista de tokens a validar

    Returns:
        bool: True si la estructura es válida, False en caso contrario

    Examples:
        >>> validar_estructura_tokens([Token("ROMANO", "X", 0), Token("SUMA", "+", 1), Token("ROMANO", "V", 2)])
        True
        >>> validar_estructura_tokens([Token("SUMA", "+", 0), Token("ROMANO", "X", 1)])
        False
    """
    # Filtra tokens de tipo espacio
    tokens_filtrados = [t for t in tokens if t.tipo != "ESPACIO"]

    # Si no hay tokens, es válido
    if not tokens_filtrados:
        return True

    # Verifica que haya al menos 3 tokens que sea impar
    if len(tokens_filtrados) < 3 or len(tokens_filtrados) % 2 == 0:
        return False

    # Verifica que el primero y el último sean romano
    if tokens_filtrados[0].tipo != "ROMANO" or tokens_filtrados[-1].tipo != "ROMANO":
        return False

    # Recorre con enumerate para alternancia
    for i, token in enumerate (tokens_filtrados):
        # Posiciones pares
        if i % 2 == 0:
            if token.tipo != "ROMANO":
                return False

        # Posiciones impares
        else:
            if token.tipo not in ["SUMA", "RESTA"]:
                return False

    return True
