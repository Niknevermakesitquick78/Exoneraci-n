import random

class Usuario:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo
        self.historial = []

    def calcular_costo(self, km):
        return km * 0.50

    def recargar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Saldo recargado. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Error: monto invalido")

    def realizar_viaje(self, km):
        if km <= 0:
            print("Error: kilometros invalidos")
            return

        costo = self.calcular_costo(km)

        if self.saldo >= costo:
            self.saldo -= costo
            self.historial.append(km)
            codigo = random.randint(100, 999)
            print(f"Viaje #{codigo} realizado! Costo: ${costo:.2f}. Saldo: ${self.saldo:.2f}")
        else:
            print("Error: saldo insuficiente")

    def ver_historial(self):
        print("=== HISTORIAL ===")
        if not self.historial:
            print("No hay viajes registrados")
        else:
            for i, km in enumerate(self.historial, 1):
                print(f"Viaje {i}: {km} km")

    def ver_perfil(self, detallado=True):
        if detallado:
            print("=== PERFIL (detallado) ===")
            print(f"Nombre: {self.nombre}")
            print(f"Tipo: Normal")
            print(f"Saldo: ${self.saldo:.2f}")
            print(f"Viajes: {len(self.historial)}")
        else:
            print(f"Nombre: {self.nombre} | Saldo: ${self.saldo:.2f}")

    def gasto_total(self):
        total = 0
        for km in self.historial:
            total += self.calcular_costo(km)
        return total


class UsuarioPremium(Usuario):
    def calcular_costo(self, km):
        return km * 0.50 * 0.80

    def ver_perfil(self, detallado=True):
        if detallado:
            print("=== PERFIL (detallado) ===")
            print(f"Nombre: {self.nombre}")
            print(f"Tipo: Premium")
            print(f"Saldo: ${self.saldo:.2f}")
            print(f"Viajes: {len(self.historial)}")
        else:
            print(f"Nombre: {self.nombre} | Saldo: ${self.saldo:.2f}")


def pedir_tipo():
    while True:
        tipo = input("Tipo (1=Normal, 2=Premium): ")
        if tipo in ["1", "2"]:
            return int(tipo)
        else:
            print("Invalido, intenta de nuevo")


def pedir_saldo():
    while True:
        try:
            saldo = float(input("Saldo inicial: "))
            if saldo >= 0:
                return saldo
            else:
                print("Invalido, intenta de nuevo")
        except:
            print("Invalido, intenta de nuevo")


def pedir_opcion_menu():
    while True:
        opcion = input("Opcion: ")
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            return opcion
        else:
            print("Invalido, intenta de nuevo")


def pedir_monto():
    while True:
        try:
            monto = float(input("Monto a recargar: "))
            return monto
        except:
            print("Invalido, intenta de nuevo")


def pedir_km():
    while True:
        try:
            km = float(input("Kilometros: "))
            return km
        except:
            print("Invalido, intenta de nuevo")


def pedir_detallado():
    while True:
        modo = input("¿Detallado? (s/n): ").lower()
        if modo in ["s", "n"]:
            return modo == "s"
        else:
            print("Invalido, intenta de nuevo")


def main():
    nombre = input("Nombre: ")
    tipo = pedir_tipo()
    saldo = pedir_saldo()

    if tipo == 2:
        usuario = UsuarioPremium(nombre, saldo)
    else:
        usuario = Usuario(nombre, saldo)

    while True:
        print("\n=== MENU ===")
        print("1. Recargar saldo")
        print("2. Realizar viaje")
        print("3. Ver historial")
        print("4. Ver perfil")
        print("5. Ver gasto total")
        print("6. Salir")

        opcion = pedir_opcion_menu()

        if opcion == "1":
            monto = pedir_monto()
            usuario.recargar(monto)

        elif opcion == "2":
            km = pedir_km()
            usuario.realizar_viaje(km)

        elif opcion == "3":
            usuario.ver_historial()

        elif opcion == "4":
            detallado = pedir_detallado()
            usuario.ver_perfil(detallado)

        elif opcion == "5":
            total = usuario.gasto_total()
            print(f"Gasto total: ${total:.2f}")

        elif opcion == "6":
            print("Gracias por usar el servicio")
            break


main()
