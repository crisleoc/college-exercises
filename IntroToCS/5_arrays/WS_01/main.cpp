#include <iostream>

// Function that read the size of a array, read the elements and print the array
void printArray(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        std::cout << array[i] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    int size;
    std::cout << "Enter the size of the array: ";
    std::cin >> size;
    int array[size];
    for (int i = 0; i < size; i++)
    {
        std::cout << "Enter the element " << i << ": ";
        std::cin >> array[i];
    }
    printArray(array, size);
    return 0;
}
