import otherfunc
import time
import tkinter as tk

def run():
    cuenta1 = 0
    print('*'*10)
    print('BIENVENIDO AL BANCO DATANOVA'.title())
    print('*'*10)
    name = input('Cual es tu nombre => ')
    print(f'Que acción deseas realizar {name}')
    time.sleep(1)

    while True:
        print('1- Consultar saldo')
        print('2- Agregar Dinero')
        print('3- Sacar dinero')
        print('4- Salir')
        eleccion1 = input()
        if eleccion1 == '1':
            print(f'Tu saldo es ${cuenta1}')
        elif eleccion1 == '2':
            cuenta1 += otherfunc.ingresar_dinero(cuenta1,name)
            print(f'Tu saldo actual es ${cuenta1}')
        elif eleccion1 == '3':
            cuenta1 = otherfunc.sacar_dinero(cuenta1,name)
        elif eleccion1 == '4':
            print('GRACIAS POR ACCEDER AL BANCO DATANOVA'.title())
            break
        else:
            print('Elige una opción valida')
            continue
        print('Deseas hacer otro movimiento => ')
        eleccion = input().lower()
        if eleccion == 'si':
            pass
        else:
            break
    

if __name__ == '__main__':
    run()
    print('Saludos Banco DataNova')


    