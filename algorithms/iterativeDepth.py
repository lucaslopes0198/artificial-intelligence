from Expansion import Expansion
import LinkedList

class Search:
    def iterativeDepth(self, start, target):
        limitDepth = int(input("Enter the limit depth: "))
        currentDepth = 0

        queue = LinkedList.DoublyLinkedList()
        stack = LinkedList.DoublyLinkedList()
        copyStack = LinkedList.DoublyLinkedList()
        stack.insertEnd(start, None, 0)
        copyStack.insertEnd(start, None, 0)
        visited = [start]
        
        while not stack.empty() or not queue.empty():
            if stack.empty():
                while not queue.empty():
                    queueMove = queue.removeEnd()
                    stack.insertEnd(queueMove.data, queueMove.parent, queueMove.level)
                    copyStack.insertEnd(queueMove.data, queueMove.parent, queueMove.level)
                    visited.append(queueMove.data)
                limitDepth += 2
                print("\nSolution not found.\nNext limit depth: ", limitDepth)
            
            currentMove = stack.removeEnd()
            currentDepth = currentMove.level + 1
            nextMoves = Expansion.getNextMoves(currentMove.data)

            for i in range(len(nextMoves)-1, -1, -1):
                newMove = nextMoves[i]
                flag = True
                if newMove in visited:
                    flag = False
                    visitedIndex = visited.index(newMove)
                    head = copyStack.head
                    while head.data != newMove:
                        head = head.nextPointer
                    if currentDepth < head.level:
                        visited.pop(visitedIndex)
                        flag = True
                if flag:
                    if newMove == target:
                        copyStack.insertEnd(newMove, currentMove, currentDepth)
                        moves = copyStack.tree()
                        return "Iterative depth solution: " + str(moves[::-1])

                    if currentDepth < limitDepth:
                        stack.insertEnd(newMove, currentMove, currentDepth)
                        copyStack.insertEnd(newMove, currentMove, currentDepth)
                        visited.append(newMove)
                    else:
                        queue.insertEnd(newMove, currentMove, currentDepth)
