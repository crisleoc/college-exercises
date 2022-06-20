def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    return data


def subfactorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    elif n >= 3:
        return (n-1) * (subfactorial(n-1)+subfactorial(n-2))


def main():
    data = get_data()
    print(subfactorial(data))


if __name__ == '__main__':
    main()
