# Encuentre el área de un hexágono regular circunscrito en un círculo de radio dado.

import math


def get_data(string):
    while True:
        try:
            num = int(input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def height_triangle(radius):
    result = math.sqrt(radius**2-((radius/2)**2))
    return result


def area(radius):
    h_triangle = height_triangle(radius)
    result = 6*((radius*h_triangle)/2)
    print(round(result, 2))


def main():
    radius = get_data("del radio del circulo")
    area(radius)


if __name__ == '__main__':
    main()
