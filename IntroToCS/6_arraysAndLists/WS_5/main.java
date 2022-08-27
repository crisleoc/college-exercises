import java.util.Scanner;

// function that given a number n, prints the pascal triangle asociated with n
// for example, if n = 3, the output should be:
// 1
// 1 1
// 1 2 1
// 1 3 3 1
class Main {
    public static void Main(String[] args) {
        int n = 3;
        printPascalTriangle(n);
    }

    public static void printPascalTriangle(int n) {
        int[][] triangle = new int[n][];
        for (int i = 0; i < n; i++) {
            triangle[i] = new int[i + 1];
            triangle[i][0] = 1;
            triangle[i][i] = 1;
            for (int j = 1; j < i; j++) {
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(triangle[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        printPascalTriangle(n);
    }
}