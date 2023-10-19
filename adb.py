import os
from turtle import clear
import colorama 
 
from colorama import Fore, Back, Style



 
print("______ _                                       ")
print("|     |_|___ ___ ___ _ _ _ ___ ___ ___ ___ ___ ")
print("|  BY Diego Alejandro Programmer   ")
print("|")
print(" diego alejandro       |_|")
print(" ") 

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('デバイス  Devices  ', accion1),
        '2': ('再起動回復', accion2),
        '3': ('リブート', accion3),
        '4': ('Salir エグジット ', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print(' デバイス')
    os.system('adb devices ')


def accion2():
    print('Has elegido la opción 2')
    os.system("adb  reboot recovery  ")
# diego alejandro 
def accion3():
    print('Has elegido la opción 3')
    os.system("adb reboot ")


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
 
os.system("clear")
print(Fore.GREEN + "thanks  for your use this tool  by Diego Alejandro ")
# diego alejandro simple code 
