// Function that reads two arrays of ordered integers. The program should print the arrays and then produce a new sorted array with the elements of the two. For example, if the arrays have the numbers 1 3 6 9 17 and 2 4 10 17, respectively, the array of numbers on the screen must be 1 2 3 4 6 9 10 17 17. The latter must be set to the exact size.
// The out put should be: The numbers of the two combined arrays (with no repeating elements) in ascending order.

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

void findIntersection(int arr1[], int size1, int arr2[], int size2)
{
    int *arr3 = new int[size1];
    int counter = 0;
    for (int i = 0; i < size1; i++)
    {
        for (int j = 0; j < size2; j++)
        {
            if (arr1[i] == arr2[j])
            {
                arr3[counter] = arr1[i];
                counter++;
            }
        }
    }
    printArray(arr3, counter);
}

void findUnion(int arr1[], int size1, int arr2[], int size2)
{
    int *arr3 = new int[size1 + size2];
    int counter = 0;
    for (int i = 0; i < size1; i++)
    {
        arr3[counter] = arr1[i];
        counter++;
    }
    for (int i = 0; i < size2; i++)
    {
        bool isUnique = true;
        for (int j = 0; j < counter; j++)
        {
            if (arr2[i] == arr3[j])
            {
                isUnique = false;
                break;
            }
        }
        if (isUnique)
        {
            arr3[counter] = arr2[i];
            counter++;
        }
    }
    printArray(arr3, counter);
}

int main()
{
    int size1;
    std::cout << "Enter the size of the first array: \n";
    std::cin >> size1;
    int *arr1 = new int[size1];
    std::cout << "Enter the first array: \n";
    for (int i = 0; i < size1; i++)
    {
        std::cin >> arr1[i];
    }
    int size2;
    std::cout << "Enter the size of the second array: \n";
    std::cin >> size2;
    int *arr2 = new int[size2];
    std::cout << "Enter the second array: \n";
    for (int i = 0; i < size2; i++)
    {
        std::cin >> arr2[i];
    }
    printArray(arr1, size1);
    printArray(arr2, size2);
    findIntersection(arr1, size1, arr2, size2);
    findUnion(arr1, size1, arr2, size2);
    return 0;
}
