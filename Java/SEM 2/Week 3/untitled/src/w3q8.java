//8. Write a Java program to find the sum of diagonal elements in a 2D array.
import java.util.Scanner;
public class w3q8 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the dimensions of the array
            System.out.print("Enter the number of rows for the 2D array: ");
            int rows = scanner.nextInt();

            System.out.print("Enter the number of columns for the 2D array: ");
            int columns = scanner.nextInt();

            // Create the 2D array
            int[][] array = new int[rows][columns];

            // Read elements of the 2D array
            System.out.println("Enter elements for the 2D array:");
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    System.out.print("Enter element at position [" + i + "][" + j + "]: ");
                    array[i][j] = scanner.nextInt();
                }
            }

            // Calculate and display the sum of diagonal elements
            int sumOfDiagonal = calculateSumOfDiagonal(array);
            System.out.println("Sum of diagonal elements in the 2D array: " + sumOfDiagonal);
        }

        static int calculateSumOfDiagonal(int[][] array) {
            int sum = 0;
            int rows = array.length;
            int columns = array[0].length;

            // Ensure the array is a square matrix (number of rows = number of columns)
            if (rows == columns) {
                for (int i = 0; i < rows; i++) {
                    sum += array[i][i]; // Add the diagonal element at position [i][i]
                }
            } else {
                System.out.println("Cannot calculate diagonal sum. The array is not a square matrix.");
            }

            return sum;
        }
    }



