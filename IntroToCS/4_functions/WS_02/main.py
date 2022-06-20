def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)


def main():
    data = get_data()
    print(recursive_factorial(data))


if __name__ == '__main__':
    main()
