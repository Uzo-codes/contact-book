#Initialize an empty dictionary to store contact names and numbers
contacts = {}

#Start an infinite loop to repeatedly prompt the user for actions
while True:
    #User chooses an option
    action = input("Choose: add / view / exit: ")

    if action == "add":
        #Request for contact name and number, then add to the dictionary
        name = input("Name: ")
        number = int(input("Number: "))
        contacts[name] = number

    elif action == "view":
        #Displays all the saved contacts
        for name, number in contacts.items():
            print(f"{name}: {number}")

    elif action == "exit":
        break

    else:
        print("Network Error")