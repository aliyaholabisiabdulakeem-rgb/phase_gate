import java.util.Scanner;

public class studentGrade {

static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int studentsNumber = getStudentsNumber();
        int subjectsNumber = getSubjectsNumber();

        int[][] scores = new int [studentsNumber][subjectsNumber];
        int[] total = new int [studentsNumber];
        int[] position = new int [studentsNumber];

        inputScores(scores, total, studentsNumber, subjectsNumber);
        calculatePosition(total, position, studentsNumber);
        displayResult(scores, total, position, studentsNumber, subjectsNumber);
    }

    
    public static int getStudentsNumber() {
        System.out.print("How many students do u have? ");
        return input.nextInt();
    }

    
    public static int getSubjectsNumber() {
        System.out.print("How many subjects do they offer? ");
        return input.nextInt();
    }

    
    public static void inputScores(int[][] scores, int[] total, int studentsNumber, int subjectsNumber) {
        for (int index = 0; index < studentsNumber; index++) {
            System.out.println("Entering score for student " + (index + 1));
            for (int count = 0; count < subjectsNumber; count++) {
                while (true) {
                    System.out.print("Enter score for each student " + (count + 1) + " : ");
                    int score = input.nextInt();
                    if (score >= 0 && score <= 100) {
                        scores[index][count] = score;
                        total[index] += score;
                        System.out.println("Saving >>>>>>>>>>>>>>>>>>>>>>>>>>>>");
                        System.out.println("Saved Successfully!!");
                        break;
                    } else {
                        System.out.println("Invalid score!, plz enter score between 0 to 100");
                    }
                }
            }
        }
    }

    
    public static void calculatePosition(int[] total, int[] position, int studentsNumber) {
        for (int index = 0; index < studentsNumber; index++) {
            position[index] = 1;
            for (int count = 0; count < studentsNumber; count++) {
                if (total[count] > total[index]) {
                    position[index]++;
                }
            }
        }
    }

   
    public static void displayResult(int[][] scores, int[] total, int[] position, int studentsNumber, int subjectsNumber) {
        System.out.println("=========================================================================");
        System.out.println("                    LAGBAJA SCHOOLS RESULT SUMMARY");
        System.out.println("=========================================================================");

        System.out.printf("%14s", "STUDENT");
        for (int count = 0; count < subjectsNumber; count++) {
            System.out.printf("%9s", "SUB" + (count + 1));
        }
        System.out.printf("%10s%10s%10s%n", "TOTAL", "AVERAGE", "POSITION");
        System.out.println("=========================================================================");

        for (int count = 0; count < studentsNumber; count++) {
            double average = (double) total[count] / subjectsNumber;
            System.out.printf("%14s", "Student " + (count + 1));
            for (int index = 0; index < subjectsNumber; index++) {
                System.out.printf("%9d", scores[count][index]);
            }
            System.out.printf("%10d%10.2f%10d%n", total[count], average, position[count]);
        }
    }
}
