# Insertion Sort in Python
from timeit import default_timer
import json
#Funcion de algoritmo insertion sort
def insertionSort(numeros):
    # Iterar a través de 1 hasta len(numeros)
    for i in range(1,len(numeros)):
        key=numeros[i]  # Elemento actual a ser comparado e insertado en su posición correcta
        j=i-1     # Índice del elemento anterior al actual
        
        # Mover los elementos del arreglo que son mayores que key, a una posición adelante
        while j>=0 and numeros[j]>key:
            numeros[j+1]=numeros[j]
            j-=1        
        numeros[j+1]=key  # Insertar el elemento actual en su posición correcta

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
insertionSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_100.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numeros))
fileOrdenamiento.close()

print(f"\n-> File_100.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo=[]
vectorTiempo.append(processTime)
with open("Tiempos_Insertion_Sort_Python.txt","w") as fileTimes:
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
    ##print(lista)

  #Convertiremos cada dato de tipo str a tipo int  
  numeros=[]
  for dato in lista:
    #Insertamos los datos numericos en una lista
    numeros.append(int(dato))
archivo.close()

#Calculando tiempo de procesamiento del archivo con 500 datos
startTime=default_timer()
#ordenamiento de datos
insertionSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_500.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numeros))
fileOrdenamiento.close()

print(f"\n-> File_500.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo.append(processTime)
with open("Tiempos_Insertion_Sort_Python.txt","w") as fileTimes:
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
    insertionSort(numeros)
    processTime=default_timer()-startTime

    with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numeros))
    fileOrdenamiento.close()

    print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
    
    vectorTiempo.append(processTime)
    with open("Tiempos_Insertion_Sort_Python.txt","w") as fileTimes:
      fileTimes.write(json.dumps(vectorTiempo))
    fileTimes.close()
  u=u+1000

while u<=100000:
    if u>=10000 and u<=100000:
      numeros=leerFiles(u)
      #Calculando tiempo de procesamiento de los archivos
      startTime=default_timer()
      #ordenamiento de datos
      insertionSort(numeros)
      processTime=default_timer()-startTime

      with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numeros))
      fileOrdenamiento.close()

      print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}\n")
     
      vectorTiempo.append(processTime)
      with open("Tiempos_Insertion_Sort_Python.txt","w") as fileTimes:
        fileTimes.write(json.dumps(vectorTiempo))
      fileTimes.close()
    u=u+10000


