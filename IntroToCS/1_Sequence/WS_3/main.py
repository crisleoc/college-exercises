# Escriba un programa calcule el area superficial corporal
# deacuerdo a los metodos de Mosteller(1), DuBois & DuBois(2)
# y Gehan & George(3), el usuario debe poder elegir el
# metodo que quiere usar.

import math


def print_menu():
    print('''
        \033[1;37;44mCalcular area superficial corporal \033[0;m
        Seleccione un método para calcular su area superficial
        \t 1. -Método Mosteller
        \t 2. -Método DuBois
        \t 3. -Método Gehan & George
        ''')


def get_data(text):
    checker = 1
    while checker == 1:
        try:
            data = float(input(text))
            checker = 0
            return data
        except ValueError:
            print("\033[1;31m\tCarácter(s) no permitido(s) \033[0;m")


def mosteller():
    height = get_data('\t\033[0;36mIngrese su altura (cm): \033[0;m')
    weight = get_data('\t\033[0;36mIngrese su peso (kg): \033[0;m')
    result = round(math.sqrt((weight*height)/3600), 2)
    print(f"\033[1;32m\tSu ASC (M. Monsteller) es de: {result} m^2  \033[0;m")


def dubois():
    height = get_data('\t\033[0;36mIngrese su altura (cm): \033[0;m')
    weight = get_data('\t\033[0;36mIngrese su peso (kg): \033[0;m')
    result = round(0.007184*height**0.725*weight**0.425, 2)
    print(
        f"\033[1;32m\tSu ASC (M. Dubois & Dubois) es de: {result} m^2  \033[0;m")


def gehan_and_george():
    height = get_data('\t\033[0;36mIngrese su altura (cm): \033[0;m')
    weight = get_data('\t\033[0;36mIngrese su peso (kg): \033[0;m')
    result = round(0.0235*height**0.42246*weight**0.51456, 2)
    print(
        f"\033[1;32m\tSu ASC (M. Gehan and George) es de: {result} m^2  \033[0;m")


def main():
    print_menu()
    checker = 1
    while checker == 1:
        option_choosen = input(
            '\t\033[1;33mIngrese la opción elegida: \033[0;m')
        if option_choosen == "1":
            mosteller()
            checker = 0
        elif option_choosen == "2":
            dubois()
            checker = 0
        elif option_choosen == "3":
            gehan_and_george()
            checker = 0
        else:
            print(
                "\033[1;31m\tEsta opción no existe, intente nuevamente. \033[0;m")


if __name__ == '__main__':
    main()
