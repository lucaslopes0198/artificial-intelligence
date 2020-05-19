from Expansion import Expansion
import LinkedList

class Search:
    def depthFirst(self, start, target):
        stack = LinkedList.DoublyLinkedList()
        copyStack = LinkedList.DoublyLinkedList()
        stack.insertEnd(start, None, None)
        copyStack.insertEnd(start, None, None)
        visited = [start]

        while stack.empty() is not None:
            currentMove = stack.removeEnd()
            nextMoves = Expansion.getNextMoves(currentMove.data)
            
            for i in range(len(nextMoves)-1, -1, -1):
                newMove = nextMoves[i]
                if newMove not in visited:
                    stack.insertEnd(newMove, currentMove, None)
                    copyStack.insertEnd(newMove, currentMove, None)
                    visited.append(newMove)
                    if newMove == target:
                        moves = copyStack.tree()
                        return "Depth-first solution: " + str(moves[::-1])
