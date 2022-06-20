def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    data = get_data()
    print(fibonacci(data))


if __name__ == '__main__':
    main()
