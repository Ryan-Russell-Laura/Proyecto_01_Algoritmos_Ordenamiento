# Merge Sort in Python
from timeit import default_timer
import json
#Funcion de algoritmo merge sort
def mergeSort(numeros):
    if len(numeros)<=1:
        return numeros    
    # Dividir el arreglo en mitades izquierda y derecha
    mitad=len(numeros)//2
    vectorIzq=numeros[:mitad]
    vectorDere=numeros[mitad:]    
    # Recursivamente aplicar merge_sort a las mitades izquierda y derecha
    vectorIzq=mergeSort(vectorIzq)
    vectorDere=mergeSort(vectorDere)    
    # Combinar las mitades ordenadas
    return merge(vectorIzq,vectorDere)

def merge(izq,dere):
    merged=[]
    indiceIzq=0
    indiceDere=0    
    # Comparar y combinar los elementos de las mitades izquierda y derecha
    while indiceIzq<len(izq) and indiceDere<len(dere):
        if izq[indiceIzq]<=dere[indiceDere]:
            merged.append(izq[indiceIzq])
            indiceIzq+=1
        else:
            merged.append(dere[indiceDere])
            indiceDere+=1
    # Agregar los elementos restantes de la mitad izquierda (si los hay)
    while indiceIzq<len(izq):
        merged.append(izq[indiceIzq])
        indiceIzq+=1
    # Agregar los elementos restantes de la mitad derecha (si los hay)
    while indiceDere<len(dere):
        merged.append(dere[indiceDere])
        indiceDere+=1 
    return merged

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
numerosOrdenados=mergeSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_100.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numerosOrdenados))
fileOrdenamiento.close()

print(f"\n-> File_100.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo=[]
vectorTiempo.append(processTime)
with open("Tiempos_Merge_Sort_Python.txt","w") as fileTimes:
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
numerosOrdenados=mergeSort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_500.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numerosOrdenados))
fileOrdenamiento.close()

print(f"\n-> File_500.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo.append(processTime)
with open("Tiempos_Merge_Sort_Python.txt","w") as fileTimes:
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
    numerosOrdenados=mergeSort(numeros)
    processTime=default_timer()-startTime

    with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numerosOrdenados))
    fileOrdenamiento.close()

    print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
    
    vectorTiempo.append(processTime)
    with open("Tiempos_Merge_Sort_Python.txt","w") as fileTimes:
      fileTimes.write(json.dumps(vectorTiempo))
    fileTimes.close()
  u=u+1000

while u<=100000:
    if u>=10000 and u<=100000:
      numeros=leerFiles(u)
      #Calculando tiempo de procesamiento de los archivos
      startTime=default_timer()
      #ordenamiento de datos
      numerosOrdenados=mergeSort(numeros)
      processTime=default_timer()-startTime

      with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numerosOrdenados))
      fileOrdenamiento.close()

      print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
     
      vectorTiempo.append(processTime)
      with open("Tiempos_Merge_Sort_Python.txt","w") as fileTimes:
        fileTimes.write(json.dumps(vectorTiempo))
      fileTimes.close()
    u=u+10000


