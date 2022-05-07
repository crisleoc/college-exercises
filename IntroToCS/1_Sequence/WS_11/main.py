# Escriba un programa que indique la cantidad de billetes
# de cada denominación ($50.000, $20.000 y $10.000) que debe
# entregar un cajero automático que sigue las siguientes reglas:

# -El usuario puede pedir hasta un máximo de $1.400.000 y mínimo $10.000.
# -Los valores pedidos son múltiplos de $10.000.
# -El cajero debe entregar la cantidad máxima de billetes de $50.000 que
# se pueden entregar, luego de billetes de $20.000 y el residuo con $10.000.


import math


def get_data():
    while True:
        try:
            num = int(
                input(f"\033[1;33mInserte el dinero que desea extraer: \033[0;m"))
            if num >= 10000 and num <= 1400000:
                if num % 10000 == 0:
                    return num
                else:
                    print(
                        "\033[0;31mEl valor a extraer debe ser multiplo de 10.\033[0;m")
            else:
                print(
                    "\033[0;31mNo puede extraer menos de 10K o más de 1.4M.\033[0;m")
        except ValueError as error:
            msg = str(error)
            print(f"\033[1;31m{msg.capitalize()} \033[0;m")


def main():
    money = get_data()
    balance = money
    tickets_50k = 0
    tickets_20k = 0
    tickets_10k = 0
    while balance != 0:
        if balance / 50000 >= 1:
            tickets_50k = math.floor(balance/50000)
            balance = balance % 50000
        elif balance / 20000 >= 1:
            tickets_20k = math.floor(balance/20000)
            balance = balance % 20000
        elif balance / 10000 >= 1:
            tickets_10k = math.floor(balance/10000)
            balance = balance % 10000
    print(tickets_50k)
    print(tickets_20k)
    print(tickets_10k)


if __name__ == '__main__':
    main()
