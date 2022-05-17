def get_data():
    try:
        value = int(input())
        return value
    except ValueError:
        print("Caracter(es) invalidos")


def main():
    num = get_data()
    for i in range(1, num, 2):
        if i+2 < num:
            if i > 1:
                print(i+2)
        else:
            break



if "__main__" == __name__:
    main()