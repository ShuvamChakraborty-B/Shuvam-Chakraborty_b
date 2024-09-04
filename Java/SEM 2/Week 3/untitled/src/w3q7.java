//7. Write a Java program to find the sum of even numbers in an integer array.
import java.util.Scanner;
public class w3q7 {
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

            // Calculate and display the sum of even numbers in the array
            int sumOfEvenNumbers = calculateSumOfEvenNumbers(array);
            System.out.println("Sum of even numbers in the array: " + sumOfEvenNumbers);
        }

        static int calculateSumOfEvenNumbers(int[] array) {
            int sum = 0;
            for (int num : array) {
                if (num % 2 == 0) {
                    sum += num;
                }
            }
            return sum;
        }
    }


