//9. Reverse the elements in an array of integers without using a second array
import java.util.Scanner;
public class w3q9 {
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

            // Reverse the array in-place
            reverseArrayInPlace(array);

            // Display the reversed array
            System.out.println("Reversed array:");
            displayArray(array);
        }

        static void reverseArrayInPlace(int[] array) {
            int start = 0;
            int end = array.length - 1;

            while (start < end) {
                // Swap elements at start and end positions
                int temp = array[start];
                array[start] = array[end];
                array[end] = temp;

                // Move to the next pair of elements
                start++;
                end--;
            }
        }

        static void displayArray(int[] array) {
            for (int num : array) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }


