# Heap Sort in Python
from timeit import default_timer
import json 

def swap(lista,i,j):
    lista[i],lista[j]=lista[j],lista[i]
def heapify(lista,i,upperFather):
    while(True):
        ##Calculamos el indice del hijo izquierdo y derecho
        left,right=i*2+1,i*2+2
        #Si el hijo izquierdo o derecho es menor que el padre maximo
        if max(left,right)<upperFather:
            ##Si el nodo raiz es mayor que el hijo izquierdo y derecho no hacer nada
            if lista[i]>=max(lista[left],lista[right]): break
            elif lista[left]>lista[right]:##Si el hijo izquierdo es mayor que el derecho
                #se intercambian y el izquierdo ahora es el padre
                swap(lista,i,left)
                i=left
            else:
                #se intercambian y el derecho ahora es el padre
                swap(lista,i,right)
                i=right
        elif left<upperFather:##Si el izquierdo es menor que el valor del padre maximo
            if lista[left]>lista[i]:##Si el nodo hijo izquierdo es mayor que el padre menor
                ##Se intercambia el padre menor con el hijo izquierdo
                swap(lista,i,left)
                i=left
            else: break
        elif right<upperFather:##Si el derecho es menor que el valor del padre maximo
            if lista[right]>lista[i]:##Si el nodo hijo derecho es mayor que el padre menor
                ##se intercambia el padre menor con el hijo derecho
                swap(lista,i,right)
                i=right
            else: break
        else: break
    
def heapsort(lista):
    ##Se crea el primer monticulo
    for j in range((len(lista)-2)//2,-1,-1):
        heapify(lista,j,len(lista))        
    #Se crean mas monticulos haciendo intercambios entre el ultimo nodo y el primer nodo
    for end in range(len(lista)-1,0,-1):
        swap(lista,0,end)
        heapify(lista,0,end)

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
heapsort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_100.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numeros))
fileOrdenamiento.close()

print(f"\n-> File_100.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo=[]
vectorTiempo.append(processTime)
with open("Tiempos_Heap_Sort_Python.txt","w") as fileTimes:
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
heapsort(numeros)
processTime=default_timer()-startTime

with open("Ordenamiento_File_500.txt","w") as fileOrdenamiento:  
  fileOrdenamiento.write(json.dumps(numeros))
fileOrdenamiento.close()

print(f"\n-> File_500.txt -> El tiempo de procesamiento fue de: {processTime}")

vectorTiempo.append(processTime)
with open("Tiempos_Heap_Sort_Python.txt","w") as fileTimes:
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
          ##print(lista)

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
    heapsort(numeros)
    processTime=default_timer()-startTime

    with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numeros))
    fileOrdenamiento.close()

    print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}")
    vectorTiempo.append(processTime)
    with open("Tiempos_Heap_Sort_Python.txt","w") as fileTimes:
      fileTimes.write(json.dumps(vectorTiempo))
    fileTimes.close()
  u=u+1000

while u<=100000:
  if u>=10000 and u<=100000:
    numeros=leerFiles(u)
    #Calculando tiempo de procesamiento de los archivos
    startTime=default_timer()
    #ordenamiento de datos
    heapsort(numeros)
    processTime=default_timer()-startTime

    with open("Ordenamiento_File_"+str(u)+".txt","w") as fileOrdenamiento:  
        fileOrdenamiento.write(json.dumps(numeros))
    fileOrdenamiento.close()

    print("\n-> File_"+str(u)+f".txt -> El tiempo de procesamiento fue de: {processTime}\n")
    vectorTiempo.append(processTime)
    with open("Tiempos_Heap_Sort_Python.txt","w") as fileTimes:
      fileTimes.write(json.dumps(vectorTiempo))
    fileTimes.close()
  u=u+10000