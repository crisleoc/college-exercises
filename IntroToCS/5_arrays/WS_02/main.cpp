// Function that read the size of the array, read
// its elements one by one and print it in reverse order.

#include <iostream>

void printArray(int *array, int size)
{
    for (int i = size - 1; i >= 0; i--)
    {
        std::cout << array[i] << "\n";
    }
    std::cout << std::endl;
}

int main()
{
    int size;
    std::cout << "Enter the size of the array: ";
    std::cin >> size;
    int *array = new int[size];
    for (int i = 0; i < size; i++)
    {
        std::cout << "Enter element " << i + 1 << ": ";
        std::cin >> array[i];
    }
    printArray(array, size);
    delete[] array;
    return 0;
}