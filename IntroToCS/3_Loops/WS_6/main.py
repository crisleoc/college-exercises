# Leer un entero positivo n. Imprimir los n primeros enteros
#  positivos en forma descendente seguidos por el cero. | |


def get_data():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print('Caracter(es) invalidos')


def main():
    number = get_data()
    for i in range(number, -1, -1):
        print(i)


if __name__ == '__main__':
    main()
