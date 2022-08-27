def get_data():
    while True:
        try:
            data = int(input("Enter a number: "))
            return data
        except ValueError:
            print("Invalid input. Please try again.")

# function that receives and array and delete the elements that are less or equeal to the average


def delete_elements(array):
    sum = 0
    for i in array:
        sum += i
    average = sum / len(array)
    for i in array:
        if i <= average:
            array.remove(i)
    return array


def main():
    arraySize = get_data()
    array = []
    for i in range(arraySize):
        array.append(get_data())
    print(delete_elements(array))


if __name__ == '__main__':
    main()
