//7. Write a Java program to calculate the sum of natural numbers up to a certain range.
import java.util.Scanner;
public class w2q7 {




        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the range (positive integer): ");
            int range = scanner.nextInt();

            if (range < 0) {
                System.out.println("Please enter a positive integer for the range.");
            } else {
                int sum = calculateSum(range);
                System.out.println("Sum of natural numbers up to " + range + " is: " + sum);
            }
        }

        static int calculateSum(int n) {
            return (n * (n + 1)) / 2;
        }
    }


