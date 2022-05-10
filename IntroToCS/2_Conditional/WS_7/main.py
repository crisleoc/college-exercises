from functools import reduce


def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Try again.")


def average_highest_values():
    data = [get_data() for i in range(4)]
    data.sort(reverse=True)
    result = reduce(lambda x, y: x + y, data[:3]) / 3
    print("%.1f" % round(result, 1))


def main():
    average_highest_values()


if __name__ == '__main__':
    main()
