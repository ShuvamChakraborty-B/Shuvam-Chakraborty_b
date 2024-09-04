//4. Write a Java program to calculate Sum of two 2-dimensional arrays.
import java.util.Scanner;
public class w3q4 {




        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the dimensions of the arrays
            System.out.print("Enter the number of rows for the arrays: ");
            int rows = scanner.nextInt();

            System.out.print("Enter the number of columns for the arrays: ");
            int columns = scanner.nextInt();

            // Create the first array
            int[][] array1 = new int[rows][columns];
            System.out.println("Enter elements for the first array:");
            readArrayElements(scanner, array1);

            // Create the second array
            int[][] array2 = new int[rows][columns];
            System.out.println("Enter elements for the second array:");
            readArrayElements(scanner, array2);

            // Calculate the sum of the arrays
            int[][] sumArray = calculateSum(array1, array2);

            // Display the sum of the arrays
            System.out.println("Sum of the two arrays:");
            displayArray(sumArray);
        }

        static void readArrayElements(Scanner scanner, int[][] array) {
            for (int i = 0; i < array.length; i++) {
                for (int j = 0; j < array[0].length; j++) {
                    System.out.print("Enter element at position [" + i + "][" + j + "]: ");
                    array[i][j] = scanner.nextInt();
                }
            }
        }

        static int[][] calculateSum(int[][] array1, int[][] array2) {
            int rows = array1.length;
            int columns = array1[0].length;
            int[][] sumArray = new int[rows][columns];

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    sumArray[i][j] = array1[i][j] + array2[i][j];
                }
            }

            return sumArray;
        }

        static void displayArray(int[][] array) {
            for (int i = 0; i < array.length; i++) {
                for (int j = 0; j < array[0].length; j++) {
                    System.out.print(array[i][j] + " ");
                }
                System.out.println();
            }
        }
    }


