from algorithms import *

import re

class Main:
    def __init__(self):
        self.choices = {"1": "breadthFirst", "2": "bidirectional", "3": "depthFirst", "4": "limitedDepth", "5": "iterativeDepth", "6": "uniformCost", "7": "greedy", "8": "aStar"}

    def solution(self):
        self.chosenAlgorithm = input("\nChoose an option or insert another key to exit\n1 - Breadth-first\n2 - Bidirectional\n3 - Depth-first\n4 - Limited Depth\n5 - Iterative Depth\n6 - Uniform-cost\n7 - Greedy\n8 - A*\n9 - Change coordinates\n")
        if self.chosenAlgorithm in self.choices:
            search = eval(self.choices[self.chosenAlgorithm] + ".Search")()
            solut = eval("search." + self.choices[self.chosenAlgorithm])(self.start, self.target)
            print("\n" + solut + "\n")
            return True
        elif self.chosenAlgorithm == "9":
            self.setCoordinates()
            return True
        else:
            return False

    def setCoordinates(self):
        print("Enter 2 numbers from 1 to 8 separated by space (e.g. 1 1)")
        regexStart = None
        while regexStart is None:
            start = input("start: ")
            regexStart = re.search("^[1-8] [1-8]$", start)
        self.start = [int(x) for x in start.split()]
        
        regexTarget = None
        while regexTarget is None:
            target = input("target: ")
            regexTarget = re.search("^[1-8] [1-8]$", target)
        self.target = [int(x) for x in target.split()]


if __name__ == "__main__":
    main = Main()

    main.setCoordinates()
    while True:
        running = main.solution()
        if not running:
            break
