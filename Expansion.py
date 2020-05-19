class Expansion:

    @classmethod
    def getNextMoves(cls, currentMove):
        nextMoves = []
        # print('kokd:', cls.validateMove(move=[1, 1]))
        move1 = [currentMove[0] - 1, currentMove[1] - 2]
        nextMoves.append(cls.__validateMove(move1))
        move2 = [currentMove[0] - 2, currentMove[1] - 1]
        nextMoves.append(cls.__validateMove(move2))

        move3 = [currentMove[0] + 1, currentMove[1] - 2]
        nextMoves.append(cls.__validateMove(move3))
        move4 = [currentMove[0] + 2, currentMove[1] - 1]
        nextMoves.append(cls.__validateMove(move4))

        move5 = [currentMove[0] + 1, currentMove[1] + 2]
        nextMoves.append(cls.__validateMove(move5))
        move6 = [currentMove[0] + 2, currentMove[1] + 1]
        nextMoves.append(cls.__validateMove(move6))

        move7 = [currentMove[0] - 1, currentMove[1] + 2]
        nextMoves.append(cls.__validateMove(move7))
        move8 = [currentMove[0] - 2, currentMove[1] + 1]
        nextMoves.append(cls.__validateMove(move8))

        return list(filter(None.__ne__, nextMoves))

    @staticmethod
    def __validateMove(move):
        if move[0] > 0 and move[0] <= 8 and move[1] > 0 and move[1] <= 8:
            if move is not None:    
                return move
