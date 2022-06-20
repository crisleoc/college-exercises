def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")


def narcissistic(number, base):
    number_string = str(number)
    sum = 0
    for digit in number_string:
        digit = int(digit)
        digit = digit ** base
        sum += digit
    if sum == number:
        return True
    else:
        return False


def main():
    n = get_data()
    b = get_data()
    print(str(narcissistic(n, b)).lower())


if __name__ == '__main__':
    main()
