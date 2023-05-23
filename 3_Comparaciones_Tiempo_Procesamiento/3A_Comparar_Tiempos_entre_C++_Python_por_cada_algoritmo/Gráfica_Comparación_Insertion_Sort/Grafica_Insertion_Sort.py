import numpy as np
import matplotlib.pyplot as plt

xFiles=[100,500]

for u in range(1000,10000,1000):
    xFiles.append(u)
for u in range(10000,110000,10000):
    xFiles.append(u)

with open("Tiempos_Insertion_Sort_Python.txt","r") as tiemposFile:
  tiemposFile.read(1) #Leemos el primer caracter y no hacemos nada con el
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(", ")     

  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposPython=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposPython.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Insertion_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposCpp=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposCpp.append(float(dato))    
tiemposFile.close()

plt.figure(figsize=(10,6))
plt.plot(yTiemposPython,label="Python")
plt.plot(yTiemposCpp,label="C++")

plt.title("Tiempo de ejecución de Insertion Sort en Python y C++")
plt.xlabel("Tamaño de archivos de datos")
plt.xticks(range(len(xFiles)),xFiles,rotation=45)
plt.ylabel("Tiempo de ejecución en segundos")
plt.legend()
plt.show()