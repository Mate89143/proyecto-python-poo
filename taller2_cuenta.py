class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria aplicando el concepto de encapsulación.

    Atributos privados:
        _titular (str): Nombre del titular de la cuenta.
        _saldo (float): Saldo actual de la cuenta.
    """

    def __init__(self, titular, saldo=0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo (float, opcional): Saldo inicial de la cuenta. Por defecto es 0.
        """
        self._titular = titular
        self._saldo = saldo

    # =======================
    # PROPIEDAD: TITULAR
    # =======================
    @property
    def titular(self):
        """
        Permite obtener el nombre del titular (solo lectura).
        """
        return self._titular

    # =======================
    # PROPIEDAD: SALDO
    # =======================
    @property
    def saldo(self):
        """
        Permite obtener el saldo actual de la cuenta.
        """
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Permite modificar el saldo con validación.

        Regla:
            - No se permite establecer un saldo negativo.

        Raises:
            ValueError: Si el saldo es negativo.
        """
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    # =======================
    # MÉTODO: DEPOSITAR
    # =======================
    def depositar(self, cantidad):
        """
        Incrementa el saldo si la cantidad es positiva.

        Args:
            cantidad (float): Dinero a depositar.

        Returns:
            bool: True si la operación fue exitosa, False si no.
        """
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    # =======================
    # MÉTODO: RETIRAR
    # =======================
    def retirar(self, cantidad):
        """
        Disminuye el saldo si hay suficiente dinero.

        Args:
            cantidad (float): Dinero a retirar.

        Returns:
            bool: True si la operación fue exitosa, False si no.
        """
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


# =======================
# PRUEBA DEL PROGRAMA
# =======================
if __name__ == "__main__":
    cuenta = CuentaBancaria("Mateo", 1000)

    print("Titular:", cuenta.titular)
    print("Saldo inicial:", cuenta.saldo)

    # Depósito válido
    if cuenta.depositar(500):
        print("Depósito exitoso")
    else:
        print("Depósito inválido")

    print("Saldo actual:", cuenta.saldo)

    # Retiro válido
    if cuenta.retirar(300):
        print("Retiro exitoso")
    else:
        print("Retiro inválido")

    print("Saldo final:", cuenta.saldo)

    # Prueba de validación (opcional)
    try:
        cuenta.saldo = -100
    except ValueError as e:
        print("Error:", e)