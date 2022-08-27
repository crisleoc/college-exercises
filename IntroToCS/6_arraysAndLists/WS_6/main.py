def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")

# a function that sorts an array in ascending order


def sort_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array


def main():
    arraySize = get_data()
    array = []
    for i in range(arraySize):
        array.append(get_data())
    print(sort_array(array))


if __name__ == '__main__':
    main()
