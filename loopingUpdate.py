#empty dictionary
book = {}

#ask the user for book details
book["Title"] = input("Enter book title: ").title()
book["Author"] = input("Enter the author's name: ").title()
book["Year"] = input("Enter the year if publication: ")

print(f"\nBook details: {book}")

#loop for updates
while True:
    updateChoice = input("\nDo you want to update a field? (yes/done): ")

    if updateChoice == "done":
        break
    elif updateChoice == "yes":
        bookField = input("Which field do you want to update (Title/Author/Year)? ").title()
        if bookField in book:
            newValue = input(f"Enter the value for {bookField}: ").title()
            book[bookField] = newValue
            print("Updated book info: ", book)
        else:
            print("Invalid field!")
    else:
        print("Please type 'yes' to update or 'done' to finish.")

print(f"\nFinal book info: {book}")
