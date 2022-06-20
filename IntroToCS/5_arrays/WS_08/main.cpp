// Function that find the smallest difference (in absolute value)
//   between two elements of an array.

#include <iostream>

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << "\n";
    }
    std::cout << std::endl;
}

void findSmallestDifference(int arr[], int size)
{
    int smallestDifference = arr[0] - arr[1];
    if (smallestDifference < 0)
    {
        smallestDifference *= -1;
    }
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            int difference = arr[i] - arr[j];
            if (difference < 0)
            {
                difference *= -1;
            }
            if (difference < smallestDifference)
            {
                smallestDifference = difference;
            }
        }
    }
    std::cout << "The smallest difference between two elements is: " << smallestDifference << "\n";
}

int main()
{
    int size;
    std::cout << "Enter the size of the array: \n";
    std::cin >> size;
    int *arr = new int[size];
    std::cout << "Enter the array: \n";
    for (int i = 0; i < size; i++)
    {
        std::cin >> arr[i];
    }
    printArray(arr, size);
    findSmallestDifference(arr, size);
    return 0;
}