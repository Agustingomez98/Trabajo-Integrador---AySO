import os
import platform
import shutil


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_presentacion():
    print("""================================================
         UNIVERSIDAD TECNOLOGICA NACIONAL
================================================

       TECNICATURA EN PROGRAMACION

       ARQUITECTURA Y SISTEMAS OPERATIVOS

             TRABAJO INTEGRADOR

------------------------------------------------

               AySO VirtualLab

       VIRTUALIZACION CON VIRTUALBOX
                  Y LINUX

------------------------------------------------

INTEGRANTES:
- Villalba Aaron Exequiel
- Franco Agustin Gomez

------------------------------------------------
""")
    input("Presione ENTER para iniciar la presentacion...\n")


def consultar(funcion):
    try:
        return funcion() or "No disponible"
    except OSError:
        return "No disponible"


def memoria_total():
    try:
        with open("/proc/meminfo", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith("MemTotal:"):
                    return f"{int(linea.split()[1]) / 1024 / 1024:.2f} GiB"
    except (OSError, ValueError, IndexError):
        pass
    return "No disponible"


def capacidad_disco():
    try:
        return f"{shutil.disk_usage('/').total / 1024 ** 3:.2f} GiB"
    except OSError:
        return "No disponible"


def distribucion():
    try:
        with open("/etc/os-release", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith("PRETTY_NAME="):
                    valor = linea.split("=", 1)[1].strip()
                    if len(valor) >= 2 and valor[0] == valor[-1] and valor[0] in "\"'":
                        valor = valor[1:-1]
                    return valor or "No disponible"
    except (OSError, UnicodeError):
        pass
    return "No disponible"


def pausar():
    input("\nPresione ENTER para volver al menu principal...\n")


def mostrar_menu():
    print("""==================================================
          ARQUITECTURA Y SISTEMAS OPERATIVOS
==================================================
                 AySO VirtualLab

        VIRTUALIZACION CON VIRTUALBOX Y LINUX

--------------------------------------------------
1. Introduccion a la virtualizacion
2. Arquitectura del entorno virtualizado
3. Recursos de hardware virtualizados
4. Sistema operativo Linux
5. Demostracion practica
6. Resultados y conclusiones
7. Finalizar presentacion
--------------------------------------------------""")
    return input("Seleccione una opcion:\n")


def introduccion():
    print("""==================================================
          1. INTRODUCCION A LA VIRTUALIZACION
==================================================

¿QUE ES LA VIRTUALIZACION?

Es una tecnologia que permite crear entornos
virtuales capaces de ejecutar sistemas operativos
y aplicaciones utilizando recursos de un equipo
fisico.

¿QUE ES UNA MAQUINA VIRTUAL?

Es un entorno de software que simula una
computadora, con procesador, memoria,
almacenamiento y dispositivos virtuales.

PRINCIPALES APLICACIONES

- Desarrollo y pruebas de software.
- Ejecucion de diferentes sistemas operativos.
- Creacion de entornos aislados.
- Aprovechamiento de recursos fisicos.

OBJETIVO DE ESTE PROYECTO

Implementar Linux dentro de VirtualBox y
demostrar la ejecucion de Python en un
sistema operativo invitado.""")
    pausar()


def arquitectura():
    print("""==================================================
       2. ARQUITECTURA DEL ENTORNO VIRTUALIZADO
==================================================

SISTEMA ANFITRION (HOST)
Windows 11

Es el sistema operativo principal instalado
en la computadora fisica.

HIPERVISOR
Oracle VirtualBox - Tipo 2

Es el software que permite crear y ejecutar
maquinas virtuales sobre el sistema anfitrion.

SISTEMA INVITADO (GUEST)
Xubuntu 26.04.1 LTS

Es el sistema operativo instalado dentro
de nuestra maquina virtual.

ESQUEMA DE FUNCIONAMIENTO

+--------------------------------------------+
|             WINDOWS 11 - HOST              |
|                                            |
|  +--------------------------------------+  |
|  |        ORACLE VIRTUALBOX             |  |
|  |                                      |  |
|  |  +--------------------------------+  |  |
|  |  |       XUBUNTU - GUEST          |  |  |
|  |  |                                |  |  |
|  |  |       PYTHON 3                 |  |  |
|  |  +--------------------------------+  |  |
|  +--------------------------------------+  |
+--------------------------------------------+

VirtualBox proporciona hardware virtual
para que Linux pueda ejecutar aplicaciones.""")
    pausar()


def recursos():
    print(f"""==================================================
         3. RECURSOS DE HARDWARE VIRTUALIZADOS
==================================================

CONFIGURACION DEFINIDA EN VIRTUALBOX

Memoria RAM asignada:       4096 MB
Procesadores virtuales:     2 vCPU
Disco virtual configurado:  30 GB

RECURSOS DETECTADOS DESDE LINUX

Arquitectura:               {consultar(platform.machine)}
CPU disponibles:            {consultar(os.cpu_count)}
Memoria RAM total:          {memoria_total()}
Capacidad sistema archivos: {capacidad_disco()}

INTERPRETACION

VirtualBox presenta recursos virtuales al
sistema operativo invitado.

Linux utiliza estos recursos para ejecutar
sus procesos y administrar memoria y archivos.

Los valores configurados pueden diferir
de las mediciones disponibles en Linux.""")
    pausar()


def sistema_operativo():
    print(f"""==================================================
            4. SISTEMA OPERATIVO LINUX
==================================================

INFORMACION DEL SISTEMA INVITADO

Sistema operativo:          {consultar(platform.system)}
Distribucion:               {distribucion()}
Version del kernel:         {consultar(platform.release)}
Arquitectura:               {consultar(platform.machine)}
Version de Python:          {consultar(platform.python_version)}

¿QUE ES UN SISTEMA OPERATIVO?

Es el software que administra los recursos
del equipo y permite ejecutar aplicaciones.

¿QUE ES EL KERNEL?

Es el nucleo del sistema operativo.
Administra procesos, memoria y dispositivos.

EJECUCION DEL PROGRAMA

Este programa Python se ejecuta como un
proceso dentro del sistema operativo Linux.""")
    pausar()


def demostracion():
    while True:
        print("""==================================================
             5. DEMOSTRACION PRACTICA
==================================================

CONSULTAS AL SISTEMA OPERATIVO INVITADO

1. Identificar sistema operativo
2. Consultar procesadores disponibles
3. Consultar directorio de ejecucion
4. Volver al menu principal
""")
        opcion = input("Seleccione una prueba:\n")
        if opcion in ("1", "2", "3"):
            limpiar_pantalla()
        if opcion == "1":
            print(f"""--------------------------------------------------
PRUEBA 1 - IDENTIFICACION DEL SISTEMA
--------------------------------------------------

Consultando el entorno de ejecucion...

Sistema detectado: {consultar(platform.system)}

RESULTADO
Python puede consultar informacion del sistema
operativo en el que se esta ejecutando.""")
        elif opcion == "2":
            print(f"""--------------------------------------------------
PRUEBA 2 - PROCESADORES DISPONIBLES
--------------------------------------------------

Consultando los recursos de procesamiento...

Procesadores detectados: {consultar(os.cpu_count)}

CONFIGURACION DE REFERENCIA
Procesadores asignados en VirtualBox: 2 vCPU

RESULTADO
El sistema operativo invitado utiliza
los recursos de CPU que tiene disponibles.""")
        elif opcion == "3":
            print(f"""--------------------------------------------------
PRUEBA 3 - SISTEMA DE ARCHIVOS
--------------------------------------------------

Consultando el directorio de trabajo...

Directorio actual:
{consultar(os.getcwd)}

RESULTADO
El programa accede al sistema de archivos
del entorno donde se esta ejecutando.""")
        elif opcion == "4":
            return
        else:
            print("Prueba no valida. Seleccione una opcion del 1 al 4.")
            continue
        input("\nPresione ENTER para continuar...\n")
        limpiar_pantalla()


def conclusiones():
    print("""==================================================
           6. RESULTADOS Y CONCLUSIONES
==================================================

RESULTADOS DEL TRABAJO

1. Se creo una maquina virtual con VirtualBox.

2. Se instalo Xubuntu como sistema invitado.

3. Se configuraron CPU, RAM y almacenamiento.

4. Se verifico el funcionamiento de Linux.

5. Se ejecuto Python dentro de la maquina
   virtual y se consultaron recursos reales.

VENTAJAS OBSERVADAS

- Separacion entre anfitrion e invitado.
- Posibilidad de probar otro sistema operativo.
- Entorno reutilizable para desarrollo.
- Control sobre los recursos asignados.

LIMITACIONES

- Consume recursos del equipo anfitrion.
- El rendimiento depende del hardware fisico.
- El aislamiento no implica seguridad absoluta.

CONCLUSION

La virtualizacion permite ejecutar un sistema
operativo invitado sobre recursos administrados
por un hipervisor.

En este trabajo se utilizo VirtualBox para
implementar Linux y ejecutar una aplicacion
Python dentro de un entorno virtualizado.""")
    pausar()


def main():
    limpiar_pantalla()
    mostrar_presentacion()
    limpiar_pantalla()
    while True:
        opcion = mostrar_menu()
        if opcion in ("1", "2", "3", "4", "5", "6", "7"):
            limpiar_pantalla()
        if opcion == "1":
            introduccion()
        elif opcion == "2":
            arquitectura()
        elif opcion == "3":
            recursos()
        elif opcion == "4":
            sistema_operativo()
        elif opcion == "5":
            demostracion()
        elif opcion == "6":
            conclusiones()
        elif opcion == "7":
            print("""==================================================
             FIN DE LA PRESENTACION
==================================================

Trabajo Integrador
Arquitectura y Sistemas Operativos

Tema: Virtualizacion con VirtualBox y Linux

AySO VirtualLab finalizado correctamente.""")
            break
        else:
            print("Opcion no valida. Seleccione un numero del 1 al 7.")
            continue
        limpiar_pantalla()


if __name__ == "__main__":
    main()
