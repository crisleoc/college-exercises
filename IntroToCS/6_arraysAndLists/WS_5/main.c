// program that given a number n, print Pascal's triangle associated with that number
// if n is 3, the output should be:
// 1
// 1 1
// 1 2 1
// 1 3 3 1

void main()
{
    int n, i, j, k;
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j <= i; j++)
        {
            for (k = 0; k < j; k++)
            {
                printf("%d ", 1);
            }
            printf("%d ", i + 1);
            for (k = 0; k < i - j; k++)
            {
                printf("%d ", 1);
            }
            printf("\n");
        }
    }
}
