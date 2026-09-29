import os
filename = "Python_journal.txt"
while True:
    print("Welcome to Personal Journal Manager!")
    print("Please select an option:\n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")
    choice = input("\nUser Input:\n")
    if choice == "1":
        entry = input("\nEnter your journal entry:\n")
        file = open(filename, "a")
        file.write(entry + "\n\n")
        file.close()
        print("\nEntry added successfully!")
    elif choice == "2":
        if not os.path.exists(filename):
            print("\nError: The journal file does not exist. Please add a new entry first.")
        else:
            file = open(filename, "r")
            content = file.read()
            file.close()       
            if content == "":
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("-------------------------")
                print(content)
    elif choice == "3":
        if not os.path.exists(filename):
            print("\nError: The journal file does not exist. Please add a new entry first.")
        else:
            keyword = input("\nEnter a keyword or date to search: ")
            file = open(filename, "r")
            content = file.read()
            file.close()           
            if keyword in content:
                print("\nMatching Entries:")
                print("-------------------------")
                print(content)
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")
    elif choice == "4":
        if not os.path.exists(filename):
            print("\nNo journal entries to delete.")
        else:
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
            if confirm == "yes":
                os.remove(filename)
                print("\nAll journal entries have been deleted.")
    elif choice == "5":
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break
    else:
        print("\nInvalid option. Please select a valid option from the menu.")       
    print("\n" + "="*40 + "\n")