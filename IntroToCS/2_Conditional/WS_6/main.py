def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Try again.")


def main():
    data = [get_data() for i in range(4)]
    data.sort(reverse=True)
    print(data[0])


if __name__ == '__main__':
    main()
