from Expansion import Expansion
import LinkedList

class Search:
    def limitedDepth(self, start, target):
        limitDepth = int(input("Enter the limit depth: "))
        stack = LinkedList.DoublyLinkedList()
        copyStack = LinkedList.DoublyLinkedList()
        stack.insertEnd(start, None, 0)
        copyStack.insertEnd(start, None, 0)
        visited = [start] 

        while stack.empty() is not None:
            currentMove = stack.removeEnd()

            if currentMove == False:
                return "Solution not found."
            currentDepth = currentMove.level + 1
            if currentDepth <= limitDepth:
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
                        stack.insertEnd(newMove, currentMove, currentDepth)
                        copyStack.insertEnd(newMove, currentMove, currentDepth)
                        visited.append(newMove)
                        if newMove == target:
                            moves = copyStack.tree()
                            return "Limited depth-first solution: " + str(moves[::-1])
