// Function given two arrays of integers of equal size,
// compute an array that contains the sum of the corresponding
// elements of the other two.

#include <iostream>
using namespace std;

void sum_arrays(int arr1[], int arr2[], int arr3[], int size)
{
    for (int i = 0; i < size; i++)
    {
        arr3[i] = arr1[i] + arr2[i];
    }
}

void print_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << "\n";
    }
}

void fill_array(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
}

int main()
{
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;
    int *arr1 = new int[size];
    int *arr2 = new int[size];
    int *arr3 = new int[size];
    fill_array(arr1, size);
    fill_array(arr2, size);
    sum_arrays(arr1, arr2, arr3, size);
    print_array(arr3, size);
    return 0;
}
