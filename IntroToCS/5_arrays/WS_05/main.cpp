// Function that read the size of the array, read its
//  elements one by one and print the average and the sum of its elements.

#include <iostream>
using namespace std;

void printAverage(int arr[], int size)
{
    int i;
    int sum = 0;
    for (i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    cout << "The average of the array is: " << sum / size << endl;
}

void printSum(int arr[], int size)
{
    int i;
    int sum = 0;
    for (i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    cout << "The sum of the array is: " << sum << endl;
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
    printSum(arr, size);
    printAverage(arr, size);
    return 0;
}