# Escribir un programa que lea 10 datos desde el
#  teclado y sume sólo aquellos que sean negativos.

def get_data():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print("Caracter(es) no valido(s)")


def main():
    sum = 0
    for i in range(1, 11):
        value = get_data()
        if value < 0:
            sum += value
    print(sum)


if __name__ == '__main__':
    main()
