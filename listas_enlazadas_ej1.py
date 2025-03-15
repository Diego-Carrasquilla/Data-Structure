from typing import Optional

class NodoAnimal:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class Animal:
    def __init__(self, nombre: str, edad: int, tipo: str):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"

class ListaAnimales:
    def __init__(self):
        self.cabeza = None
    
    def agregar_animal(self, nombre: str, edad: int, tipo: str):
        if self.buscar_animal(nombre, tipo):
            print(f"El animal {nombre} de tipo {tipo} ya existe en la lista.")
            return
        
        nuevo_animal = NodoAnimal(Animal(nombre, edad, tipo))
        nuevo_animal.siguiente = self.cabeza
        self.cabeza = nuevo_animal
    
    def buscar_animal(self, nombre: str, tipo: str) -> Optional[Animal]:
        temp = self.cabeza
        while temp:
            if temp.animal.nombre == nombre and temp.animal.tipo == tipo:
                return temp.animal
            temp = temp.siguiente
        return None
    
    def imprimir_lista_iterativa(self):
        temp = self.cabeza
        while temp:
            print(temp.animal)
            temp = temp.siguiente
    
    def imprimir_lista_recursiva(self, nodo: Optional[NodoAnimal]):
        if nodo:
            print(nodo.animal)
            self.imprimir_lista_recursiva(nodo.siguiente)

# Ejemplo de uso
if __name__ == "__main__":
    lista_animales = ListaAnimales()
    lista_animales.agregar_animal("Pantera", 5, "Felino")
    lista_animales.agregar_animal("León", 4, "Felino")
    lista_animales.agregar_animal("Tigre", 3, "Felino")
    lista_animales.agregar_animal("León", 4, "Felino")  # No se agregará por ser duplicado
    
    print("\nLista enlazada iterativa:")
    lista_animales.imprimir_lista_iterativa()
    
    print("\nLista enlazada recursiva:")
    lista_animales.imprimir_lista_recursiva(lista_animales.cabeza)
