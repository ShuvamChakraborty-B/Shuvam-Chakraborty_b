/*5. Admission to a professional course is subject to the following conditions:
        (a) marks in Mathematics >= 60 (b) marks in Physics >=50
        (c) marks in Chemistry >=40 (d) Total in all 3 subjects >=200
        (Or)
        Total in Maths & Physics>=150
        Given the marks in the 3 subjects of n (user input) students, write a program to process the applications to list the eligible candidates.*/
import java.util.Scanner;
public class w2q5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of students: ");
        int n = scanner.nextInt();

        int[][] marks = new int[n][3]; // Assuming 3 subjects: Math, Physics, Chemistry

        // Input marks for each student
        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter marks for student " + (i + 1) + ":");
            System.out.print("Mathematics: ");
            marks[i][0] = scanner.nextInt();
            System.out.print("Physics: ");
            marks[i][1] = scanner.nextInt();
            System.out.print("Chemistry: ");
            marks[i][2] = scanner.nextInt();
        }

        // Process applications and list eligible candidates
        System.out.println("\nList of eligible candidates:");

        for (int i = 0; i < n; i++) {
            if (isEligible(marks[i])) {
                System.out.println("Student " + (i + 1));
            }
        }
    }

    static boolean isEligible(int[] studentMarks) {
        int mathMarks = studentMarks[0];
        int physicsMarks = studentMarks[1];
        int chemistryMarks = studentMarks[2];

        return (mathMarks >= 60 && physicsMarks >= 50 && chemistryMarks >= 40 &&
                mathMarks + physicsMarks + chemistryMarks >= 200) ||
                (mathMarks + physicsMarks >= 150);
    }
}





