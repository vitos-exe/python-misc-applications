#importing database module, creating database object
import database
CONTACT_PATH = 'contacts.txt'
contacts = database.Database(CONTACT_PATH)

#starting the app
print("Welcome to Contact Book!")
running = True
while running:
    #taking input from the user
    print("\n----------------")
    print("Choose action to do:")
    print("all - show all contacts")
    print("search - search the contact")
    print("add - add the contact")
    print("quit - exit the application")
    action = input("Your input: ")
    print("----------------\n")
    match action.lower():

        #prints all the contacts
        case "all":
            print(contacts)

        #searches the inputed contact and changes or deletes it
        case "search":
            searched = contacts.search(input("Enter searched contact name: ")) 
            if not(searched):
                print("\nInvalid contact name!!!")
                continue
            print(f"{searched}")
            action = input("Print 'del' to delete odject, 'change' to change it or anything else to go back: ").lower()
            if action == "del":
                contacts.delete(searched)
                print("\nThe contact was deleted")
            elif action == "change":
                searched.first_name = input("Input new first name: ")
                searched.second_name = input("Input new second name: ")
                searched.phone_number = input("Input new phone number name: ")
                searched.description = input("Input new description: ")
                print("\nThe contact was changed")

        #adds a contact
        case "add":
            print('Create new contact')
            full_name = input("Input contact's first and second names: ").split()
            if len(full_name) < 2:
                full_name.append("")
            num = input("Input contact's phone number: ")
            desc = input("Input contact's description: ")
            contacts.add(*full_name, num, desc)
            print("\nNew contact was added")

        #stops the app
        case "quit":
            running = False

        #if neither input is valid, takes input once more
        case _:
            print("Invalid input, try once more")