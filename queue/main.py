from queueM import QueueM

def menu():
    """User's options."""
    option = -1
    while option < 0 or option > 4:
        print('\n1 - Insert a new node in the queue.\n' +
              '2 - Print the linked list.\n' +
              '3 - Delete a node from queue.\n' +
              '4 - Clear the queue.\n' +
              '0 - Exit\n')
        option = int(input("Enter your option: "))
        if option < 0 or option > 4:
            print('\tInvalid option! Enter again.')
    return option

def main():
    print("### Queue's test ###\n")
    choice = 100

    # Start with the empty list
    myQueue = QueueM()

    while choice != 0:
        choice = menu()

        if choice == 0:
            print("Closing.\n")
            break
        elif choice == 1:
            myQueue.push(input("Enter an item: "))
        elif choice == 2:
            myQueue.print_queue()
        elif choice == 3:
            myQueue.pop()
        else:
            myQueue.clear()

main()
