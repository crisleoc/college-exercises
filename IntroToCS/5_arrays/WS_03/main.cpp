// Function that read the size of the array, read its elements
//  one by one and print its maximum value and its minimum value.

#include <iostream>
using namespace std;

void readArray(int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << "Enter element " << i + 1 << ": ";
        cin >> array[i];
    }
}

void printArray(int *array, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << array[i] << "\n";
    }
    cout << endl;
}

int maxValue(int *array, int size)
{
    int max = array[0];
    for (int i = 1; i < size; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
    }
    return max;
}

int minValue(int *array, int size)
{
    int min = array[0];
    for (int i = 1; i < size; i++)
    {
        if (array[i] < min)
        {
            min = array[i];
        }
    }
    return min;
}

int main()
{
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int *array = new int[size];
    readArray(array, size);
    printArray(array, size);
    cout << "Max value: " << maxValue(array, size) << endl;
    cout << "Min value: " << minValue(array, size) << endl;
    delete[] array;
    return 0;
}