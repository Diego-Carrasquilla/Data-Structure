# #CLASE DE LISTAS Y DICCIONARIOS

# def agregar_numero(lista, numero):
#     lista.append(numero)
#     print(f"Número {numero} agregado a la lista.")


# def eliminar_numero(lista, numero):
#     if numero in lista:
#         indice = lista.index(numero)
#         if 0 <= indice < len(lista):
#             lista.pop(indice)
#             print(f"Número {numero} eliminado de la lista en el índice {indice}.")
#     else:
#         print(f"Número {numero} no encontrado en la lista.")
        
# lista = []
# while True:
#         accion = input("¿Deseas agregar o eliminar un número? (agregar/eliminar/salir): ").strip().lower()
#         if accion == "salir":
#             break
#         elif accion in ["agregar", "eliminar"]:
#             try:
#                 numero = int(input("Introduce el número: "))
#                 if accion == "agregar":
#                     agregar_numero(lista, numero)
#                     print("Lista Modificada:", lista)
#                 elif accion == "eliminar":
#                     eliminar_numero(lista, numero)
#                     print("Lista Modificada:", lista)
#             except ValueError:
#                 print("Por favor, introduce un número válido.")
#         else:
#             print("Acción no válida. Por favor, elige 'agregar', 'eliminar' o 'salir'.")
# print("Programa terminado. Lista final:", lista)


#EJERCICIO DICCIOPNARIOS

# def agregar_persona(diccionario, nombre, edad):
#     diccionario[nombre] = {"edad": edad }
#     print(f"Persona {nombre} agregada al diccionario.")
#     print(diccionario)

# def eliminar_persona(diccionario, nombre):
#     if nombre in diccionario:
#         diccionario.pop(nombre)
#         print(f"Persona {nombre} eliminada del diccionario.")
#         print(diccionario)
#     else:
#         print(f"Persona {nombre} no encontrada en el diccionario.")

# personas = {}
# while True:
#     accion = input("¿Deseas agregar o eliminar una persona? (agregar/eliminar/salir): ").strip().lower()
#     if accion == "salir":
#         break
#     elif accion in ["agregar", "eliminar"]:
#         nombre = input("Introduce el nombre de la persona: ")
#         if accion == "agregar":
#             try:
#                 edad = int(input("Introduce la edad de la persona: "))
#                 agregar_persona(personas, nombre, edad)
#             except ValueError:
#                 print("Por favor, introduce un número válido.")
#         elif accion == "eliminar":
#             eliminar_persona(personas, nombre)
#     else:
#         print("Acción no válida. Por favor, elige 'agregar', 'eliminar' o 'salir.'")
              
# Ejercicio triángulo de números
# def imprimir_triangulo(numero):
#     for i in range(1, numero + 1):
#         triangulo = ' '.join(str(x) for x in range(1, i + 1))
#         print(triangulo)

# while True:
#     try:
#         numero = int(input("Introduce un número: "))
#         imprimir_triangulo(numero)
#         break
#     except ValueError:
#         print("Por favor, introduce un número válido.")

# Ejercicio calcular la multiplicacion de 2 numeros (solo usando sumas)
def multiplicar(num1, num2):
    resultado = 0
    for i in range(num2):
        resultado += num1
    return resultado

while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        print(f"El resultado de multiplicar {num1} por {num2} es {multiplicar(num1, num2)}.")
        break
    except ValueError:
        print("Por favor, introduce un número válido.")