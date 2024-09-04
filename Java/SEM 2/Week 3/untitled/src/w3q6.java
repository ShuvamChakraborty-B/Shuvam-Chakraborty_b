//6. Write a Java program to search an element in an array.
import java.util.Scanner;
public class w3q6 {
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

            // Read the element to search
            System.out.print("Enter the element to search: ");
            int elementToSearch = scanner.nextInt();

            // Search for the element and display the result
            int position = searchElement(array, elementToSearch);
            if (position != -1) {
                System.out.println("Element found at position: " + position);
            } else {
                System.out.println("Element not found in the array.");
            }
        }

        static int searchElement(int[] array, int target) {
            for (int i = 0; i < array.length; i++) {
                if (array[i] == target) {
                    return i; // Return the position if the element is found
                }
            }
            return -1; // Return -1 if the element is not found
        }
    }

