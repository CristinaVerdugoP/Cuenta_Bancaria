from cuenta_bancaria import Cuenta_Bancaria

#Creación de los objetos: cuentas
cuenta1 = Cuenta_Bancaria(700, 0.02)
cuenta2 = Cuenta_Bancaria(500, 0.03)

print("\nPara la cuenta1:")
cuenta1.hacer_deposito(200).hacer_deposito(100).hacer_deposito(50).hacer_retiro(150).generar_interes().mostrar_balance()

print("\nPara la cuenta2:")
cuenta2.hacer_deposito(100).hacer_deposito(300).hacer_retiro(50).hacer_retiro(150).hacer_retiro(350).hacer_retiro(10).generar_interes().mostrar_balance()

print("\nLlamando el balance de todas las cuentas")
Cuenta_Bancaria.todas_las_cuentas()