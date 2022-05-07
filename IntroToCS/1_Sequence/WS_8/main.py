# Encuentre el volumen y el área de la superficie de un toro.
import math


def get_data(string):
    while True:
        try:
            num = int(input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def area(external_r, internal_r):
    result = 4*math.pi**2*external_r*internal_r
    print(round(result, 2))


def volume(external_r, internal_r):
    result = 2*math.pi**2*external_r*internal_r**2
    print(round(result, 2))


def main():
    internal_radius = get_data("del radio interior")
    external_radius = get_data("del radio exterior")
    area(external_radius, internal_radius)
    volume(external_radius, internal_radius)


if __name__ == '__main__':
    main()
