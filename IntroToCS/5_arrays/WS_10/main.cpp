// Function that given two arrays without repeats,
//  compute the array that results from the intersection between
//  the elements of the other two arrays. The latter must be defined
// in the exact size.

#include <iostream>

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << "\n";
    }
    std::cout << std::endl;
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
    return 0;
}
