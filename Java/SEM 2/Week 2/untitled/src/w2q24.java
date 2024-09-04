public class w2q24 {

        public static void main(String[] args) {
            int rows = 4;

            for (int i = 1; i <= rows; i++) {
                int count = i;

                // Print spaces
                for (int space = 1; space <= rows - i; space++) {
                    System.out.print("   ");
                }

                // Print decreasing numbers
                for (int j = 1; j <= i; j++) {
                    System.out.print(count + "  ");
                    count--;
                }

                // Print increasing numbers
                for (int k = 2; k <= i; k++) {
                    System.out.print(k + "  ");
                }

                System.out.println();
            }
        }
    }


