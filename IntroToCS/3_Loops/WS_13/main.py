# Determine si un número es primo o no.

def get_data():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("That's not a number!")


def main():
    num = get_data()
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')


if __name__ == '__main__':
    main()
