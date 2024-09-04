//13. Write a Java program to check whether a given matrix is sparse or not.
import java.util.Scanner;
public class w3q13 {
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

            // Check if the matrix is sparse and display the result
            boolean isSparse = checkSparseMatrix(matrix);
            if (isSparse) {
                System.out.println("The matrix is sparse.");
            } else {
                System.out.println("The matrix is not sparse.");
            }
        }

        static boolean checkSparseMatrix(int[][] matrix) {
            int totalElements = matrix.length * matrix[0].length;
            int zeroCount = 0;

            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    if (matrix[i][j] == 0) {
                        zeroCount++;
                    }
                }
            }

            // If more than half of the elements are zero, consider it as a sparse matrix
            return zeroCount > (totalElements / 2);
        }
    }


