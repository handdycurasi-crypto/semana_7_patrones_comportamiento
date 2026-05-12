# Semana 7 - Patrones de Comportamiento

## Curso
Lenguajes de Programación Orientada a Objetos II

## Estudiante
Handdy Ronald Curasi Zevallos

## Tema
Patrones de comportamiento: Observer, Strategy y Command.

## Descripción
Este repositorio contiene la implementación de tres patrones de comportamiento trabajados en la Semana 7.

Los patrones desarrollados son:

- Observer en Python
- Strategy en C++
- Command en Python

## Archivos

### 1. observer_chat.py
Implementa el patrón Observer.

El programa crea un sistema de chat donde varios usuarios reciben una notificación cuando se envía un mensaje.

Ejecución:

```bash
python observer_chat.py
```

Resultado esperado:

```text
Handdy recibio una notificacion: Nuevo mensaje en el grupo de POO2
Carlos recibio una notificacion: Nuevo mensaje en el grupo de POO2
Lucia recibio una notificacion: Nuevo mensaje en el grupo de POO2
```

### 2. strategy_ordenamiento.cpp
Implementa el patrón Strategy.

El programa permite cambiar entre dos algoritmos de ordenamiento:

- Burbuja
- Ordenamiento rápido usando sort

Compilación:

```bash
g++ strategy_ordenamiento.cpp -o strategy
```

Ejecución:

```bash
./strategy
```

### 3. command_editor.py
Implementa el patrón Command.

El programa simula un editor de texto con comandos para escribir, guardar y deshacer.

Ejecución:

```bash
python command_editor.py
```

## Comparación breve

| Patrón | Función principal | Ejemplo desarrollado |
|---|---|---|
| Observer | Notifica cambios a varios objetos | Usuarios de un chat |
| Strategy | Permite cambiar algoritmos | Ordenamiento burbuja y rápido |
| Command | Convierte acciones en objetos | Editor de texto con guardar y deshacer |

## Conclusión
Los patrones de comportamiento ayudan a organizar la comunicación y las acciones entre objetos. Observer permite notificar cambios, Strategy permite cambiar algoritmos y Command permite manejar operaciones como objetos independientes.
