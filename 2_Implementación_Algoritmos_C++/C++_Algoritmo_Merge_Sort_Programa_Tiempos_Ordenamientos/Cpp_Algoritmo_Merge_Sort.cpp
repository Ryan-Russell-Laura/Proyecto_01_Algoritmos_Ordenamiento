#include<iostream>
#include<string>
#include<cstdlib>
#include<vector>
#include<chrono>
#include<stdio.h>
#include<bits/stdc++.h>
#include<fstream>

using namespace std;

void merge(vector<int>& numeros_aleatorios,int izq,int mid,int dere){
    int n1=mid-izq+1;
    int n2=dere-mid;

    // Crear arreglos temporales para almacenar los elementos divididos
    vector<int> izqArr(n1);
    vector<int> dereArr(n2);

    // Copiar los elementos a los arreglos temporales
    for(int i=0;i<n1;i++){
        izqArr[i]=numeros_aleatorios[izq+i];
    }
    for(int j=0;j<n2;j++){
        dereArr[j]=numeros_aleatorios[mid+1+j];
    }

    // Combinar los elementos en orden ascendente
    int i = 0;
    int j = 0;
    int k = izq;

    while(i<n1&&j<n2){
        if(izqArr[i] <= dereArr[j]){
            numeros_aleatorios[k] = izqArr[i];
            i++;
        }else{
            numeros_aleatorios[k] = dereArr[j];
            j++;
        }
        k++;
    }

    // Copiar los elementos restantes de izqArr, si los hay
    while(i<n1){
        numeros_aleatorios[k]=izqArr[i];
        i++;
        k++;
    }

    // Copiar los elementos restantes de dereArr, si los hay
    while (j<n2){
        numeros_aleatorios[k]=dereArr[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& numeros_aleatorios, int izq, int dere){
    if (izq<dere){
        int mid=izq+(dere-izq)/2;

        // Dividir el arreglo en dos mitades
        mergeSort(numeros_aleatorios,izq,mid);
        mergeSort(numeros_aleatorios,mid+1,dere);

        // Combinar las dos mitades ordenadas
        merge(numeros_aleatorios,izq,mid,dere);
    }
}

int main(){
    //Creamos un vector que tenga los tamanios de cada archivo de texto    
    vector<int>tamanos={100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
    //Con ofstream creamos un archivo de texto para guardar los tiempos del algoritmo
	ofstream archivo_tiempo("Tiempos_Merge_Sort_C++.txt");
    for (int tamano:tamanos){
	    //Con ifstream y ayuda del bucle for leemos cada uno de los archivos
		//según su tamanio    	  
        ifstream archivo("File_"+to_string(tamano)+".txt");    	
		//Creamos un vector para guardar los numeros aleatorios por leer
		vector<int>numeros_aleatorios;
        //Creamos nuevos archivos de texto para guardar los datos aleatorios de valor numérico
		ofstream archivoEdit("File_Edit_"+to_string(tamano)+".txt");
        //Creamos variables que equivalen a los únicos caracteres
		//que no son valores numéricos en nuestros archivos de datos aleatorios
		char caracter;
        char paren1='[';
        char paren2=']';
        char coma=',';
        //El siguiente algoritmo nos permitirá discriminar los corchetes y comas
        //sustituyéndolos por saltos de lineas en caso de las comas
        //y espacios en caso de los corchetes
       	while(archivo.get(caracter)){
        	if(caracter==paren1 or caracter==paren2){
        		archivoEdit<<' ';
			}else{
				if(caracter==coma){
					archivoEdit<<"\n";
				}else{
					//si el caracter no es coma ni corchete se
					//escribirá en el nuevo archivo de texto creado
					archivoEdit<<caracter;
				}
			}
		}
		archivoEdit.close();
		archivo.close();
		int numero;
		//Leemos los datos numéricos guardados en nuestros nuevos archivos de texto
		ifstream archivoNuevo("File_Edit_"+to_string(tamano)+".txt");
    	while(archivoNuevo>>numero){
    		//Ingresamos los datos numéricos en el vector denominado numeros_aleatorios
    		numeros_aleatorios.push_back(numero);
		}		
		archivoNuevo.close();

		double tiempo_process;
		clock_t tiempo_inicio,tiempo_final;
		//Medición de tiempo del algoritmo
		tiempo_inicio=clock();
        mergeSort(numeros_aleatorios,0,numeros_aleatorios.size()-1);
		tiempo_final=clock();
		//cálculo del tiempo de procesamiento
		tiempo_process=(double)(tiempo_final-tiempo_inicio)/CLOCKS_PER_SEC;
		
		cout<<"-> File_"+to_string(tamano)+".txt -> "<<"El tiempo de procesamiento fue de:"<<tiempo_process<<"\n";
        //escribir el tiempo de procesamiento en un fichero
        archivo_tiempo<<to_string(tiempo_process)+",";		
        
		ofstream archivo_ord("Ordenamiento_File_"+to_string(tamano)+".txt");
        //escribimos el vector numeros_aleatorios con numeros ordenados en un archivo
		for (int num : numeros_aleatorios){
            archivo_ord<<to_string(num)+",";
        }
        archivo_ord.close();
		cout<<endl;	      
	}
    archivo_tiempo.close();
  return 0;
}
