# Escribir un programa que escriba los números comprendidos
#  entre 1 y 1000. El programa escribirá en la pantalla los
#  números en grupos de 20, solicitando al usuario si quiere
#  o no continuar visualizando el siguiente grupo de números.

def get_data():
    while True:
        try:
            value = input('Imprimir +20 números? (yes/no): ')
            if value == 'yes' or value == 'no':
                return value
            else:
                raise ValueError
        except ValueError:
            print("Solo se permite ingresar Yes o No")


def main():
    check = 'yes'
    number = 0
    while check == 'yes':
        check = get_data()
        if check == 'yes':
            for i in range(number+1, number+21):
                print(i)
                if i == number+20:
                    number += 20
                    break


if __name__ == '__main__':
    main()
