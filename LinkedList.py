class Node:
    def __init__(self, data, prevPointer, nextPointer, parent, level):
        self.data = data
        self.prevPointer = prevPointer
        self.nextPointer = nextPointer
        self.parent = parent
        self.level = level

class DoublyLinkedList:

    head = None
    tail = None

    def insertStart(self, data, parent, level):

        node = Node(data, None, None, parent, level)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.nextPointer = self.head
            self.head.prevPointer = node
            self.head = node

    def insertEnd(self, data, parent, level):

        node = Node(data, None, None, parent, level)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nextPointer = node
            node.prevPointer = self.tail
            self.tail = node

    def removeStart(self):

        current_node = None

        if self.head is not None:
            current_node = self.head
            if current_node.nextPointer is not None:
                self.head = self.head.nextPointer
            else:
                self.head = self.tail = None
        return current_node

    def removeEnd(self):

        if self.head is not None:
            current_node = self.tail
            if current_node.prevPointer is not None:
                self.tail = self.tail.prevPointer
                self.tail.nextPointer = None
            else:
                self.head = self.tail = None
        else:
            return False
        return current_node

    def empty(self):

        if self.head is None:
            return True
        else:
            return False

    def showLinkedList(self):

        print("Doubly linked list:")
        current_node = self.head
        node = ""

        while current_node is not None:
            node += " | " + str(current_node.data) + str(current_node.parent) + " | "
            current_node = current_node.nextPointer

        print(node)

    def tree(self):

        current_node = self.tail
        node = []

        while current_node.parent is not None:
            node.append(current_node.data)
            current_node = current_node.parent

        node.append(current_node.data)

        return node
