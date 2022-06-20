def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")


def digits(n, b):
    if n == 0:
        return 0
    else:
        return 1 + digits(n // b, b)


def main():
    n = get_data()
    b = get_data()
    print(digits(n, b))


if __name__ == '__main__':
    main()
