def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")


def delete_multiples(array, number):
    noMultipleArray = []
    for i in range(len(array)+1):
        if i % number != 0:
            noMultipleArray.append(array[i])
    return noMultipleArray


def main():
    x = get_data()
    arraySize = get_data()
    array = []
    for i in range(arraySize):
        array.append(get_data())
    print(delete_multiples(array, x))


if __name__ == "__main__":
    main()
