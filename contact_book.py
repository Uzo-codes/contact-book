contacts = {}

while True:
    action = input("Choose: add / view / exit: ")

    if action == "add":
        name = input("Name: ")
        number = int(input("Number: "))
        contacts[name] = number

    elif action == "view":
        for name, number in contacts.items():
            print(f"{name}: {number}")

    elif action == "exit":
        break

    else:
        print("Network Error")