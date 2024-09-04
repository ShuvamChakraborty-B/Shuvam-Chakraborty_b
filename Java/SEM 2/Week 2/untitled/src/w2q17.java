/*18. Write a program to compute the value of Euler’s number that is used as the base of natural logarithms. Use the following formula.
e= 1+ 1/1! +1 /2! + 1/3+................ 1/n!*/
import java.util.Scanner;

public class w2q17 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the number of terms (n) to calculate e: ");
            int n = scanner.nextInt();

            double eulerNumber = calculateEulerNumber(n);

            System.out.println("The value of Euler's number (e) is approximately: " + eulerNumber);
        }

        static double calculateEulerNumber(int n) {
            double eulerNumber = 1.0;
            double factorial = 1.0;

            for (int i = 1; i <= n; i++) {
                factorial *= i;
                eulerNumber += 1.0 / factorial;
            }

            return eulerNumber;
        }
    }


