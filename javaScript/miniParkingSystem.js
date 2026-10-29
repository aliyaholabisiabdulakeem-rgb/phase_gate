const userInput = require("prompt-sync")();
let menuChoice = console.log(`

======PARKING SYSTEM======

1. enter a parking space.
2. enter your name.
3. Check available spaces.
4. Exit.
`)


menuChoice = userInput("plz kindly enter a menu choice: ")

    if(menuChoice = 1){
        let parkingSpace = userInput("plz kindly enter a parking space: ")
//        let new_list = [0] * 20
//        for(count in new_list){
//            if(new_list[user_input] > 1){
//                new_list[user_input] = '1'
//}
//}
}
//        console.log(new_list[user_input])
//
    else if(menuChoice = 2){

        let Name = userInput("plz kindly enter your name: ")
}
        console.lg(name)
    else if(menuChoice = 3){

        let availableSpaces = userInput("check available spaces: ")

        let new_list = [0] * 20

        console.log("Available parking spaces are : " ,new_list)
}
    else{

        console.log("Exiting...., Goodbye!! 🤩️")    
}            
       
