#include <iostream>
using namespace std;

int main()
{
    int col, fil;
    cin >> fil;
    cin >> col;
    int array[fil][col];

    for (int i = 0; i < fil; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> array[i][j];
        }
    }

    for (int i = 0; i < col; i++)
    {
        int sum = 0;
        for (int j = 0; j < fil; j++)
        {
            sum += array[j][i];
        }
        cout << sum << endl;
    }

        return 0;
}