//11. Write Java program to find the sum of all odd numbers in a 2D array.
import java.util.Scanner;
public class w3q11 {
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

            // Calculate and display the sum of odd numbers
            int sumOfOddNumbers = calculateSumOfOddNumbers(array);
            System.out.println("Sum of odd numbers in the 2D array: " + sumOfOddNumbers);
        }

        static int calculateSumOfOddNumbers(int[][] array) {
            int sum = 0;

            for (int i = 0; i < array.length; i++) {
                for (int j = 0; j < array[0].length; j++) {
                    if (array[i][j] % 2 != 0) {
                        sum += array[i][j];
                    }
                }
            }

            return sum;
        }
    }


