import java.util.Scanner;
public class w2q22 {




        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the number from the user
            System.out.print("Enter a number: ");
            int number = scanner.nextInt();

            // Check if the number is Armstrong
            if (isArmstrongNumber(number)) {
                System.out.println(number + " is an Armstrong number.");
            } else {
                System.out.println(number + " is not an Armstrong number.");
            }
        }

        static boolean isArmstrongNumber(int number) {
            int originalNumber = number;
            int numberOfDigits = countDigits(number);
            int sum = 0;

            while (number > 0) {
                int digit = number % 10;
                sum += Math.pow(digit, numberOfDigits);
                number /= 10;
            }

            return sum == originalNumber;
        }

        static int countDigits(int number) {
            int count = 0;
            while (number != 0) {
                number /= 10;
                count++;
            }
            return count;
        }
    }


