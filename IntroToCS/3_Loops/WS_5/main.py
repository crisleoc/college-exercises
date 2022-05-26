# Leer un número n múltiplo de 5 y generar la sucesión 5,
#  10, 15, 20, 25, 30, 35, …, n. El programa debe validar
#  que la entrada sea un múltiplo de 5 y sino mostrar un mensaje de error.

def get_data():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print('Caracter(es) invalidos')


def main():
    number = get_data()
    if number % 5 == 0:
        for i in range(5, number + 5, 5):
            print(i)
    else:
        print('Error')


if __name__ == '__main__':
    main()
