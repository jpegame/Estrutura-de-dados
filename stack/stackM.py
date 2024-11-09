from node import Node

class StackM:
    """Stack's class."""
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def push(self, new_data):
        """Function to insert a new node at the beginning."""
        new_node = Node(new_data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_stack(self):
        """Function to print the stack."""
        if self.isEmpty():
            print('Empty stack.')
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def pop(self):
        """Function to remove item at the beginning."""
        if self.isEmpty():
            print("Empty stack.")
        else:
            self.head = self.head.next

    def clear(self):
        """Function to clear all items in the stack."""
        if self.isEmpty():
            print("Empty stack.")
        else:
            self.head = None
