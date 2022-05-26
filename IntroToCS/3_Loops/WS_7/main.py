# Lea en x el interés anual. Escribir un programa que
#  calcule cuantos años tarda en duplicarse un capital con un interés anual x.
def get_data():
    while True:
        try:
            value = float(input())
            return value
        except ValueError:
            print('Caracter(es) invalidos')


def main():
    capital = 1000
    years = 1
    interest = get_data()
    while capital < 2000:
        capital = capital * ((1 + (interest/12)) ** 12)
        years += 1
    print(years)


if __name__ == '__main__':
    main()
