contacts = {}

def show_contacts():
    if not contacts:
        print("No contacts saved yet.")
    else:
        print("\n---saved contacts---")
        for name, number in contacts.items():
            print(name, ':', number)

def add_contacts():
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    contacts[name] = number
    print("Contact added")

def search_contacts():
    name = input("Enter your name: ")
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("No such contact.")


def remove_contacts():
    name = input("Enter your name: ")
    if name in contacts:
        del contacts[name]
        print("Contact removed")
    else:
        print("No such contact.")

while True:
    print("\n1. View Contacts")
    print("2. Add Contacts")
    print("3. Search Contacts")
    print("4. Remove Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1 - 5): ")
    if choice == '1':
        show_contacts()

    elif choice == '2':
        add_contacts()

    elif choice == '3':
        search_contacts()

    elif choice == '4':
        remove_contacts()

    elif choice == '5':
        print("Goodbye")
        break

    else:
        print("Invalid choice.")
