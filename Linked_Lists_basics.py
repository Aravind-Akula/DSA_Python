class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def append(self, data):
        """Add a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, key):
        """Delete the first occurrence of a node with the given key."""
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the linked list
        if not current:
            print("Key not found!")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Linked List:")
    ll.display()

    print("\nDeleting 20:")
    ll.delete(20)
    ll.display()

    print("\nDeleting 40 (not in list):")
    ll.delete(40)
    ll.display()
