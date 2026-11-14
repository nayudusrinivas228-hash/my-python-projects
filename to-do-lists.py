print("Welcome To To-Do-apllication")
Tasks={print("1.Learn Python"),
       print("2.Wacthing Movies"),
       print("3.Learn SQL"),
       print("4.Learn complete Full Stack"),
       }
print(Tasks)
User=input("Please select Your Task :" )
adding="Your Task added sucessfully"
description=input("Please provide some Description about yoour Task :" )
if User=='1':
    print(adding)
    print(description)
elif User=='2':
    print(adding)
    print(description)
elif User=='3':
    print(adding)
    print(description)
elif User=='4':
    print(adding)
    print(description)
else:
    print("You chosen Invalid please chose correct one")
    

c = input("Do you want to check status (Yes/No): ")
if c.lower() == "yes":
    print("A. Mark as completed")
    print("B. Mark as pending")
    print("C. In Process")
    completed = input("Please select one status: ")
    if completed.upper() == 'A':
        print("Task Completed Successfully")
    elif completed.upper() == 'B':
        print("Your Task is Pending")
    elif completed.upper() == 'C':
        print("Your Task is In Process")
    else:
        print("Invalid Selection")

else:
    print("Thank you for using our application")


    

    

