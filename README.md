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
- Taller 1: Gestión de libros
- Taller 2: Cuenta bancaria con encapsulación
- Proyecto integrador: Sistema de préstamos de equipos

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