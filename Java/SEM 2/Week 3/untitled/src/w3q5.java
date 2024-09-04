//5. Write a Java program to find the range of a 1D array.
import java.util.Scanner;

public class w3q5 {



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

            // Find and display the range of the array
            int range = findArrayRange(array);
            System.out.println("The range of the array is: " + range);
        }

        static int findArrayRange(int[] array) {
            if (array.length == 0) {
                System.out.println("Array is empty. Cannot find range.");
                return 0;
            }

            int min = array[0];
            int max = array[0];

            // Find minimum and maximum values in the array
            for (int i = 1; i < array.length; i++) {
                if (array[i] < min) {
                    min = array[i];
                } else if (array[i] > max) {
                    max = array[i];
                }
            }

            // Calculate and return the range
            return max - min;
        }
    }


