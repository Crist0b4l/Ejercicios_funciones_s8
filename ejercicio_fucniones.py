'''Ejercicios funciones'''


import math
import re


def mostrar_menu():
    print("1. Calcuiar iva")
    print("2. Aplicar descuento")
    print("3. Calcular IMC")
    print("4. Salir")


def calcular_iva(num):
    iva_calculado = num * 0.19
    precio_con_iva = num + iva_calculado
    return (precio_con_iva)


def descuento(num):
    dcto_aplicado = num * 0.7
    return dcto_aplicado


def calcular_imc(peso, estatura):
    imc = peso/(estatura ** 2)
    if imc < 18.5:
        print(f"{imc:.1f} = Bajo peso")
    elif imc >= 18.5 and imc <= 24.9:
        print(f"{imc:.1f} = Adecuado")
    elif imc >= 25 and imc <= 29.9:
        print(f"{imc:.1f} = Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print(f"{imc:.1f} = Obesidad grado 1")
    elif imc >= 35 and imc <= 39.9:
        print(f"{imc:.1f} = Obesidad grado 2")
    elif imc >= 40:
        print(f"{imc:.1f} = Obesidad grado 3")


while True:
    mostrar_menu()
    print("Ingrese una opción")
    opcion = int(input())

    if opcion == 1:
        num = float(input("Ingrese el valor para calcular el IVA: "))
        print(f"El precio del producto con IVA es: {calcular_iva(num):.2f}")
    elif opcion == 2:
        num = float(
            input("Ingrese el precio del producto para aplicar el descuento del 30%: "))
        print(f"El precio con el descuento aplicado es ${descuento(num):.2f}")
    elif opcion == 3:
        peso = float(input("Ingrese su peso en Kg: "))
        estatura = float(input("Ingrese su estatura en metros: "))
        calcular_imc(peso, estatura)
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Seleccione una opción válida")


# Ejercicio 2 menu con operaciones matematicas


def menu2():
    print("Menú")
    print("1. Número primo")
    print("2. Factorial")
    print("3. Palíndrome")
    print("4. Salir")


def num_primo(num):
    if num <= 1:
        print(f"{num} No es un número primo")
        return False
    if num == 2:
        print(f"{num} Es el único número par primo")
        return True
    if num % 2 == 0:
        print(f"{num} No es un número primo")
        return False
    for n in range(3, num):
        if num % n == 0:
            print(f"{num} No es un número primo, es divisible por {n}")
            return False
    print(f"{num} Es un número primo")
    return True


def factorial(num):
    secuencia = "*".join(str(i) for i in range(num, 0, -1))
    resultado = math.factorial(num)
    print(f"El factorial de {num} es: {secuencia} = {resultado}")


def es_palindromo(frase):
    frase_incluida = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    if frase_incluida == frase_incluida[::-1]:
        print(f"{frase} Es un palíndromo")
    else:
        print(f"{frase} No es un palíndromo")


while True:
    menu2()
    print("Elige una opción")
    opcion = int(input())

    if opcion == 1:
        while True:
            num = int(
                input("Ingrese un número entero entre 1 y 15 para verificar si es primo: "))
            if num < 1 or num > 15:
                print("Por favor ingrese un número dentro del rango (1-15)")
            else:
                num_primo(num)
                break

    elif opcion == 2:
        while True:
            num = int(
                input("Ingrese un número entero entre 3 y 10 para conocer su factorial: "))
            if num < 3 or num > 10:
                print("Por favor ingrese un número dentro del rango (3-10)")
            else:
                factorial(num)
                break

    elif opcion == 3:
        frase = input("Ingrese una frase para comprobar si es un palíndromo: ")
        es_palindromo(frase)

    elif opcion == 4:
        print("Saliendo del programa...")
        print("Autor: Cristóbal Varas Polanco")
        break
    else:
        print("Seleccione una opción válida")
