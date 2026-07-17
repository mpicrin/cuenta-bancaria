class Cuenta:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.prestamos = []
        
    def depositar(self):
        ingreso = int(input("Cuanto desea depositar: "))
        self.saldo += ingreso
        print(f"Saldo agregado con exito.\n Saldo actual {self.saldo}$")
        
    def retirar(self):
        if self.saldo > 0:
            retiro = int(input(f"Saldo {self.saldo}$ a Retirar: "))
            if retiro > self.saldo:
                print(f"No dispone de esa cantidad su saldo es de {self.saldo}$. Pida un prestamo")
            else:
                self.saldo -= retiro
                print(f"Se han descontado {retiro}$ de su cuenta.\nSaldo restante {self.saldo}$")
        else:
            print("No dispone de fondos para retirar")
            
    def pagar_prestamos(self):
        if not self.prestamos:
            return "No tiene deudas"
        else:
            for i, p in enumerate(self.prestamos ,start=1):
                print(f"{i} - Monto: {p["monto"]}$ Pendiente a pagar: {p["pendiente"]}$")
                
            opc = int(input("-> ")) - 1
            print(f"\nDeuda: {self.prestamos[opc]["pendiente"]}$  Saldo: {self.saldo}$")
            cant = int(input("Cuanto va a pagar: "))
            if self.saldo > cant:
                if cant >= self.prestamos[opc]["pendiente"]:
                    self.saldo -= self.prestamos[opc]["pendiente"]
                    self.prestamos.pop(opc)
                    return f"Pago total del prestamo realizado. Saldo restante {self.saldo}$"
                else:
                    self.prestamos[opc]["pendiente"] -= cant
                    self.saldo -= cant
                    return f"Pago parcial realizado queda {self.prestamos[opc]["pendiente"]} | Saldo restante {self.saldo}$"
            else:
                return "No tiene Saldo sufuciente"
               
    def pedir_prestamos(self):
        prest = sum(p["monto"] for p in self.prestamos)

        if prest >= 10000:
            return f"Tiene una deuda de {prest}$, no se puede aceptar más por el momento. Por favor pague."
        else: 
            while True:
                monto = int(input("Cuanto desea pedir: "))
                if monto + prest <= 10000:
                    break
                else: print(f"Puede pedir un max de 10000\n Tiene {prest}$ | Puede pedir {10000 - prest}")
            pendiente = monto + monto * 0.05
            prestamo = {"monto":monto ,"pendiente":pendiente}
            self.prestamos.append(prestamo)
            self.saldo += monto
            return f"Se le aplicará un 5% de comisión\n   |{monto} -> {pendiente}|\n Saldo actual {self.saldo}$"
            
    def mostrar_estado(self):
        print(f"Cuenta de: {self.titular} \nSaldo: {self.saldo}$   Prestamos: {sum(p["pendiente"] for p in self.prestamos)}$")
    
class Main:
    def main():
        cuenta = Cuenta("Raidel", 2000)
        while True:
            
            print("""\n     ___MENU___
    1- Depositar
    2- Retirar
    3- Ver cuenta
      Prestamos
    4- Pedir prestamos
    5- Pagar prestamos
    0- Salir...\n""")
            opc = input("-> ")
            match (opc):
                case "1": cuenta.depositar()
                case "2": cuenta.retirar()
                case "3": cuenta.mostrar_estado()
                case "4": print(cuenta.pedir_prestamos())
                case "5": print(cuenta.pagar_prestamos())
                case "0": break
                case _: print("Eso no es opcion")
                
if __name__ == "__main__":
    Main.main() 