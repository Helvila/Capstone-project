# Initialize list for journal entries
journal_entries = []

# Function to display the main menu
def display_menu():
    print("\nMenu:")
    print("1. Display Journal Entries")
    print("2. Add Journal Entry")
    print("3. Edit Journal Entry")
    print("4. Delete Journal Entry")
    print("5. Search Journal Entry")
    print("6. Exit")

# Function to display journal entries
def display_journal_entries(filter_by_category=False):
    if not journal_entries:
        print("No journal entries available.")
    else:
        print("Journal Entries:")
        if not filter_by_category:
            for index, entry in enumerate(journal_entries):
                print(f"{index + 1}. Date: {entry['date']}, Category: {entry['category']}, Content: {entry['content']}")
        else:
            category = input("Enter category: ")
            filtered_entries = [entry for entry in journal_entries if entry['category'].lower() == category.lower()]
            if not filtered_entries:
                print(f"No entries found with category '{category}'.")
            else:
                print(f"Entries with category '{category}':")
                for index, entry in enumerate(filtered_entries):
                    print(f"{index + 1}. Date: {entry['date']}, Content: {entry['content']}")

# Function to add a new journal entry
def add_journal_entry():
    date = input("Enter date of entry (format: DD-MM-YYYY): ")
    category = input("Enter category of entry: ")
    content = input("Enter content of entry: ")
    journal_entries.append({"date": date, "category": category, "content": content})
    print("Journal entry added successfully.")

# Function to edit a journal entry
def edit_journal_entry():
    display_journal_entries()
    index = int(input("Enter the index of the entry to edit: ")) - 1
    if 0 <= index < len(journal_entries):
        date = input("Enter new date (format: DD-MM-YYYY): ")
        category = input("Enter new category: ")
        content = input("Enter new content: ")
        journal_entries[index] = {"date": date, "category": category, "content": content}
        print("Journal entry edited successfully.")
    else:
        print("Invalid entry index.")

# Function to delete a journal entry
def delete_journal_entry():
    display_journal_entries()
    index = int(input("Enter the index of the entry to delete: ")) - 1
    if 0 <= index < len(journal_entries):
        del journal_entries[index]
        print("Journal entry deleted successfully.")
    else:
        print("Invalid entry index.")

# Function for advanced search
def search_journal_entry():
    print("Advanced Search:")
    print("1. By Date")
    print("2. By Category")
    print("3. By Keyword")
    option = input("Choose search option: ")

    if option == '1':
        date = input("Enter date to search (format: DD-MM-YYYY): ")
        filtered_entries = [entry for entry in journal_entries if entry['date'] == date]
    elif option == '2':
        display_journal_entries(filter_by_category=True)
        return
    elif option == '3':
        keyword = input("Enter keyword to search: ")
        filtered_entries = [entry for entry in journal_entries if keyword.lower() in entry['content'].lower()]
    else:
        print("Invalid option.")
        return

    if not filtered_entries:
        print("No entries found.")
    else:
        print("Search Results:")
        for index, entry in enumerate(filtered_entries):
            print(f"{index + 1}. Date: {entry['date']}, Category: {entry['category']}, Content: {entry['content']}")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        display_journal_entries()
    elif choice == '2':
        add_journal_entry()
    elif choice == '3':
        edit_journal_entry()
    elif choice == '4':
        delete_journal_entry()
    elif choice == '5':
        search_journal_entry()
    elif choice == '6':
        print("Thank you for using the journal application.")
        break
    else:
        print("Invalid choice. Please try again.")
