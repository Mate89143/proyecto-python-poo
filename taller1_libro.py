class Libro:
    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya estaba disponible."

    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {estado}"


def main():
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)

    print("=== Información inicial ===")
    print(libro1.informacion(), "\n")
    print(libro2.informacion(), "\n")

    print("=== Préstamo ===")
    print(libro1.prestar())
    print(libro2.prestar(), "\n")

    print("=== Intento de préstamo ===")
    print(libro1.prestar(), "\n")

    print("=== Después del préstamo ===")
    print(libro1.informacion(), "\n")

    print("=== Devolución ===")
    print(libro1.devolver(), "\n")

    print("=== Intento de devolución ===")
    print(libro1.devolver(), "\n")

    print("=== Final ===")
    print(libro1.informacion(), "\n")
    print(libro2.informacion())


if __name__ == "__main__":
    main()