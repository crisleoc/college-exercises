// function that given a number n, prints the pascal triangle asociated with n
// for example, if n = 3, the output should be:
// 1
// 1 1
// 1 2 1
// 1 3 3 1

#include <iostream>

using namespace std;

void printPascalTriangle(int n)
{
    int row = 0;
    int col = 0;
    int num = 0;
    int **triangle = new int *[n];
    for (int i = 0; i <= n; i++)
    {
        triangle[i] = new int[i + 1];
    }
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            if (j == 0 || j == i)
            {
                triangle[i][j] = 1;
            }
            else
            {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
    }
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            cout << triangle[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int n;
    cin >> n;
    printPascalTriangle(n);
    return 0;
}