from tabulate import tabulate
import datetime

# Initialize list for journal entries
journal_entries = [
    {"date": "13-04-2024", "category": "Happy", "content": "I've met my old friend, that we haven't met for a long time, I'm really happy today."},
    {"date": "21-04-2024", "category": "Sad", "content": "I feel sad today that I have to leave my girlfriend for a long time."}
]

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
        headers = ["Date", "Category", "Journal"]
        if not filter_by_category:
            table_data = [[entry["date"], entry["category"], entry["content"]] for entry in journal_entries]
        else:
            category = input("Enter category: ")
            filtered_entries = [entry for entry in journal_entries if entry['category'].lower() == category.lower()]
            if not filtered_entries:
                print(f"No entries found with category '{category}'.")
                return
            table_data = [[entry["date"], entry["category"], entry["content"]] for entry in filtered_entries]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# Function to add a new journal entry
def add_journal_entry():
    while True:
        date_input = input("Enter date of entry (format: DD-MM-YYYY): ")
        try:
            date = datetime.datetime.strptime(date_input, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Invalid date format. Please enter date in the format DD-MM-YYYY.")
    
    category = input("Enter category of entry: ")
    content = input("Enter content of entry: ")
    journal_entries.append({"date": date.strftime("%d-%m-%Y"), "category": category, "content": content})
    print("Journal entry added successfully.")

# Function to edit a journal entry
def edit_journal_entry():
    display_journal_entries()
    index = int(input("Enter the index of the entry to edit: ")) - 1
    if 0 <= index < len(journal_entries):
        entry = journal_entries[index]
        print("Current entry details:")
        print(f"Date: {entry['date']}, Category: {entry['category']}, Content: {entry['content']}")
        
        new_content = input("Enter new content: ")
        journal_entries[index]['content'] += "\n" + new_content
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
