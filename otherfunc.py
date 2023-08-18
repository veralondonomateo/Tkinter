import time

def ingresar_dinero(cuenta):
    print(f'BIENVENIDO A LA SECCIÓN DE CONSIGNACIÓNES'.title())
    time.sleep(1)
    print(f' tu saldo actual es ${cuenta}')
    print('¿Que monto deseas ingresar a tu cuenta?')
    eleccion = int(input())
    cuenta += eleccion
    return cuenta

def sacar_dinero(cuenta):
    eleccion = 0
    print(f'BIENVENIDO A LA SECCIÓN DE RETIROS'.title())
    time.sleep(1)
    def elegir(eleccion):
        print(f' tu Saldo actual es ${cuenta}')
        print('¿Que cantidad deseas retirar?')
        eleccion = int(input())
        return eleccion
    x = elegir(eleccion)
    if x < cuenta:
        cuenta -= x
        print(f'Retiro exitoso ')
        print(f'Tu saldo actual es ${cuenta}')
    elif elegir(eleccion) > cuenta:
        print(f'Tu saldo es insuficiente , intenta con otra cantidad')
        elegir(eleccion)
    return cuenta