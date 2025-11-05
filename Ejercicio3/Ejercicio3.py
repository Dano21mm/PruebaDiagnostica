"""
------------------------------------------------------------
Universidad Nacional Experimental de Guayana (UNEG)
Asignatura: Lenguajes y Compiladores
Periodo: 2025-II
Autor: Daniel Mata 30.810.393
------------------------------------------------------------
Problema 3:
Implemente reconocimiento de cadenas, expresiones notación científica, ip, correo electrónico.
------------------------------------------------------------
"""


def es_notacion_cientifica(cadena):
    cadena = cadena.strip()
    if 'e' in cadena.lower():
        partes = cadena.lower().split('e')
        if len(partes) != 2:
            return False
        base, exponente = partes
        if base in ('+', '-') or exponente in ('+', '-'):
            return False
        try:
            float(base)       
            int(exponente)    
            return True
        except ValueError:
            return False
    return False


def es_ip(cadena):
    partes = cadena.split('.')
    if len(partes) != 4:
        return False
    for p in partes:
        if not p.isdigit():
            return False
        n = int(p)
        if n < 0 or n > 255:
            return False
    return True


def es_correo(cadena):
    if '@' not in cadena or cadena.count('@') != 1:
        return False
    usuario, dominio = cadena.split('@')
    if not usuario or not dominio:
        return False
    if usuario[0] == '.' or usuario[-1] == '.':
        return False
    partes_dominio = dominio.split('.')
    if len(partes_dominio) < 2:
        return False
    for p in partes_dominio:
        if not p:
            return False
    if len(partes_dominio[-1]) < 2:
        return False
    return True


def reconocer_cadena(cadena):
    if es_notacion_cientifica(cadena):
        return f"{cadena} -> Notacion cientifica valida"
    elif es_ip(cadena):
        return f"{cadena} -> Direccion IP valida"
    elif es_correo(cadena):
        return f"{cadena} -> Correo electronico valido"
    else:
        return f"{cadena} -> No coincide con ningun formato conocido"

# --- Lista de pruebas ---
def main():
    entradas = [
        "1.23e+10",
        "-4.56E-3",
        "192.168.0.1",
        "255.255.255.255",
        "usuario@mail.com",
        "mal@correo",
        "300.10.1.1",
        "texto_normal"
    ]

    for e in entradas:
        print(reconocer_cadena(e))

if __name__ == "__main__":
    main()
