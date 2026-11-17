# Trabajo Práctico Integrador — Arquitectura y Sistemas Operativos

**Universidad Tecnológica Nacional (UTN)**  
**Tecnicatura Universitaria en Programación**

## Integrantes

- **Villalba Aarón Exequiel**
- **Franco Agustín Gómez**

## Descripción del proyecto

Este repositorio contiene el Trabajo Práctico Integrador de la materia **Arquitectura y Sistemas Operativos**, enfocado en el estudio y la aplicación práctica de la virtualización.

El proyecto consiste en implementar un entorno virtualizado mediante **Oracle VirtualBox**, utilizando Windows 11 como sistema anfitrión y Xubuntu Linux como sistema invitado.

Como complemento, se desarrolló **AySO VirtualLab**, una aplicación de consola en Python que permite demostrar conceptos de virtualización y consultar información del sistema operativo y sus recursos.

## Objetivos

- Comprender los fundamentos de la virtualización.
- Identificar los componentes de una arquitectura virtualizada.
- Configurar y utilizar una máquina virtual.
- Instalar un sistema operativo Linux.
- Analizar los recursos asignados al sistema invitado.
- Desarrollar una aplicación Python para demostrar conceptos de sistemas operativos.
- Documentar los procedimientos, resultados y conclusiones.

## Entorno de trabajo

| Componente | Tecnología |
|---|---|
| Sistema anfitrión | Windows 11 |
| Hipervisor | Oracle VirtualBox (tipo 2) |
| Sistema invitado | Xubuntu 26.04.1 LTS |
| Memoria RAM | 4096 MB |
| Procesadores virtuales | 2 |
| Disco virtual | 30 GB (VDI) |
| Red | NAT |
| Sistema de archivos | ext4 |
| Lenguaje | Python 3 |

## Contenido del repositorio

### 1. Informe del trabajo integrador

**[Consultar informe completo en PDF](./TPI_Virtualizacion_AySO_VirtualLab_Entrega_Corregida.pdf)**

El documento desarrolla la fundamentación teórica, la metodología utilizada, la configuración del entorno virtual, la experiencia práctica, los resultados y las conclusiones.

### 2. Aplicación AySO VirtualLab

**[Consultar código fuente — main.py](./main.py)**

Aplicación de consola desarrollada en Python 3 que incluye:

- Introducción a la virtualización.
- Arquitectura anfitrión, hipervisor e invitado.
- Información sobre CPU, memoria RAM y almacenamiento.
- Identificación del sistema operativo y el entorno Python.
- Demostraciones prácticas mediante consultas al sistema.
- Resultados y conclusiones.

**Ejecución en Linux:**

```bash
python3 main.py
```

### 3. Video de presentación

**[Ver presentación y demostración práctica en Google Drive](https://drive.google.com/file/d/11SVa0zSlMRffMnKZwwe274r7KnMa0_9M/view?usp=drive_link)**

El video presenta los conceptos principales del trabajo, la configuración de la máquina virtual y una demostración de la aplicación desarrollada.

## Conclusiones

Este proyecto permitió relacionar los fundamentos teóricos de la virtualización con su implementación práctica.

Mediante VirtualBox y Xubuntu fue posible crear un entorno aislado, asignar recursos virtuales y observar el funcionamiento de un sistema operativo invitado.

La aplicación AySO VirtualLab complementó esta experiencia, permitiendo consultar información real del sistema y aplicar conocimientos de programación en Python.

---

**UTN — Tecnicatura Universitaria en Programación**  
*Trabajo Práctico Integrador — Arquitectura y Sistemas Operativos*