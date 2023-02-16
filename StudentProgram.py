import StudentClass as sc


# Get the starting balance.
name = input("name: ")
stu_id = input("What is your student id? ")
dob = input("What is your DOB? ")
classification = input("Classification: ")

# Create a BankAccount object.
student1 = sc.Student(name, stu_id, dob, classification)

# Display the balance.
# print("Age of student: ", format(savings.get_balance(), ",.2f"), sep="")

student1.calc_age()
student1.calc_registration()

print(f"Student age is: {student1.get_age()}")
print(f"Student can register between {student1.get_registration()}")


# Call the main function.
