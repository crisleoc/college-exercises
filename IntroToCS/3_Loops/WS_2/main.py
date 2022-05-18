def get_data():
    while True:
        try:
            value = int(input())
            return value
        except ValueError:
            print("Caracter(es) invalidos")


def main():
    num1 = get_data()
    num2 = get_data()
    for i in range(num1, num2+1):
        if i % 5 == 0:
            print(i)


if "__main__" == __name__:
    main()
