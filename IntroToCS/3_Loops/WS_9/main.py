# Dadas dos entradas a y b, Calcular la media y la mitad
#  de ese valor sucesivamente hasta alcanzar el cero (1e-6).

def get_data(string):
    while True:
        try:
            value = float(input(f'Ingrese el valor de {string}: '))
            return value
        except ValueError:
            print("Caracter(es) invalidos")


def main():
    a = get_data('a')
    b = get_data('b')
    while a > 1e-6:
        a = ((a + b) / 2)/2
        print(a)
        b /= 2


if __name__ == '__main__':
    main()
