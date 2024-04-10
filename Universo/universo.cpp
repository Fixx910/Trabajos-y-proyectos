#include <iostream>
#include <string>
#include <fstream>
#include <chrono>
#include <algorithm>
#include <ctime>
#include <vector>

using namespace std;

// Declaración anticipada de la función auxiliar
vector<string> generarCombinacionesAux(string prefix, int m);

// Función para generar todas las combinaciones de palabras de longitud hasta n
vector<string> generarCombinaciones(int n) {
    vector<string> combinaciones;
    for (int i = 0; i <= n; ++i) {
        vector<string> subCombinaciones = generarCombinacionesAux("", i);
        combinaciones.insert(combinaciones.end(), subCombinaciones.begin(), subCombinaciones.end());
        cout << "Se ha ingresado al txt E^" << i << "'" << endl; // Mensaje al completar E^i
    }
    return combinaciones;
}

// Función auxiliar para generar las combinaciones de palabras de longitud m
vector<string> generarCombinacionesAux(string prefix, int m) {
    vector<string> combinaciones;
    if (m == 0) {
        combinaciones.push_back(prefix);
    } else {
        combinaciones = generarCombinacionesAux(prefix + "a", m - 1);
        vector<string> subCombinaciones = generarCombinacionesAux(prefix + "b", m - 1);
        combinaciones.insert(combinaciones.end(), subCombinaciones.begin(), subCombinaciones.end());
    }
    return combinaciones;
}

int main() {
    int opcion;
    cout << "Seleccione una opción:" << endl;
    cout << "1. Usar de forma automática (genera un número aleatorio de 0 a 1000)" << endl;
    cout << "2. Usar de forma manual (el usuario ingresa el número)" << endl;
    cin >> opcion;

    int n;
    if (opcion == 1) {
        // Generar un número aleatorio entre 0 y 1000 para la opción automática
        srand(time(0));
        n = rand() % 10;
        cout << "Número aleatorio generado: " << n << endl;
    } else if (opcion == 2) {
        // Pedir al usuario que ingrese el número para la opción manual
        cout << "Ingrese n (n): ";
        cin >> n;
    } else {
        cout << "Opción no válida. Saliendo del programa." << endl;
        return 1;
    }

    // Formar el nombre del archivo
    string nombreArchivo;
    nombreArchivo = "Universo.txt";
    

    // Generar todas las combinaciones de palabras de longitud hasta n
    vector<string> combinaciones = generarCombinaciones(n);

    // Abrir el archivo para escritura
    ofstream archivo(nombreArchivo, ios::out | ios::trunc);

    // Escribir las combinaciones en el archivo
    archivo << "E^" << n << "={ε";
    for (size_t i = 1; i < combinaciones.size(); ++i) {
        archivo << "," << combinaciones[i];
    }
    archivo << "}\n";

    // Mostrar mensaje de finalización
    cout << "Se ha creado el archivo con el nombre: " << nombreArchivo << endl;

    // Cerrar el archivo
    archivo.close();

    return 0;
}
