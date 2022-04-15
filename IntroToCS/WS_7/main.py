# Encuentre el volumen y el área de la superficie de un cono truncado.


import math


def get_data(string):
    while True:
        try:
            num = int(input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def get_generatrix(height, r_top, r_base):
    result = math.sqrt(height**2+(r_base-r_top)**2)
    return result


def volume(height, r_top, r_base):
    result = (height*math.pi/3)*(r_base**2 + r_top**2+r_base*r_top)
    print(round(result, 2))


def area(r_base, r_top, generatrix):
    result = math.pi*(r_base**2+r_top**2+generatrix*(r_base+r_top))
    print(round(result, 2))


def main():
    radius_base = get_data("del radio de la base")
    radius_top = get_data("del radio de la tapa")
    height = get_data("de la altura")
    generatrix = get_generatrix(height, radius_top, radius_base)
    area(radius_base, radius_top, generatrix)
    volume(height, radius_top, radius_base)


if __name__ == '__main__':
    main()
