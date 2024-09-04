//12. Write a Java program to count the number of digits of an integer.
import java.util.Scanner;
public class w2q12 {



        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter an integer: ");
            long number = scanner.nextLong();

            // Convert the number to a positive value
            long positiveNumber = Math.abs(number);

            // Initialize digit count to 0
            int digitCount = 0;

            // Count the digits using a loop
            do {
                positiveNumber /= 10;
                digitCount++;
            } while (positiveNumber > 0);

            System.out.println("Number of digits in " + number + " is: " + digitCount);
        }
    }


