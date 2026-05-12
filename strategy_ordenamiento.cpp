#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class EstrategiaOrdenamiento {
public:
    virtual void ordenar(vector<int>& datos) = 0;
    virtual ~EstrategiaOrdenamiento() {}
};

class OrdenamientoBurbuja : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        for (int i = 0; i < datos.size() - 1; i++) {
            for (int j = 0; j < datos.size() - i - 1; j++) {
                if (datos[j] > datos[j + 1]) {
                    swap(datos[j], datos[j + 1]);
                }
            }
        }
    }
};

class OrdenamientoRapido : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        sort(datos.begin(), datos.end());
    }
};

class ContextoOrdenamiento {
private:
    EstrategiaOrdenamiento* estrategia;

public:
    ContextoOrdenamiento(EstrategiaOrdenamiento* estrategiaInicial) {
        estrategia = estrategiaInicial;
    }

    void cambiarEstrategia(EstrategiaOrdenamiento* nuevaEstrategia) {
        estrategia = nuevaEstrategia;
    }

    void ordenarDatos(vector<int>& datos) {
        estrategia->ordenar(datos);
    }
};

void mostrar(vector<int> datos) {
    for (int numero : datos) {
        cout << numero << " ";
    }

    cout << endl;
}

int main() {
    vector<int> datos1 = {5, 2, 9, 1, 3};
    vector<int> datos2 = {8, 4, 7, 6, 0};

    OrdenamientoBurbuja burbuja;
    OrdenamientoRapido rapido;

    ContextoOrdenamiento contexto(&burbuja);

    contexto.ordenarDatos(datos1);
    cout << "Ordenamiento burbuja: ";
    mostrar(datos1);

    contexto.cambiarEstrategia(&rapido);

    contexto.ordenarDatos(datos2);
    cout << "Ordenamiento rapido: ";
    mostrar(datos2);

    return 0;
}
