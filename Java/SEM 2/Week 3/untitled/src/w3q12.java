//12. Write a Java program to print transpose of matrix.
import java.util.Scanner;
public class w3q12 {
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);

            // Read the dimensions of the matrix
            System.out.print("Enter the number of rows for the matrix: ");
            int rows = scanner.nextInt();

            System.out.print("Enter the number of columns for the matrix: ");
            int columns = scanner.nextInt();

            // Create the matrix
            int[][] matrix = new int[rows][columns];

            // Read elements of the matrix
            System.out.println("Enter elements for the matrix:");
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    System.out.print("Enter element at position [" + i + "][" + j + "]: ");
                    matrix[i][j] = scanner.nextInt();
                }
            }

            // Print the original matrix
            System.out.println("Original Matrix:");
            displayMatrix(matrix);

            // Calculate and print the transpose of the matrix
            int[][] transposeMatrix = calculateTranspose(matrix);
            System.out.println("Transpose Matrix:");
            displayMatrix(transposeMatrix);
        }

        static int[][] calculateTranspose(int[][] matrix) {
            int rows = matrix.length;
            int columns = matrix[0].length;

            int[][] transpose = new int[columns][rows];

            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    transpose[j][i] = matrix[i][j];
                }
            }

            return transpose;
        }

        static void displayMatrix(int[][] matrix) {
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    System.out.print(matrix[i][j] + " ");
                }
                System.out.println();
            }
        }
    }


