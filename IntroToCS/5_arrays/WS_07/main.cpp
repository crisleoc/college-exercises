// Function that find the second largest element in an given array.

#include <iostream>

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << "\n";
    }
    std::cout << std::endl;
}

void findSecondLargest(int arr[], int size)
{
    int largest = arr[0];
    int secondLargest = arr[0];
    for (int i = 0; i < size; i++)
    {
        if (arr[i] > largest)
        {
            secondLargest = largest;
            largest = arr[i];
        }
        else if (arr[i] > secondLargest)
        {
            secondLargest = arr[i];
        }
    }
    std::cout << "The second largest element is: " << secondLargest << "\n";
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
    findSecondLargest(arr, size);
    return 0;
}