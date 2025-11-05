#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


long long* generar_coeficientes(int n) {
    long long* coef = (long long*)malloc((n + 1) * sizeof(long long));
    long long* prev = (long long*)malloc((n + 1) * sizeof(long long));

    coef[0] = 1;
    for (int i = 1; i <= n; i++) {
        coef[0] = 1;
        for (int j = 1; j < i; j++)
            coef[j] = prev[j - 1] + prev[j];
        coef[i] = 1;

        for (int k = 0; k <= i; k++)
            prev[k] = coef[k];
    }

    free(prev);
    return coef;
}

double calcular_polinomio(long long* coef, int n, double x, FILE* f) {
    double resultado = 0;
    for (int i = 0; i <= n; i++) {
        double termino = coef[i] * pow(x, n - i);
        fprintf(f, "Paso %d: %lld * (%.2f)^%d = %.2f\n", i + 1, coef[i], x, n - i, termino);
        resultado += termino;
    }
    return resultado;
}

int main() {
    int n = 100;
    double x = 2;
    clock_t inicio, fin;
    inicio = clock();

    FILE* f = fopen("resultado_c.txt", "w");
    if (!f) {
        printf("Error al crear archivo.\n");
        return 1;
    }

    long long* coef = generar_coeficientes(n);
    fprintf(f, "Coeficientes de (x + 1)^%d:\n", n);
    for (int i = 0; i <= n; i++) fprintf(f, "%lld ", coef[i]);
    fprintf(f, "\n\nCálculo paso a paso:\n");

    double resultado = calcular_polinomio(coef, n, x, f);
    fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;
    fprintf(f, "\nResultado f(%.2f) = %.2f\n", x, resultado);
    fprintf(f, "Tiempo de ejecución: %.6f segundos\n", tiempo);

    fclose(f);
    free(coef);
    return 0;
}
