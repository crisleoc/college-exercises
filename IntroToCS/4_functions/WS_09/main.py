def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data


def double_factorial(n):
    if n <= 0:
        return 1
    else:
        return n * double_factorial(n-2)


def main():
    data = get_data()
    print(double_factorial(data))


if __name__ == '__main__':
    main()
