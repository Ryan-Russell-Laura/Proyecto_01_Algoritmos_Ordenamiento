#include<iostream>
#include<string>
#include<cstdlib>
#include<vector>
#include<chrono>
#include<stdio.h>
#include<bits/stdc++.h>
#include<fstream>

using namespace std;

// Funci�n para intercambiar dos elementos en un vector
void swap(int& a, int& b){
    int aux = a;
    a = b;
    b = aux;
}

// Funci�n para dividir el arreglo y colocar el pivote en la posici�n correcta
int particion(vector<int>& numeros_aleatorios, int primero, int ultimo){
    int pivot=numeros_aleatorios[ultimo];  // Elegir el �ltimo elemento como pivote
    int i=primero-1;  // �ndice del elemento m�s peque�o

    for(int j=primero;j<=ultimo-1;++j){
        // Si el elemento actual es m�s peque�o o igual que el pivote
        if(numeros_aleatorios[j]<=pivot){
            i++;  // Incrementar el �ndice del elemento m�s peque�o
            swap(numeros_aleatorios[i],numeros_aleatorios[j]);  // Intercambiar los elementos
        }
    }

    swap(numeros_aleatorios[i+1],numeros_aleatorios[ultimo]);  // Colocar el pivote en la posici�n correcta
    return(i+1);
}

// Funci�n principal de Quick Sort
void quickSort(vector<int>& numeros_aleatorios,int primero,int ultimo){
    if (primero<ultimo) {
        // Obtener el �ndice del pivote despu�s de dividir y colocarlo en la posici�n correcta
        int pivotIndice = particion(numeros_aleatorios, primero, ultimo);

        // Ordenar recursivamente los elementos antes y despu�s del pivote
        //Primero: hacer el proceso con los datos a la izquierda del pivote
        quickSort(numeros_aleatorios, primero, pivotIndice-1);
		//hacer el proceso con los datos a la derecha del pivote 
        quickSort(numeros_aleatorios, pivotIndice+1, ultimo);
    }
}

int main(){
    //Creamos un vector que tenga los tamanios de cada archivo de texto   
    vector<int>tamanos={100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    //Con ofstream creamos un archivo de texto para guardar los tiempos del algoritmo
	ofstream archivo_tiempo("Tiempos_Quick_Sort_C++.txt");
    for (int tamano:tamanos){
		//Con ifstream y ayuda del bucle for leemos cada uno de los archivos
		//seg�n su tamanio    	  
        ifstream archivo("File_"+to_string(tamano)+".txt");    	
		//Creamos un vector para guardar los numeros aleatorios por leer
		vector<int>numeros_aleatorios;
        //Creamos nuevos archivos de texto para guardar los datos aleatorios de valor num�rico
		ofstream archivoEdit("File_Edit_"+to_string(tamano)+".txt");
        //Creamos variables que equivalen a los �nicos caracteres
		//que no son valores num�ricos en nuestros archivos de datos aleatorios
		char caracter;
        char paren1='[';
        char paren2=']';
        char coma=',';
        //El siguiente algoritmo nos permitir� discriminar los corchetes y comas
        //sustituy�ndolos por saltos de lineas en caso de las comas
        //y espacios en caso de los corchetes
       	while(archivo.get(caracter)){
        	if(caracter==paren1 or caracter==paren2){
        		archivoEdit<<' ';
			}else{
				if(caracter==coma){
					archivoEdit<<"\n";
				}else{
					//si el caracter no es coma ni corchete se
					//escribir� en el nuevo archivo de texto creado
					archivoEdit<<caracter;
				}
			}
		}
		archivoEdit.close();
		archivo.close();
		int numero;
		//Leemos los datos num�ricos guardados en nuestros nuevos archivos de texto
		ifstream archivoNuevo("File_Edit_"+to_string(tamano)+".txt");
    	while(archivoNuevo>>numero){
    		//Ingresamos los datos num�ricos en el vector denominado numeros_aleatorios
    		numeros_aleatorios.push_back(numero);
		}		
		archivoNuevo.close();		

		double tiempo_process;
		clock_t tiempo_inicio,tiempo_final;
		//Medici�n de tiempo del algoritmo
		tiempo_inicio=clock();
		//invocamos al algoritmo de ordenamiento
        quickSort(numeros_aleatorios,0,numeros_aleatorios.size()-1);
		tiempo_final=clock();
		//c�lculo del tiempo de procesamiento
		tiempo_process=(double)(tiempo_final-tiempo_inicio)/CLOCKS_PER_SEC;
		
		cout<<"-> File_"+to_string(tamano)+".txt -> "<<"El tiempo de procesamiento fue de:"<<tiempo_process<<"\n";
        //escribir el tiempo de procesamiento en un fichero
        archivo_tiempo<<to_string(tiempo_process)+",";		
        
		ofstream archivo_ord("Ordenamiento_File_"+to_string(tamano)+".txt");
        //escribimos el vector numeros_aleatorios con n�meros ordenados en un archivo
		for (int num : numeros_aleatorios){
            archivo_ord<<to_string(num)+",";
        }
        archivo_ord.close();
		cout<<endl;	      
	}
    archivo_tiempo.close();
  return 0;
}
