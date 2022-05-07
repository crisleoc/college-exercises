# Encuentre el volumen y el área de la superficie de un cono.

import math


def get_data():
    while True:
        try:
            num = int(input("\033[1;33mInserte un número: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def area(radius_base, height):
    generatrix = math.sqrt(height**2+radius_base**2)
    result = math.pi*radius_base*generatrix
    print(round(result, 2))


def volume(radius_base, height):
    result = (1/3)*math.pi*radius_base**2*height
    print(round(result, 2))


def main():
    r = get_data()
    h = get_data()
    area(r, h)
    volume(r, h)


if __name__ == '__main__':
    main()
