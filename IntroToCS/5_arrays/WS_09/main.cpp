// Function that given an array, calculate another equivalent
//  but eliminating the duplicates. The latter must be defined
//  the exact size.

#include <iostream>

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << "\n";
    }
    std::cout << std::endl;
}

void findUnique(int arr[], int size)
{
    int *unique = new int[size];
    int uniqueSize = 0;
    for (int i = 0; i < size; i++)
    {
        bool isUnique = true;
        for (int j = 0; j < uniqueSize; j++)
        {
            if (arr[i] == unique[j])
            {
                isUnique = false;
                break;
            }
        }
        if (isUnique)
        {
            unique[uniqueSize] = arr[i];
            uniqueSize++;
        }
    }
    printArray(unique, uniqueSize);
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
    findUnique(arr, size);
    return 0;
}