from datetime import datetime

class NodoTarea:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
    
    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class ListaTareas:
    def __init__(self):
        self.cabeza = None
    
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = NodoTarea(Tarea(descripcion, prioridad, fecha_vencimiento))
        if not self.cabeza or (self.cabeza.tarea.prioridad > prioridad or (self.cabeza.tarea.prioridad == prioridad and self.cabeza.tarea.fecha_vencimiento > nueva_tarea.tarea.fecha_vencimiento)):
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
        else:
            temp = self.cabeza
            while temp.siguiente and (temp.siguiente.tarea.prioridad < prioridad or (temp.siguiente.tarea.prioridad == prioridad and temp.siguiente.tarea.fecha_vencimiento <= nueva_tarea.tarea.fecha_vencimiento)):
                temp = temp.siguiente
            nueva_tarea.siguiente = temp.siguiente
            temp.siguiente = nueva_tarea
    
    def eliminar_tarea(self, descripcion=None, posicion=None):
        if not self.cabeza:
            return False
        
        if descripcion:
            if self.cabeza.tarea.descripcion == descripcion:
                self.cabeza = self.cabeza.siguiente
                return True
            temp = self.cabeza
            while temp.siguiente and temp.siguiente.tarea.descripcion != descripcion:
                temp = temp.siguiente
            if temp.siguiente:
                temp.siguiente = temp.siguiente.siguiente
                return True
        
        elif posicion is not None:
            if posicion == 0:
                self.cabeza = self.cabeza.siguiente
                return True
            temp = self.cabeza
            count = 0
            while temp.siguiente and count < posicion - 1:
                temp = temp.siguiente
                count += 1
            if temp.siguiente:
                temp.siguiente = temp.siguiente.siguiente
                return True
        return False
    
    def imprimir_tareas(self):
        temp = self.cabeza
        while temp:
            print(temp.tarea)
            temp = temp.siguiente
    
    def buscar_tarea(self, descripcion):
        temp = self.cabeza
        while temp:
            if temp.tarea.descripcion == descripcion:
                return temp.tarea
            temp = temp.siguiente
        return None
    
    def marcar_completada(self, descripcion):
        return self.eliminar_tarea(descripcion=descripcion)

# Ejemplo de uso
if __name__ == "__main__":
    lista_tareas = ListaTareas()
    lista_tareas.agregar_tarea("Comprar leche", 1, "2025-03-10")
    lista_tareas.agregar_tarea("Llamar al médico", 2, "2025-03-12")
    lista_tareas.agregar_tarea("Pagar facturas", 1, "2025-03-15")
    lista_tareas.agregar_tarea("Hacer ejercicio", 3, "2025-03-11")
    
    print("Lista de tareas ordenadas:")
    lista_tareas.imprimir_tareas()
    
    print("\nEliminando 'Llamar al médico'...")
    lista_tareas.eliminar_tarea(descripcion="Llamar al médico")
    lista_tareas.imprimir_tareas()
    
    print("\nBuscando 'Pagar facturas'...")
    tarea_encontrada = lista_tareas.buscar_tarea("Pagar facturas")
    print(tarea_encontrada if tarea_encontrada else "No encontrada")
    
    print("\nMarcando 'Comprar leche' como completada...")
    lista_tareas.marcar_completada("Comprar leche")
    lista_tareas.imprimir_tareas()
