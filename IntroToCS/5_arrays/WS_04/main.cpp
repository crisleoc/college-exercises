// Function that read the size of the array, read its
//  elements one by one and print all negative numbers
//  in the order of the array

#include <iostream>
using namespace std;

void printNegative(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        if (arr[i] < 0)
        {
            cout << arr[i] << "\n";
        }
    }
}

void readArray(int arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        cout << "Enter element " << i + 1 << ": ";
        cin >> arr[i];
    }
}

int main()
{
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int *arr = new int[size];
    readArray(arr, size);
    cout << endl;
    printNegative(arr, size);
    return 0;
}