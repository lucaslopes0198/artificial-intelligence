from Expansion import Expansion
import LinkedList

class Search:
    def breadthFirst(self, start, target):
        queue = LinkedList.DoublyLinkedList()
        copyQueue = LinkedList.DoublyLinkedList()
        queue.insertEnd(start, None, None)
        copyQueue.insertEnd(start, None, None)
        visited = [start]

        while queue.empty() is not None:
            currentMove = queue.removeStart()
            nextMoves = Expansion.getNextMoves(currentMove.data)

            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited:
                    queue.insertEnd(newMove, currentMove, None)
                    copyQueue.insertEnd(newMove, currentMove, None)
                    visited.append(newMove)
                    if newMove == target:
                        moves = copyQueue.tree()
                        return "Breadth-first solution: " + str(moves[::-1])
