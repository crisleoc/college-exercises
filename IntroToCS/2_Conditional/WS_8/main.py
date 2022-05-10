def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Try again.")


def efficiency():
    produced = get_data()
    defective = get_data()
    if defective < 200 and produced > 10000:
        return 4
    elif defective > 200 and produced > 10000:
        return 3
    elif defective < 200 and produced < 10000:
        return 2
    elif defective > 200 and produced < 10000:
        return 1


def main():
    print("Efficiency:", efficiency())


if __name__ == '__main__':
    main()
