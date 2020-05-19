import random
from Expansion import Expansion
import LinkedListValued

class Search:
    def greedy(self, start, target):
        heuristic = abs((target[0] - start[0])) + abs((target[1] - start[1]))
        queue = LinkedListValued.DoublyLinkedList()
        copyQueue = LinkedListValued.DoublyLinkedList()
        queue.insertEnd(start, None, 0, heuristic)
        copyQueue.insertEnd(start, None, 0, heuristic)
        visited = [start]

        while queue.empty() is not None:
            currentMove = queue.removeStart()
            nextMoves = Expansion.getNextMoves(currentMove.data)
            minHeuristic = float("inf")

            for i in range(len(nextMoves)):
                newMove = nextMoves[i]
                if newMove not in visited:
                    heuristic = abs((target[0] - newMove[0])) + abs((target[1] - newMove[1]))
                    if heuristic < minHeuristic:
                        minHeuristic = heuristic
                        minCurrentMove = newMove
                    if newMove == target:
                        copyQueue.insertEnd(minCurrentMove, currentMove, 0, minHeuristic)
                        moves = copyQueue.tree(copyQueue.tail)
                        tail = copyQueue.tail
                        finalHeuristic = 0
                        while tail.parent is not None:
                            finalHeuristic += tail.value
                            tail = tail.parent
                        return "Greedy solution: " + str(moves[::-1]) + "\nHeuristic: " + str(finalHeuristic)

            queue.insertEnd(minCurrentMove, currentMove, 0, minHeuristic)
            copyQueue.insertEnd(minCurrentMove, currentMove, 0, minHeuristic)
            queue.insereNodeGreedy(minCurrentMove, currentMove, 0, minHeuristic)
            visited.append(minCurrentMove)
