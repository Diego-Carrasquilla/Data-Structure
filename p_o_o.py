class Vehiculo:
    marca = str
    combustible = int
    tipo = str
    encendido = bool

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible
        self.encendido = False
        self.en_marcha = False

    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}"

    def encender(self):
        if self.combustible <= 10:
            self.encendido = True
            return "Vehiculo encendido con combustible bajo, pasar a gasolinera"
        elif self.combustible == 0:
            self.encendido = False
            return "Vehiculo apagado"
        else:
            self.encendido = True
            return "Vehiculo encendido"

    def arrancar(self):
        if self.encendido:
            self.en_marcha = True
            return "Vehiculo en marcha"
        else:
            return "Vehiculo apagado"

    def consumir_combustible(self):
        while self.combustible > 0:
            self.combustible -= 1
            print(f"Combustible: {self.combustible}")
            if self.combustible == 10:
                self.combustible -= 1
                print("Vehiculo con combustible bajo, pasar a gasolinera")
            elif self.combustible == 0:
                self.en_marcha = False
                return "Vehiculo sin combustible"


class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Moto"
    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}, Tipo: {self.tipo}"
    

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible)
        self.tipo = "Carro"
    def __str__(self):
        return f"Marca: {self.marca}, Combustible: {self.combustible}, Tipo: {self.tipo}"


# Ejercicio 1
print("Ejercicio 1")
Vehiculo1 = Vehiculo("Toyota", 80)
print(Vehiculo1)

# Ejercicio 2 y 3
print("Ejercicio 2 y 3")
Moto1 = Moto("Honda", 20)
print(Moto1)
Carro1 = Carro("Chevrolet", 100)
print(Carro1)

# Ejercicio 4
print("Ejercicio 4")
print(Moto1.encender())
print(Moto1.arrancar())

# Ejercicio 5
print("Ejercicio 5")
print(Moto1.consumir_combustible())

