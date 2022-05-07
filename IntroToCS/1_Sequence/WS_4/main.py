# Dado un entero positivo de tres dígitos,
# escriba un programa que calcule la suma de sus dígitos.


def get_data():
    while True:
        try:
            num = int(input("\033[1;33mInserte un número: \033[0;m"))
            return num
        except ValueError:
            print("\033[1;31mCarácter(es) no permitido(s). \033[0;m")


def main():
    array = list(str(get_data()))
    result = 0
    for i in array:
        result += int(i)
    print(result)


if __name__ == '__main__':
    main()
