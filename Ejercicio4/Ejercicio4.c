/*
------------------------------------------------------------
Asignatura: Lenguajes y Compiladores
Periodo: 2025-II
Autor: Daniel Mata 30.810.393
------------------------------------------------------------
Problema 4:
Para un programa escrito en lenguaje C, cargado en una memoria de forma dinámica verifique si
existen palabras reservadas en C y tradúzcalas a su equivalente en español.
------------------------------------------------------------
*/



#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char *palabra;
    char *traduccion;
} PalabraReservada;

PalabraReservada reservadas[] = {
    {"int", "entero"},
    {"float", "flotante"},
    {"double", "doble"},
    {"char", "caracter"},
    {"void", "vacio"},
    {"if", "si"},
    {"else", "sino"},
    {"for", "para"},
    {"while", "mientras"},
    {"do", "hacer"},
    {"switch", "cambiar"},
    {"case", "caso"},
    {"break", "romper"},
    {"continue", "continuar"},
    {"return", "retornar"},
    {"struct", "estructura"},
    {"typedef", "definir_tipo"},
    {"enum", "enumeracion"},
    {"const", "constante"},
    {"sizeof", "tamano_de"},
    {"default", "predeterminado"}
};

int esPalabraReservada(char *token, char **traduccion) {
    int n = sizeof(reservadas) / sizeof(reservadas[0]);
    for(int i = 0; i < n; i++) {
        if(strcmp(token, reservadas[i].palabra) == 0) {
            *traduccion = reservadas[i].traduccion;
            return 1;
        }
    }
    return 0;
}


bool yaImprimida(char *token, char **lista, int cantidad) {
    for(int i = 0; i < cantidad; i++) {
        if(strcmp(token, lista[i]) == 0) {
            return true;
        }
    }
    return false;
}

int main() {
    char codigo[] =
        "int main() {\n"
        "    int suma = 0;\n"
        "    int n = 5;\n"
        "    for(int i = 1; i <= n; i++) {\n"
        "        suma += i;\n"
        "    }\n"
        "    if(suma > 10) {\n"
        "        printf(\"La suma es mayor que 10\\n\");\n"
        "    } else {\n"
        "        printf(\"La suma es menor o igual a 10\\n\");\n"
        "    }\n"
        "    return 0;\n"
        "}";

    char *separadores = " \t\n;(){}[],";
    char *token = strtok(codigo, separadores);

    char *encontradas[50]; 
    int contador = 0;

    printf("Palabras reservadas encontradas y su traduccion (sin duplicados):\n");
    while(token != NULL) {
        char *traduccion;
        if(esPalabraReservada(token, &traduccion)) {
            if(!yaImprimida(token, encontradas, contador)) {
                printf("%s -> %s\n", token, traduccion);
                encontradas[contador++] = token;
            }
        }
        token = strtok(NULL, separadores);
    }

    return 0;
}

