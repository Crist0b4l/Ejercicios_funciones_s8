'''Ejercicios funciones'''


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
