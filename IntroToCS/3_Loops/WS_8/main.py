# Escribir un programa que pida un número y si el
#  que se introduce por el teclado es menor de 100
#  que vuelva a solicitarlo hasta que se ingrese un
#  valor mayor o igual a 100.

def main():
    while True:
        try:
            value = int(input())
            if value > 100:
                print(value)
                break
        except ValueError:
            print('Caracter(es) invalidos')


if __name__ == '__main__':
    main()
