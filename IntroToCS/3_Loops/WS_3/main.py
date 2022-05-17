def get_data():
    try:
        value = int(input())
        return value
    except ValueError:
        print("Caracter(es) invalidos")


def main():
    number = get_data()
    result = 0
    for i in range(0, number):
        result += i
    print(result)



if "__main__" == __name__:
    main()