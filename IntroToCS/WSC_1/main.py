# Leer un número entero n de consola. Determinar si es positivo, negativo o cero.


def get_data(string):
    while True:
        try:
            num = int(input(f"\033[1;33mInserte el valor {string}: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def condition(num):
    if num == 0:
        print("Cero")
    elif num < 0:
        print("Negativo")
    elif num > 0:
        print("Positivo")


def main():
    num = get_data("del número")
    condition(num)


if __name__ == '__main__':
    main()
