import random
from random import randint
import json

u=100
numeros_aleatorios=[randint(1,100)for _ in range(u)]
guardoNumeros=numeros_aleatorios

with open('File_100.txt','w') as archivo:
    archivo.write(json.dumps(guardoNumeros))
archivo.close()

print('\n')

u=500
numeros_aleatorios=[randint(1,100)for _ in range(u)]
guardoNumeros=numeros_aleatorios

with open('File_500.txt','w') as archivo:
    archivo.write(json.dumps(guardoNumeros))
archivo.close()

print('\n')

u=1000
while u<10000:
    if u>=1000 and u<10000:
        numeros_aleatorios=[randint(1,100) for _ in range(u)]
        files="File_"
        numeroFile=str(u)
        extension=".txt"
        nombre=files+numeroFile+extension
        with open(nombre,'w') as archivo:
            archivo.write(json.dumps(numeros_aleatorios))
        archivo.close()
        numeros_aleatorios=[]
    u=u+1000

while u<=100000:
    if u>=10000 and u<=100000:
        numeros_aleatorios=[randint(1,100)for _ in range(u)]
        files="File_"
        numeroFile=str(u)
        extension=".txt"
        nombre=files+numeroFile+extension
        with open(nombre,'w') as archivo:
            archivo.write(json.dumps(numeros_aleatorios))
        archivo.close()
        numero_aleatorios=[]
    u=u+10000