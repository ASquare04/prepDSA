class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_node(self, node):
        if self.head is None or node is None:
            return

        if self.head == node:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        if node.prev:
            node.prev.next = node.next

        del node

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print("Doubly Linked List:", nodes)

# Example Usage
dll = DoublyLinkedList()

# Insertion
dll.insert_at_beginning(3)
dll.insert_at_end(5)
dll.insert_at_beginning(2)
dll.insert_at_end(7)
dll.display()  # Output: Doubly Linked List: [2, 3, 5, 7]

# Deletion
dll.delete_node(dll.head.next)  # Deletes the node with data 3
dll.display()  # Output: Doubly Linked List: [2, 5, 7]
