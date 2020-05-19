class Node:
    def __init__(self, data, prevPointer, nextPointer, parent, cost, value):
        self.data = data
        self.prevPointer = prevPointer
        self.nextPointer = nextPointer
        self.parent = parent
        self.cost = cost
        self.value = value


class DoublyLinkedList:

    head = None
    tail = None

    def insertNode(self, data, parent, cost, value):

        node = Node(data, None, None, parent, cost, value)
        currentMove = self.head

        while currentMove.value < value:
            currentMove = currentMove.nextPointer
        if currentMove.prevPointer is not None:
            ant = currentMove.prevPointer
            ant.nextPointer = node
            node.prevPointer = ant
            node.nextPointer = currentMove
            currentMove.prevPointer = node

    def insereNodeGreedy(self, data, parent, cost, value):

        node = Node(data, None, None, parent, cost, value)
        currentMove = self.head

        while currentMove.value > value:
            currentMove = currentMove.nextPointer
        if currentMove.prevPointer is not None:
            ant = currentMove.prevPointer
            ant.nextPointer = node
            node.prevPointer = ant
            node.nextPointer = currentMove
            currentMove.prevPointer = node

    def insertEnd(self, data, parent, cost, value):

        node = Node(data, None, None, parent, cost, value)

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

    def tree(self, Node):

        current_node = Node
        node = []

        while current_node.parent is not None:
            node.append(current_node.data)
            current_node = current_node.parent
        node.append(current_node.data)
        return node
