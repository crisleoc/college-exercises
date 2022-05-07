# Escriba un programa que calcule la distancia más corta
# de un punto a una línea recta.

import math


def get_data(string):
    while True:
        try:
            num = int(input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")

# y=mx+b
# ax+bx+x=0
# |Ax+Bx+C|/sqrt(A^2+B^2)


def distance(x, y, m, b):
    result = (abs(m*x+(-1)*y+b)/(math.sqrt(m**2+(-1)**2)))
    print(round(result, 3))


def main():
    x = get_data("de la coordenada X")
    y = get_data("de la coordenada Y")
    m = get_data("de la pendiente (M)")
    b = get_data("del intersecto (B)")
    distance(x, y, m, b)


if __name__ == '__main__':
    main()
