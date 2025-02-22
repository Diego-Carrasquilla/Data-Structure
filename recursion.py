#funcion para encontrar el factorial de un numero con for
def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

#funcion para encontrar el factorial de un numero con while
def factorial(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado *= i
        i += 1
    return resultado

#funcion para encontrar los primeros numeros de la serie fibonacci con recursion
def fibonacci(n):
    def fibonacci_recursivo(n):
        if n <= 1:
            return n
        else:
            return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    fibonacci_recursivo(10)
    serie = []
    for i in range(n + 1):
        serie.append(fibonacci_recursivo(i))
    return serie

print(fibonacci(10))

#sumar los elementos de una lista con recursion
def sumar_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sumar_lista(lista[1:])
print(sumar_lista([1, 2, 3, 4, 5]))


#realizr una multiplicacion a traves de sumas con recursion
def multiplicar(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + multiplicar(num1, num2 - 1)
print(multiplicar(5, 3))

#realizar una division a traves de restas con recursion
def dividir(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)
print(dividir(10, 2))




