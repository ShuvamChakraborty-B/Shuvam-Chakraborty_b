import java.util.Scanner;
public class w2q13 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the base number: ");
            double base = scanner.nextDouble();

            System.out.print("Enter the exponent: ");
            int exponent = scanner.nextInt();

            double result = calculateExponential(base, exponent);

            System.out.println(base + " raised to the power of " + exponent + " is: " + result);
        }

        static double calculateExponential(double base, int exponent) {
            double result = 1;

            if (exponent < 0) {
                base = 1 / base;
                exponent = -exponent;
            }

            for (int i = 0; i < exponent; i++) {
                result *= base;
            }

            return result;
        }
    }



