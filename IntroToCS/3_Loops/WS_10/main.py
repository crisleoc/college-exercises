# Lea un número entero positivo n y, usando ciclos, escribir
#  un programa que calcule la suma de los cuadrados de los n
#  primeros números enteros.


def get_data():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print("Caracter(es) no valido(s)")


def main():
    n = get_data()
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    print(sum)


if __name__ == "__main__":
    main()
