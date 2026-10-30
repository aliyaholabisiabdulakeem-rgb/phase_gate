const userInput = require("prompt-sync")()

studentsNumber = userInput("How many students do u have? ");

subjectsNumber = userInput("How many subjects do they offer? ");

console.log("Saving >>>>>>>>>>>>>>>>>>>>>>>");



    let[][] scores = new int[studentsNumber][subjectsNumber];
    let[] total = new int[studentsNumber];
    let[] position = new int[studentsNumber];

        for(let index = 0; index < studentsNumber; index++){
            console.log("Entering score for students " + (index + 1));
            for(let count = 0; count < subjectsNumber; count++){
                while(true){
                console.log("Enter score for each students: " + (count + 1));
                    let score = input.nextInt();
                if(score >= 0 && score <= 100){
                    scores[index][count] = score;
                    total[index ] += score;
                console.log("Saved Successfuly!!");
                        break;
                }
                else{
                console.log("Invalid score!, plz enter score between 0 to 100");        
                }
}       
}
}
        for(let index = 0; index < studentsNumber; index++){
            position[index] = 1;
            for(let count = 0; count < studentsNumber; count++){
                if(total[count] > total[index]){
                    position[index]++;
}
}
}

console.log("\n===============================================================");

console.log("\n          LAGBAJA SCHOOLS RESULT SUMMARY");

console.log("\n===============================================================");

console.log("%-14s", "STUDENT");

    for(let count = 0; count < studentsNumber; count++){
        System.out.printf("%9s", "SUB " + (count + 1));
}
System.out.printf("%11s%11s%10s%n" , "TOTAL", "AVERAGE", "POSITION");

console.log("\n===============================================================");


        for(let count = 0; count < studentsNumber; count++){
            let float(Average) = total[count] / subjectsNumber;
            System.out.printf("%-14s", "Student" + (count + 1));
        for(let index = 0; index < subjectsNumber; index++){
            System.out.printf("%9d", scores[count][index]);
}
        System.out.printf("%11d%11.2f%9d%n",
             total[count], Average, position[count]);
}
}
}

