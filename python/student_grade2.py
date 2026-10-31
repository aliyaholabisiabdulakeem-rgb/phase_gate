def get_students_numbers():
    students_number = int(input("How many students do u have? "))
    return students_number

def get_subjects_numbers():
    subjects_number = int(input("How many subjects do they offer? "))
    return subjects_number

def input_score(scores, total, students_number, subjects_number):
    for index in range(students_number):
        print("\nEntering score for student " , (index + 1))
        for count in range(students_number):
            while True:
                score = int(input("Enter score for each students: "))
                score += count + 1  
                if score >= 0 and score <= 100:
                    scores[index][count] = score
                    total[index] += score
                    print("\nSaving >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                    print("\nSaved Successfully!!")
                    break
                else: 
                    print("\nInvalid score!, plz enter score between 0 to 100")

def calculate_position(total, position, students_number):
    for index in range(students_number):
        position[index] = 1
        for count in range(students_number):
            if total[count] > total[index]:
                position[index] += 1

def displayResult(scores, total, position, students_number, subjects_number):
    print("\n=========================================================================")
    print("\n                    LAGBAJA SCHOOLS RESULT SUMMARY")
    print("\n=========================================================================")

    print("STUDENT", end = "\t")
    for count in range(subjects_number):
        print("SUB" , (count + 1), end = "\t")
    
    print("TOTAL", "\t", "AVERAGE","\t", "POSITION");
    print("\n=========================================================================")

    for count in range(students_number):
        average = total[count] / subjects_number
        print("Student " , (count + 1), end = "\t")
        for index in range(subjects_number):
            print(scores[count][index], end = "\t")
        
        print(total[count], "\t", average, "\t", position[count])

    
students_number = get_students_numbers()
subjects_number = get_subjects_numbers()

scores = [[0] * students_number for index in range(students_number)]

total = [0] * students_number

position = [0] * students_number

input_score(scores, total, students_number, subjects_number)
calculate_position(total, position, students_number)
displayResult(scores, total, position, students_number, subjects_number)



















              
