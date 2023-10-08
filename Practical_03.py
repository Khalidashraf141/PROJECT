'''WAP to accept a number from the user and display whether
 it is an even number or odd number. (Practical_03)'''
while True:
    try:
        user_input = int(input("Enter your number====> "))
        
        if user_input < 0:
            print(f"{user_input} = Please enter a positive number")

        elif user_input % 2 == 0:
            print(f"{user_input} = This is an even number")

        else:
            print(f"{user_input} = This is an odd number")
        
        break  
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

