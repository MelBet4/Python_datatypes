#Write a program that uses a dictionary to store a 
#student’s info: name, age, and grade.
#Ask the user for input and store the values.
#Then ask the user if they want to update one of
#the fields (e.g., change grade).
#Print the updated dictionary.

#empty dictionary
student = {}

#ask for user's input
student["Name"] = input("Enter your name: ").title()
student["Age"] = input("Enter your age: ")
student["Grade"] = input("Enter your grade: ")
print("\nStudent info: ", student)

#ask if user wants to update
choice = input("\nDo you want to update any field? (yes/no): ").lower()

if choice == "yes":
    field = input("Which field do you want to update (Name/Age/Grade)? ").title()
    if field in student:
        new_value = input(f"Enter new value for {field}: ")
        student[field] = new_value
    else:
        print("Invalid field!")

print("\nUpdated student info: ", student)

#Write a program that uses a dictionary to store 
#information about a book: title, author, and year published.
#Ask the user for input and store the values.
#Print the dictionary.
#Then ask the user if they want to update 
#one of the fields (e.g., change the year).
#Print the updated dictionary.

#empty dictionary
book = {}

#ask user for book details
book["Title"] = input("Enter book title: ").title()
book["Author"] = input("Enter the author's name: ").title()
book["Year"] = input("Enter the year of publication: ")

print(f"\nBook details: {book}")

#ask user if they want to make an update
updateChoice = input("\nDo you want to update any field (yes/no)? ").lower()

if updateChoice == "yes":
    bookField = input("\nWhich book field do you want to update (Title/Author/Year)? ")
    if bookField in book:
        updatedValue = input(f"Enter the value for {bookField}: ").title()
        book[bookField] = updatedValue
    else:
        print("Invalid field!")

print(f"\nUpdated book info: {book}")

