const prompt = require('prompt-sync')();

function getStudentsNumber() {
    let n = Number(prompt("How many students? "));
    return n;
}


function getSubjectsNumber() {
    let n = Number(prompt("How many subjects? "));
    return n;
}


function inputScores(scores, total, studentsNumber, subjectsNumber) {
    for (let count = 0; count < studentsNumber; count++) {
        for (let index = 0; index < subjectsNumber; index++) {
            let score = Number(prompt("Enter score for student " + (count+1) + " subject " + (index+1) + ": "));

            while (score < 0 || score > 100) {
                console.log("Invalid score");
                score = Number(prompt("Enter score for student " + (count+1) + " subject " + (index+1) + ": "));

            }

            scores[count][index] = score;
            total[count] = total[count] + score;
        }
    }
}


function calculatePosition(total, position, studentsNumber) {
    for (let i = 0; i < studentsNumber; i++) {
        position[i] = 1;
        for (let j = 0; j < studentsNumber; j++) {
            if (total[j] > total[i]) {
                position[i] = position[i] + 1;
            }
        }
    }
}


function displayResult(scores, total, position, studentsNumber, subjectsNumber) {
    console.log("\n===============================================================")

    console.log("\n          LAGBAJA SCHOOLS RESULT SUMMARY")

    console.log("=================================================================");
    let header = "STUDENT\t";
    for (let count = 0; count < subjectsNumber; count++) {
        header = header + "SUB" + (count + 1) + "\t";
    }
    header = header + "TOTAL\tAVERAGE\tPOSITION";
    console.log(header);

    for (let count = 0; count < studentsNumber; count++) {

        let average = total[count] / subjectsNumber; 

        let inner = "Student " + (count+1) + "\t";

        for (let index = 0; index < subjectsNumber; index++) {

            inner = inner + scores[count][index] + "\t";
        }
        inner = inner + total[count] + "\t" + average + "\t" + position[count];

        console.log(inner);
    }
}

let studentsNumber = getStudentsNumber();
let subjectsNumber = getSubjectsNumber();
let scores = [];
let total = [];
let position = [];
for (let index = 0; index < studentsNumber; index++) {
    scores[index] = [];
    for (let count = 0; count < subjectsNumber; count++) {
        scores[index][count] = 0;
    }
    total[index] = 0;
    position[index] = 0;
}


inputScores(scores, total, studentsNumber, subjectsNumber);
calculatePosition(total, position, studentsNumber);
displayResult(scores, total, position, studentsNumber, subjectsNumber);

