from node import Node

class QueueM:
    """Queue's class."""
    
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

    def print_queue(self):
        """Function to print the queue."""
        if self.isEmpty():
            print("Empty queue.")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def pop(self):
        if self.isEmpty():
            print("Empty queue.")
        else:
            penult = self.head
            last = self.head
            while last.next:
                penult = last
                last = last.next
            penult.next = None
            self.tail = penult

    def clear(self):
        """Function to clear all items in the queue."""
        if self.isEmpty():
            print("Empty queue.")
        else:
            self.head = None
