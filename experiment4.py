#contact management system
cbook = {}

while True:
    print("\nWelcome to the Contact Management System")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display contacts")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        name = input("Enter the contact name: ").strip()
        phone = input("Enter the phone number: ").strip()

        if name in cbook:
            print("That contact already exists.")
        else:
            cbook[name] = phone
            print("Contact added successfully.")

    elif choice == 2:
        name = input("Enter the name to search: ").strip()

        if name in cbook:
            print(f"{name}: {cbook[name]}")
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter the name to update: ").strip()

        if name in cbook:
            cbook[name] = input("Enter the new phone number: ").strip()
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter the name to delete: ").strip()

        if name in cbook:
            del cbook[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == 5:
        if cbook:
            print("\nContacts:")
            for name, phone in cbook.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts to display.")

    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
