# Counting Sort in Python
from timeit import default_timer
import json
#Funcion de algoritmo counting sort
def countingSort(numeros):
    # Encuentra el maximo elemento en el arreglo numeros
    maxElemento=max(numeros)

    countArrayTamanio=maxElemento+1

    # Inicializa un arreglo de conteo con (max+1) ceros
    countArray=[0]*countArrayTamanio

    # Paso 1 -> lee el arreglo de numeros y los cuenta
    for el in numeros: 
        countArray[el]+=1

    # Paso 2 -> Por cada elemento del arreglo de conteo, 
    # suma el valor actual con el valor previo y lo guarda como valor del elemento actual
    for i in range(1,countArrayTamanio):
        countArray[i]+=countArray[i-1] 

    # Paso 3 -> Calcula la posicion del elemento
    # basado en las posiciones del arreglo de conteo
    numerosOrdenados=[0]*len(numeros)
    i=len(numeros)-1
    while i >= 0:
        elementoActual=numeros[i]
        countArray[elementoActual]-=1
        nuevaPosicion=countArray[elementoActual]
        numerosOrdenados[nuevaPosicion]=elementoActual
        i-=1
    return numerosOrdenados

# ARCHIVO 100 DATOS       
#Convirtiento cadenas de datos a un arreglo de numeros enteros
with open("File_100.txt","r") as archivo:
  archivo.read(1)
  info=archivo.readlines()
    
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(", ")

  #Convertiremos cada dato de tipo str a tipo int  
  numeros=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista
    numeros.append(int(dato))
archivo.close()

#Calculando tiempo de procesamiento del archivo con 100 datos
startTime=default_timer()
#ordenamiento de datos
numerosOrdenados=countingSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_100.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numerosOrdenados))
fileOrdenamiento.close()

print(f"\n-> File_100.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo=[]
vectorTiempo.append(processTime)
with open("Tiempos_Counting_Sort_Python.txt","w") as fileTimes:
   fileTimes.write(json.dumps(vectorTiempo))
fileTimes.close()

# ARCHIVO 500 DATOS
# Convirtiento cadenas de datos a un arreglo de numeros enteros
with open('File_500.txt','r') as archivo:
  archivo.read(1)
  info=archivo.readlines()
    
  #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
  for dato in info:
    #guardamos el resultado en una variable denominada lista   
    lista=dato.strip("]").split(", ")

  #Convertiremos cada dato de tipo str a tipo int  
  numeros=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista
    numeros.append(int(dato))
archivo.close()

#Calculando tiempo de procesamiento del archivo con 500 datos
startTime=default_timer()
#ordenamiento de datos
numerosOrdenados=countingSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_500.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numerosOrdenados))
fileOrdenamiento.close()

print(f"\n-> File_500.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo.append(processTime)
with open("Tiempos_Counting_Sort_Python.txt","w") as fileTimes:
   fileTimes.write(json.dumps(vectorTiempo))
fileTimes.close()

#####################################################

def leerFiles(u):
  if u>=1000 and u<10000:
    with open("File_"+str(u)+".txt","r") as archivo:
      archivo.read(1)
      info=archivo.readlines()
        
      #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
      for dato in info:
        #guardamos el resultado en una variable denominada lista   
        lista=dato.strip("]").split(", ")    

      #Convertiremos cada dato de tipo str a tipo int  
      numeros=[]
      for dato in lista:
        #Insertamos los datos numericos en una lista
        numeros.append(int(dato))    
    archivo.close()
  elif u>=10000 and u<=100000:
      with open("File_"+str(u)+".txt","r") as archivo:
        archivo.read(1)
        info=archivo.readlines()
          
        #Separamos los datos de las comas con split y eliminamos el corchete cerrado con strip
        for dato in info:
          #guardamos el resultado en una variable denominada lista   
          lista=dato.strip("]").split(", ")     

        #Convertiremos cada dato de tipo str a tipo int  
        numeros=[]
        for dato in lista:
          #Insertamos los datos numericos en una lista
          numeros.append(int(dato))    
      archivo.close()
  return numeros

u=1000
while u<10000:
  if u>=1000 and u<10000:
    numeros=leerFiles(u)
    #Calculando tiempo de procesamiento de los archivos
    startTime=default_timer()
    #ordenamiento de datos
    numerosOrdenados=countingSort(numeros)
    processTime=default_timer()-startTime

    with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numerosOrdenados))
    fileOrdenamiento.close()

    print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
    
    vectorTiempo.append(processTime)
    with open("Tiempos_Counting_Sort_Python.txt","w") as fileTimes:
      fileTimes.write(json.dumps(vectorTiempo))
    fileTimes.close()
  u=u+1000

while u<=100000:
    if u>=10000 and u<=100000:
      numeros=leerFiles(u)
      #Calculando tiempo de procesamiento de los archivos
      startTime=default_timer()
      #ordenamiento de datos
      numerosOrdenados=countingSort(numeros)
      processTime=default_timer()-startTime

      with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numerosOrdenados))
      fileOrdenamiento.close()

      print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
     
      vectorTiempo.append(processTime)
      with open("Tiempos_Counting_Sort_Python.txt","w") as fileTimes:
        fileTimes.write(json.dumps(vectorTiempo))
      fileTimes.close()
    u=u+10000
