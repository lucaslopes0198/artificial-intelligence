from Expansion import Expansion
import LinkedList

class Search(object):
    def bidirectional(self, start, start2):
        moves, moves2 = [], []

        stack = LinkedList.DoublyLinkedList()
        stackCopy = LinkedList.DoublyLinkedList()
        stack.insertEnd(start, None, None)
        stackCopy.insertEnd(start, None, None)
        visited = [start]

        stack2 = LinkedList.DoublyLinkedList()
        stackc2 = LinkedList.DoublyLinkedList()
        stack2.insertEnd(start2, None, None)
        stackc2.insertEnd(start2, None, None)
        visited2 = [start2]

        while stack.empty() is not None and stack2.empty() is not None:
            currentMove = stack.removeStart()
            currentMove2 = stack2.removeStart()

            nextMoves = Expansion.getNextMoves(currentMove.data)
            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited:
                    stack.insertEnd(newMove, currentMove, None)
                    stackCopy.insertEnd(newMove, currentMove, None)
                    visited.append(newMove)
                    if newMove in visited2:
                        while currentMove2.prevPointer is not None:
                            currentMove2 = currentMove2.prevPointer
                        while currentMove2.data != newMove:
                            currentMove2 = currentMove2.nextPointer
                        if currentMove2.parent is None:
                            moves2.append(currentMove.data)
                        while currentMove2.parent is not None:
                            currentMove2 = currentMove2.parent
                            moves2.append(currentMove2.data)
                        moves1 = stackCopy.tree()
                        return "Bidirecional solution: " + str(list(moves1[::-1]) + moves2)

            nextMoves = Expansion.getNextMoves(currentMove2.data)
            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited2:
                    stack2.insertEnd(newMove, currentMove2, None)
                    stackc2.insertEnd(newMove, currentMove2, None)
                    visited2.append(newMove)
                    if newMove in visited:
                        while currentMove.prevPointer is not None:
                            currentMove = currentMove.prevPointer
                        while currentMove.nextPointer is not None and currentMove.data != newMove:
                            currentMove = currentMove.nextPointer
                        if currentMove.parent is None:
                            moves2.append(currentMove.data)
                        while currentMove.parent is not None:
                            currentMove = currentMove.parent
                            moves2.append(currentMove.data)
                        moves1 = stackc2.tree()
                        return "Bidirecional solution: " + str(list(moves2[::-1]) + moves1)
