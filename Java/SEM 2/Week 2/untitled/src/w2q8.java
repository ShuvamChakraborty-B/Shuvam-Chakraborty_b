import java.util.Scanner;
public class w2q8 {




        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the lower bound of the interval: ");
            int lowerBound = scanner.nextInt();

            System.out.print("Enter the upper bound of the interval: ");
            int upperBound = scanner.nextInt();

            if (lowerBound <= upperBound) {
                System.out.println("Multiples of 10 between " + lowerBound + " and " + upperBound + ":");
                printMultiplesOf10(lowerBound, upperBound);
            } else {
                System.out.println("Invalid interval. Please ensure the lower bound is less than or equal to the upper bound.");
            }
        }

        static void printMultiplesOf10(int lowerBound, int upperBound) {
            for (int i = lowerBound; i <= upperBound; i++) {
                if (i % 10 == 0) {
                    System.out.print(i + " ");
                }
            }
            System.out.println(); // Move to the next line after printing multiples
        }
    }









