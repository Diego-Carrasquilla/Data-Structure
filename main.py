# #EJEMPLO 1
# personas = []

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# dinero = int(input("Ingresa la cantidad de dinero que tienes: "))

# personas.append({"nombre": nombre, "edad": edad, "dinero": dinero})

# for persona in personas:
#     if persona["edad"] < 18 or persona["dinero"] < 50000:
#         print(f"{persona['nombre']} no puede pasar.")
#     else:
#         print(f"{persona['nombre']} puede pasar.")



#EJEMPLO 2
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


num_salones = 5
num_horas = 24  


salones = [f"Salon {i+1}" for i in range(num_salones)]



hora_inicial = datetime(2025, 2, 8, 0, 0)


data = []

for hora in range(num_horas):
    hora_actual = hora_inicial.replace(hour=hora_inicial.hour + hora)
    
    for salon in salones:
        temperatura = round(random.uniform(18, 30), 2)
        
        data.append([hora_actual, salon, temperatura])


df = pd.DataFrame(data, columns=["Hora", "Salon", "Temperatura"])

print(df)

promedio_temperatura = df.groupby('Salon')['Temperatura'].mean()

print(promedio_temperatura)
