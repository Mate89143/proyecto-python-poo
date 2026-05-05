# Proyecto Python POO - Clases, Objetos y Encapsulación

# Autor
Mateo Úsuga Álvarez

## Descripción del proyecto

Este proyecto implementa los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** en Python, incluyendo:

- Clases y objetos
- Encapsulación
- Atributos y métodos
- Propiedades
- Manejo de estado en objetos
- Aplicación en un sistema real de préstamos

El proyecto está dividido en tres partes:

### Taller 1: Gestión de libros

En este taller se crea una clase "Libro" que simula el funcionamiento básico de una biblioteca.

Permite:
- Registrar libros con título, autor y número de páginas.
- Prestar libros cambiando su estado a "no disponible".
- Devolver libros y actualizar su estado.
- Consultar la información completa del libro.

### Taller 2: Cuenta bancaria con encapsulación

En este taller se implementa una clase "CuentaBancaria" aplicando el concepto de encapsulación.

Permite:
- Manejar un titular y un saldo privado.
- Consultar datos de forma controlada mediante propiedades.
- Depositar dinero validando valores positivos.
- Retirar dinero verificando saldo disponible.
- Evitar valores inválidos como saldos negativos.

### Proyecto integrador: Sistema de préstamos de equipos

Este proyecto simula un sistema real de préstamos de equipos mediante un menú interactivo.

Permite:
- Ver equipos disponibles.
- Registrar préstamos con usuario y fecha.
- Devolver equipos.
- Consultar historial de préstamos.
- Agregar nuevos equipos al sistema.

---

## Diseño de clases y encapsulación

En este proyecto se aplican los principios de la POO para modelar entidades del mundo real:

- Cada clase representa un objeto con atributos y comportamientos.
- Se usa encapsulación para proteger datos internos (como `_saldo` o `_titular`).
- Los métodos controlan el acceso y modificación del estado del objeto.
- Se utilizan propiedades (`@property`) para validar y controlar datos.

Esto permite un código más organizado, seguro y fácil de mantener.

---

## Ejecución en consola

### Taller 1 - Libro

![evidencia template](/images/Taller%201.png)
![evidencia template](/images/Taller%201.2.png)

Se evidencia el cambio de estado del libro entre “Disponible” y “Prestado”, además de la validación para evitar operaciones inválidas.

### Taller 2 - Cuenta Bancaria

![evidencia template](/images/Taller%202.png)

Se muestran operaciones seguras sobre el saldo. La encapsulación evita modificar directamente los atributos y protege contra valores inválidos como saldos negativos.

### Proyecto Integrador

![evidencia template](/images/Taller%203.png)

El sistema permite interactuar con equipos mediante un menú. Cada opción modifica el estado del sistema (préstamos, devoluciones y registro de historial).

## Reflexión personal

Este proyecto me permitió comprender cómo la POO (Programación Orientada a Objetos) facilita la organización del código mediante clases y objetos.

Se aprendió a:

- Modelar problemas reales con clases.
- Usar encapsulación para proteger datos.
- Implementar métodos con lógica de negocio.
- Manejar estados dentro de objetos.

Retos superados:

- Entender el uso correcto de self.
- Aplicar propiedades con validación.
- Controlar estados en sistemas interactivos.
- Organizar múltiples archivos de forma coherente.