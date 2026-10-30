import java.util.Scanner;
public class studentGrade{
public static void main(String[] args){
    Scanner input = new Scanner(System.in);

System.out.print("How many students do u have? ");
    int studentsNumber = input.nextInt();

System.out.print("How many subjects do they offer? ");
    int  subjectsNumber = input.nextInt();
System.out.println("Saving >>>>>>>>>>>>>>>>>>>>>>>");



    int[][] scores = new int[studentsNumber][subjectsNumber];
    int[] total = new int[studentsNumber];
    int[] position = new int[studentsNumber];

        for(int index = 0; index < studentsNumber; index++){
            System.out.println("Entering score for students " + (index + 1));
            for(int count = 0; count < subjectsNumber; count++){
                while(true){
                System.out.print("Enter score for each students: " + (count + 1));
                    int score = input.nextInt();
                if(score >= 0 && score <= 100){
                    scores[index][count] = score;
                    total[index ] += score;
                System.out.println("Saved Successfuly!!");
                        break;
                }
                else{
                System.out.println("Invalid score!, plz enter score between 0 to 100");        
                }
}       
}
}
        for(int index = 0; index < studentsNumber; index++){
            position[index] = 1;
            for(int count = 0; count < studentsNumber; count++){
                if(total[count] > total[index]){
                    position[index]++;
}
}
}

System.out.println("===============================================================");

System.out.println("          LAGBAJA SCHOOLS RESULT SUMMARY");

System.out.println("===============================================================");

System.out.printf("%-14s", "STUDENT");

    for(int count = 0; count < studentsNumber; count++){
        System.out.printf("%9s", "SUB " + (count + 1));
}
System.out.printf("%11s%11s%10s%n" , "TOTAL", "AVERAGE", "POSITION");

System.out.println("===============================================================");


        for(int count = 0; count < studentsNumber; count++){
            double Average = total[count] / subjectsNumber;
            System.out.printf("%-14s", "Student" + (count + 1));
        for(int index = 0; index < subjectsNumber; index++){
            System.out.printf("%9d", scores[count][index]);
}
        System.out.printf("%11d%11.2f%9d%n",
             total[count], Average, position[count]);
}
}
}

