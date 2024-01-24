import java.util.Scanner;

public class first {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the number of rows from the user
        System.out.print("Enter the number of rows: ");
        int numRows = scanner.nextInt();

        // Call the method to print the star pattern
        printStarPattern(numRows);
    }

    // Method to print the star pattern
    static void printStarPattern(int rows) {
        for (int i = 1; i <= rows; i++) {
            // Print spaces before the stars
            for (int j = 1; j <= rows - i; j++) {
                System.out.print(" ");
            }

            // Print '*' characters
            for (int k = 1; k <= i; k++) {
                System.out.print("* ");
            }

            // Move to the next line after printing each row
            System.out.println();
        }
    }
}
