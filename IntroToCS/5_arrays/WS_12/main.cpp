// program that reads an array of integers, and a number x,
//  and writes to the screen all the indices of the positions
//  in the array where x is. For example, if the array is 1 2
// 3 1 3 2 2 1 and x is 2, the program would write: 1 5 6.

#include <iostream>

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << arr[i] << "\n";
    }
    std::cout << std::endl;
}

void findX(int arr[], int size, int x)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == x)
        {
            std::cout << i << "\n";
        }
    }
    std::cout << std::endl;
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
    int x;
    std::cout << "Enter the number to find: \n";
    std::cin >> x;
    // printArray(arr, size);
    findX(arr, size, x);
    return 0;
}
