"""
Asignatura: Lenguajes y Compiladores
Periodo: 2025-II
Autor: Daniel Mata 30.810.393
------------------------------------------------------------
Problema 4:
Para un programa escrito en lenguaje C, cargado en una memoria de forma dinámica verifique si
existen palabras reservadas en C y tradúzcalas a su equivalente en español.
------------------------------------------------------------
"""


def validar_fen(fen: str, debug=False) -> bool:

    partes = fen.strip().split()

    if len(partes) != 6:
        if debug: print("Error: la FEN no tiene 6 campos separados por espacio.")
        return False

    posicion, turno, enroque, al_paso, medio_mov, num_mov = partes

    filas = posicion.split('/')

    if len(filas) != 8:
        if debug: print("Error: la posición del tablero no tiene 8 filas.")
        return False

    piezas_validas = "pnbrqkPNBRQK"

    for i, fila in enumerate(filas, start=1):
        total = 0

        if len(fila) == 0:
            if debug: print(f"Error: la fila {i} está vacía.")
            return False

        for c in fila:
            if c.isdigit():
                if not (1 <= int(c) <= 8):
                    if debug: print(f"Error: número '{c}' inválido en fila {i}.")
                    return False
                total += int(c)
            elif c in piezas_validas:
                total += 1
            else:
                if debug: print(f"Error: carácter '{c}' inválido en fila {i}.")
                return False

        if total != 8:
            if debug: print(f"Error: la fila {i} no suma 8 casillas (suma {total}).")
            return False

    if turno not in ("w", "b"):
        if debug: print("Error: el turno debe ser 'w' (blancas) o 'b' (negras).")
        return False

    enroques_validos = set("KQkq")
    if enroque != "-":
        vistos = set()
        for c in enroque:
            if c not in enroques_validos:
                if debug: print(f"Error: carácter '{c}' no válido en el campo de enroques.")
                return False
            if c in vistos:
                if debug: print(f"Error: carácter '{c}' duplicado en enroques.")
                return False
            vistos.add(c)


    columnas = "abcdefgh"
    filas_validas = "36"

    if al_paso != "-":
        if len(al_paso) != 2:
            if debug: print("Error: formato de casilla al paso inválido.")
            return False
        col, fila = al_paso[0], al_paso[1]
        if (col not in columnas) or (fila not in filas_validas):
            if debug: print(f"Error: casilla al paso '{al_paso}' no es válida (solo a-h y filas 3 o 6).")
            return False


    if not medio_mov.isdigit() or int(medio_mov) < 0:
        if debug: print("Error: el medio movimiento debe ser un número >= 0.")
        return False

    if not num_mov.isdigit() or int(num_mov) < 1:
        if debug: print("Error: el número de jugada debe ser >= 1.")
        return False

    return True

if __name__ == "__main__":
    ejemplos = [
        # Válidos
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
        "8/8/8/8/8/8/8/K6k w - - 10 50",
        # Inválidos
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPP/RNBQKBNR w KQkq - 0 1",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR x KQkq - 0 1",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KKQ - 0 1",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq e5 0 1",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - -5 1",
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"
    ]

    print("\n=== Validación de Notación FEN ===\n")

    for i, fen in enumerate(ejemplos, start=1):
        print(f"Ejemplo {i}: {fen}")
        resultado = validar_fen(fen)
        print("Resultado:", "Valida" if resultado else "Invalida")
        print("-" * 70)