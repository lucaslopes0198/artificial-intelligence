import random
from Expansion import Expansion
import LinkedListValued

class Search:
    def aStar(self, start, target):
        value = abs(target[0] - start[0]) + abs(target[1] - start[1])
        queue = LinkedListValued.DoublyLinkedList()
        copyQueue = LinkedListValued.DoublyLinkedList()
        queue.insertEnd(start, None, 0, value)
        copyQueue.insertEnd(start, None, 0, value)
        visited = [start]

        while queue.empty() is not None:
            currentMove = queue.head

            nextMoves = Expansion.getNextMoves(currentMove.data)
            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited:
                    cost = random.randint(3, 10) + currentMove.cost
                    heuristic = abs(target[0] - newMove[0]) + abs(target[1] - newMove[1])
                    value = cost + heuristic
                    queue.insertEnd(newMove, currentMove, cost, value)
                    copyQueue.insertEnd(newMove, currentMove, cost, value)
                    queue.insertNode(newMove, currentMove, cost, value)
                    visited.append(newMove)
            if currentMove.data == target:
                finalCost = currentMove.value
                moves = copyQueue.tree(currentMove)
                return "A* solution: " + str(moves[::-1]) + "\nCost: " + str(finalCost)
            queue.removeStart()
