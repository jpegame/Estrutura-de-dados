from stackM import StackM

def menu():
    """User's options."""
    option = -1
    while option < 0 or option >= 5:
        print('\n1 - Insert a new node in the stack.\n' +
              '2 - Print the stack.\n' +
              '3 - Delete a node from the stack.\n' +
              '4 - Clear all stack.\n' +
              '0 - Exit\n')
        option = int(input("Enter your option: "))
        if option < 0 or option > 4:
            print('\tInvalid option! Enter again.')
    return option

def main():
    print("### Stack's test ###\n")
    choice = 100
    myStack = StackM()

    while choice != 0:
        choice = menu()

        if choice == 0:
            print("Closing..\n")
            break
        elif choice == 1:
            myStack.push(input("Enter an item: "))
        elif choice == 2:
            myStack.print_stack()
        elif choice == 3:
            myStack.pop()
        else:
            myStack.clear()

main()
