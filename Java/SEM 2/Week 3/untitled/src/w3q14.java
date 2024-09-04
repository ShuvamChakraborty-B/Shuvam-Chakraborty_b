//14. Write a Java program to count the prime numbers in an array.
import java.util.Scanner;
public class w3q14 {




        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the size of the array
            System.out.print("Enter the size of the array: ");
            int size = scanner.nextInt();

            // Create the array
            int[] array = new int[size];

            // Read elements of the array
            System.out.println("Enter the elements of the array:");
            for (int i = 0; i < size; i++) {
                System.out.print("Enter element at position " + i + ": ");
                array[i] = scanner.nextInt();
            }

            // Count and display the number of prime numbers in the array
            int primeCount = countPrimeNumbers(array);
            System.out.println("Number of prime numbers in the array: " + primeCount);
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

        static int countPrimeNumbers(int[] array) {
            int count = 0;

            for (int num : array) {
                if (isPrime(num)) {
                    count++;
                }
            }

            return count;
        }
    }


