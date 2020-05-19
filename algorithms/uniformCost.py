import random
from Expansion import Expansion
import LinkedListValued

class Search(object):
    def uniformCost(self, start, target):
        queue = LinkedListValued.DoublyLinkedList()
        copyQueue = LinkedListValued.DoublyLinkedList()
        queue.insertEnd(start, None, 0, 0)
        copyQueue.insertEnd(start, None, 0, 0)
        visited = [start]

        while queue.empty() is not None:
            currentMove = queue.head
            nextMoves = Expansion.getNextMoves(currentMove.data)

            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited:
                    cost = random.randint(5,15) + currentMove.cost
                    queue.insertEnd(newMove, currentMove, cost, cost)
                    copyQueue.insertEnd(newMove, currentMove, cost, cost)
                    queue.insertNode(newMove, currentMove, cost, cost)
                    visited.append(newMove)
                    if newMove == target:
                        moves = copyQueue.tree(copyQueue.tail)
                        finalCost = copyQueue.tail
                        finalCost = finalCost.cost
                        return "Uniform cost solution: " + str(moves[::-1]) + "\nCost: " + str(finalCost)
            queue.removeStart()
