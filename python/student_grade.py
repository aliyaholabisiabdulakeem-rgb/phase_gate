student_number = int(input("How many students do u have? "))
subject_number = int(input("How many subjects do they offer? "))

scores = [[0] * subject_number for _ in range(student_number)]
total = [0] * student_number
position = [0] * student_number

for index in range(student_number):
    print("Entering score for students " , (index + 1))

for count in range(subject_number):
    while True:
        score = int(input("Enter score for each students: "))
        score += count + 1
        if score >= 0 and score <= 78:
            scores[index][count] = score
            total[index ] += score
            print("Saving >>>>>>>>>>>>>>>>>>>>>>>")
            print("Saved Successfuly!!")
            break;
                
        else:
            print("Invalid score!, plz enter score between 0 to 100")


for index in range(student_number):
    position[index] = 1;
    for count in range(student_number):
        if total[count] > total[index]:
            position[index] += 1

print("\n===============================================================")

print("\n          LAGBAJA SCHOOLS RESULT SUMMARY")

print("\n===============================================================")

print("STUDENT", "\t")

for count in range(student_number):
    print("SUB " , (count + 1))

print("TOTAL", "\t", "AVERAGE", "\t", "POSITION")

for count in range(student_number):
    Average = total[count] / subject_number
    print("Student" , (count + 1))
    for index in range(subject_number):
        print(scores[count][index])
        print(total[count], "\t", Average, "\t", position[count])    

print("\n===============================================================")
           
