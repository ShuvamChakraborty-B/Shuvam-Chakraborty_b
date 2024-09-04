//10. Write a Java program to enter n elements in an array and find smallest number among them.
import java.util.Scanner;

public class w3q10 {
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

            // Find and display the smallest number in the array
            int smallestNumber = findSmallestNumber(array);
            System.out.println("The smallest number in the array is: " + smallestNumber);
        }

        static int findSmallestNumber(int[] array) {
            if (array.length == 0) {
                System.out.println("Array is empty. Cannot find the smallest number.");
                return 0;
            }

            int smallest = array[0];

            for (int i = 1; i < array.length; i++) {
                if (array[i] < smallest) {
                    smallest = array[i];
                }
            }

            return smallest;
        }
    }


