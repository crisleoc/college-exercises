import java.util.Scanner;

public class Main {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_YELLOW = "\u001B[33m";

    public static double GetDouble(String description) {
        while (true) {
            try {
                Scanner input = new Scanner(System.in);
                System.out.println(ANSI_YELLOW + "Ingrese el valor de " + description + ":" + ANSI_RESET);
                double value = Double.parseDouble(input.nextLine());
                return value;
            } catch (Exception e) {
                // TODO: handle exception
                System.out.println(ANSI_RED + "Caracter invalido -" + e.getMessage() + ANSI_RESET);
            }
        }
    }

    public static boolean PointInCircumference() {
        double x1 = GetDouble("x1");
        double y1 = GetDouble("y1");
        double r = GetDouble("r");
        double x2 = GetDouble("x2");
        double y2 = GetDouble("y2");

        double ResultOp = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

        if (ResultOp <= r)
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        if (PointInCircumference())
            System.out.println("yes");
        else
            System.out.println("no");
    }
}
