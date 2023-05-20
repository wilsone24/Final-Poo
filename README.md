# **Parcial Final  POO Wilson Estrada**
Nombre: Wilson Manuel Estrada Ortega

Codigo: 200098310
## **Resumen**
Se Requiere diseñar un sistema para La empresa de manejo de residuos “TrashCity” para administrar su operación. El primer servicio de la empresa consiste en la recolección de los residuos de la ciudad: camiones de la empresa recorren la ciudad en rutas preestablecidas tomando los residuos dispuestos por los usuarios. Una ruta contiene la serie de puntos geográficos (latitud, longitud) por donde debe pasar es camión. Cada camión cuenta con un conductor y dos asistentes de recolección en un turno. Un turno define el recorrido completo de un camión y su equipo a recoger residuos, en un rango de día y hora de inicio y finalización, siguiendo una de las rutas existentes. En el turno se almacena la localización geográfica y tiempo en el que pasó en su recorrido.Al final de turno, la carga del camión pasa a ser clasificada en un centro de acopio. El resultado de la separación se almacena en el sistema asociado al turno: cuántas toneladas de vidrio, papel, plástico, metal y residuos orgánicos. De los elementos camión y persona se almacena información básica de identificación. 


## **Funcionalidad**
Se implementó en Python los métodos que permitan el cálculo de la cantidad de vidrio (Principalmente) y los distintos materiales que se recogió en todas las rutas de un día en específico. Se aplicaron conceptos de **Herencia, Polimorfismo, Encapsulación, Decoradores, Metodos Get y set, Patron de diseño observer, Patron de diseño Singleton y Unit Test.**

## **UML**

![](https://github.com/wilsone24/Final-Poo/blob/main/UML.png)

## **Instrucciones**
1. Ingresar en el enlace del repositorio de Github: https://github.com/wilsone24/Final-Poo

2. Seleccionar la parte de code y copiar el HTTPS: https://github.com/wilsone24/Final-Poo.git

3. Ingresar a VsCode o desde gitBash y clonar el repositorio: git clone https://github.com/wilsone24/Final-Poo.git

### **Ejecutar App**

Una vez Clonado el repositorio se encontrará con 3 carpetas y 3 archivos, de los cuales para iniciar el proyecto unicamente abrira el **main.py** y lo ejecutará.

Así mismo si quiere verificar el codigo, clases, funcionalidades, entre otros aspectos, la clasificacion de las carpetas es la siguiente:

1. **Entidades:** Contiene las clases en los distintos archivos que pueden ser un ente como lo son: Camiones, Empleados, Observador y empresa. Sus respectivos archivos son Camiones.py, Empleados.py, Empresa.py y Observer.py, estos contendran todo el codigo, clases y funciones.

2. **Funcionalidades:** Contiene las clases en los distintos archivos que pueden ser Funcionalidades del programa  y con lo que se puede interactuar como lo son: Puntos Geograficos, Recolección, Turnos y La funcion principal. Sus respectivos archivos son PuntoGeografico.py, Recoleccion.py, Turnos.py y Funciones.py, estos contendran todo el codigo, clases y funciones.

2. **RecursosTests:** Contiene Recursos necesarios para el correcto funcionamiento de las pruebas unitarias

### **Verificar Pruebas Unitarias**
Para Verificar las distintas pruebas unitarias que se le hicieron a las funciones unicamente se dirigirá al archivo **TestRecolección.py** y lo ejecuta.

* El resultado de la prueba unitaria será mostrado en consola.
