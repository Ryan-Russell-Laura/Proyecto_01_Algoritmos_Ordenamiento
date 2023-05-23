import numpy as np
import matplotlib.pyplot as plt

xFiles=[100,500]

for u in range(1000,10000,1000):
    xFiles.append(u)
for u in range(10000,110000,10000):
    xFiles.append(u)

with open("Tiempos_Bubble_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposBubbleSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposBubbleSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Counting_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposCountingSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposCountingSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Heap_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposHeapSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposHeapSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Insertion_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposInsertionSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposInsertionSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Merge_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposMergeSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposMergeSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Quick_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposQuickSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposQuickSort.append(float(dato))    
tiemposFile.close()

with open("Tiempos_Selection_Sort_C++.txt","r") as tiemposFile:
  info=tiemposFile.readlines() #Leemos todas las lineas y lo guardamos en info
          
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(",")   
  
  lista.pop()#Eliminamos el ultimo elemento de la lista porque es una coma sola
  #Convertiremos cada dato de tipo str a tipo float  
  yTiemposSelectionSort=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista yTiempos
    yTiemposSelectionSort.append(float(dato))    
tiemposFile.close()

plt.figure(figsize=(10,5))
plt.plot(yTiemposBubbleSort,label="BubbleSort")
plt.plot(yTiemposCountingSort,label="CountingSort")
plt.plot(yTiemposHeapSort,label="HeapSort")
plt.plot(yTiemposInsertionSort,label="InsertionSort")
plt.plot(yTiemposMergeSort,label="MergeSort")
plt.plot(yTiemposQuickSort,label="QuickSort")
plt.plot(yTiemposSelectionSort,label="SelectionSort")

plt.title("Comparación de los algoritmos de ordenamiento implementados en C++")
plt.xlabel("Tamaño de archivos de datos")
plt.xticks(range(len(xFiles)),xFiles,rotation=45)
plt.ylabel("Tiempo de ejecución en segundos")
plt.legend()
plt.show()