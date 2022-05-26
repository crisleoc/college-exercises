import java.util.Scanner;

public class Main {

    public static double get_double(String name) {
        Scanner input = new Scanner(System.in);
        while (true) {
            try {
                System.out.print("Enter value of " + name + ": ");
                double value = Double.parseDouble(input.nextLine());
                return value;
            } catch (NumberFormatException nfe) {
                System.out.print("Wrong input,enter again");
            }
        }
    }

    public static void main(String[] args) {
        double a = get_double("a");
        double b = get_double("b");
        while (a > -0.000001) {
            a = ((a + b) / 2) / 2;
            b /= 2;
            System.out.println(a);
        }
    }
}
