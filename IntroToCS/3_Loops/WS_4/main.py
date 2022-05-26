# Lea un número entero n y, usando ciclos, generar la sucesión:
# 1, 5, 3, 7, 5, 9, 7, ..., n (Hasta la primera aparición de n
# si n es impar, ó en el caso par; hasta la primera aparición de n-1).

def get_data():
    try:
        value = int(input("Ingrese un número entero: "))
        return value
    except ValueError:
        print("Caracter(es) invalidos")


def main():
    num = get_data()
    if num % 2 == 0:
        num -= 1
        for i in range(1, num, 2):
            if i >= num:
                break
            else:
                if i > 1:
                    print(i-2)
                    print(i+2)
    else:
        for i in range(1, num, 2):
            if i >= num:
                break
            else:
                if i > 1:
                    print(i-2)
                    print(i+2)


if "__main__" == __name__:
    main()
