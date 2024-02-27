def __menu():
    print("1.   Information")
    print("2.   Credits")
    print("3.   Exit")

def __infoPath():

def handle_choice(choice):
    if choice == '1':
        __infoPath()

    elif choice == '2':
        print("Credits... ")

    elif choice == '3':
        print("See you... ")

    else:
        print("1..3")

if __name__ == "__main__":
    while True:
        __menu()

        user_choice = input(">> ")
        handle_choice(user_choice)
        if user_choice == '3':
            break