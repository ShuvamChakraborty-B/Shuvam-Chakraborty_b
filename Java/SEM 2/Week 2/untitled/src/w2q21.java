import java.util.Scanner;
public class w2q21 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the lower and upper limits of the interval
            System.out.print("Enter the lower limit of the interval: ");
            int lowerLimit = scanner.nextInt();

            System.out.print("Enter the upper limit of the interval: ");
            int upperLimit = scanner.nextInt();

            System.out.println("Prime numbers between " + lowerLimit + " and " + upperLimit + ":");
            displayPrimes(lowerLimit, upperLimit);
        }

        static void displayPrimes(int lowerLimit, int upperLimit) {
            for (int number = lowerLimit; number <= upperLimit; number++) {
                if (isPrime(number)) {
                    System.out.print(number + " ");
                }
            }
        }

        static boolean isPrime(int number) {
            if (number <= 1) {
                return false;
            }

            for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    return false;
                }
            }

            return true;
        }
    }


