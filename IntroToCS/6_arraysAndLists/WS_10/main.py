def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")

# A function that reads a number and tells if it is a palindrome or not.


def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False


def main():
    number = get_data()
    if is_palindrome(number):
        print("si")
    else:
        print("no")


if __name__ == "__main__":
    main()
