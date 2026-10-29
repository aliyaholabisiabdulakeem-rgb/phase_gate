def parking_system():
    print ("""
    ======PARKING SYSTEM======

    1. enter a parking space.
    2. enter your name.
    3. Check available spaces.
    4. Exit.
    """)

menu_choice = int(input("plz kindly enter a menu choice: "))
match menu_choice:
    case 1: 
        user_input = print(input("plz kindly enter a parking space: "))
#        new_list = [0] * 20
#        for count in new_list:
#            if new_list[user_input] > 1:
#                new_list[user_input] = '1'
#        print(new_list[user_input])

    case 2:
        print(input("plz kindly enter your name: "))

    case 3:
        print("check available spaces: ")

        new_list = [0] * 20
        print("Available parking spaces are : " ,new_list)

    case 4:
            print("Exiting...., Goodbye!! 🤩️")    
    
    case _:
            print("Invalid")
            
parking_system()            
     
