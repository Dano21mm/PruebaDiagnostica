"""
------------------------------------------------------------
Asignatura: Lenguajes y Compiladores
Periodo: 2025-II
Autor: Daniel Mata 30.810.393
------------------------------------------------------------
Problema 2:
Dado un número entero no negativo n, a) genere los coeficientes del polinomio (x+1) n
, muestre el resultado del polinomio y b) muestre por pasos el cálculo para x dado, f(x) = (x+1)n ,según el
polinomio generado. Implemente el algoritmo utilizando memoria dinámica. Para generar los polinomios de (x+1)n

Codificar en dos lenguajes y medir el tiempo de ejecución de cada código para n=100 el resultado
escribirlo en archivo txt.
------------------------------------------------------------
"""

import time

def generar_coeficientes(n):
    coef = [1]
    for i in range(1, n + 1):
        nuevo = [1]
        for j in range(1, i):
            nuevo.append(coef[j - 1] + coef[j])
        nuevo.append(1)
        coef = nuevo
    return coef

def calcular_polinomio(coef, n, x, f):
    resultado = 0
    for i, c in enumerate(coef):
        termino = c * (x ** (n - i))
        f.write(f"Paso {i+1}: {c} * ({x})^{n - i} = {termino}\n")
        resultado += termino
    return resultado

n = 100
x = 2
inicio = time.time()

with open("resultado_python.txt", "w", encoding="utf-8") as f:
    coef = generar_coeficientes(n)
    f.write(f"Coeficientes de (x + 1)^{n}:\n")
    f.write(" ".join(map(str, coef)) + "\n\nCálculo paso a paso:\n")
    resultado = calcular_polinomio(coef, n, x, f)
    fin = time.time()
    tiempo = fin - inicio
    f.write(f"\nResultado f({x}) = {resultado:,}\n")
    f.write(f"Tiempo de ejecución: {tiempo:.6f} segundos\n")

print("Cálculo completado. Revisa los archivos 'resultado_c.txt' y 'resultado_python.txt'")
