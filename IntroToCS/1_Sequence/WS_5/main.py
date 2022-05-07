# Calcule el área de un triángulo equilátero..

import math


def get_data():
    while True:
        try:
            num = int(input("\033[1;33mInserte un número: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def main():
    side = get_data()
    result = (math.sqrt(3)/4)*side**2
    print(round(result, 2))


if __name__ == '__main__':
    main()
