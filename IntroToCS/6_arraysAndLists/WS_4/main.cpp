#include <iostream>
using namespace std;

// Function that recives a 2D array, fills it with user input and returns the array
int **fillArray(int fil, int col)
{
    int **array = new int *[fil];
    for (int i = 0; i < fil; i++)
    {
        array[i] = new int[col];
    }
    for (int i = 0; i < fil; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> array[i][j];
        }
    }
    return array;
}

// Function that prints a 2D array
void printArray(int **array, int fil, int col)
{
    for (int i = 0; i < fil; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cout << array[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int col, fil;
    cin >> fil;
    cin >> col;
    int **array1 = fillArray(fil, col);
    // printArray(array1, fil, col);
    int **array2 = fillArray(fil, col);
    // printArray(array2, fil, col);
    // sum the elements with the same index in both arrays and put them in a new array
    int **array3 = new int *[fil];
    for (int i = 0; i < fil; i++)
    {
        array3[i] = new int[col];
    }
    for (int i = 0; i < fil; i++)
    {
        for (int j = 0; j < col; j++)
        {
            array3[i][j] = array1[i][j] + array2[i][j];
        }
    }
    printArray(array3, fil, col);

    return 0;
}