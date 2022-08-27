# Write a program that prints the first n numbers in reverse order and separated by hyphens.
def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    number = get_data()
    for i in range(number, 0, -1):
        if i > 1:
            print(i, end="-")
        else:
            print(i)


if __name__ == '__main__':
    main()
