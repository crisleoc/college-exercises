# Escriba un programa que calcule la suma de 1+2+3+…+n.

def insert_val():
    checker = 1
    num = 0
    while checker == 1:
        try:
            num = int(input('Inserte un número: '))
            checker = 0
        except ValueError:
            print('Ingrese un carácter valido.')
    return num


def sum(value):
    result = 0
    for i in range(value+1):
        result += i
    return result


def main():
    value = insert_val()
    print(f'El resultado es: {sum(value)}')
    return sum(value)


if __name__ == '__main__':
    main()
