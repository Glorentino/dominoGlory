import random
dominoPieces = [[0, 0], 
                [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], 
                [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], 
                [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                [3, 3], [3, 4], [3, 5], [3, 6],
                [4, 4], [4, 5], [4, 6],
                [5, 5], [5, 6],
                [6, 6]
                ]

random.shuffle(dominoPieces)

gameboard = []
drawPile = []
player1 = []
player2 = []

while len(player1) < 7:
    player1.append(dominoPieces.pop())
while len(player2) < 7:
    player2.append(dominoPieces.pop())
print(player1) 
print(player2) 


class Player:
    def __init__(self):
        self.hand = []

    def showHand(self):
        return self.hand
    def makeMove(self):
        return
    def pickUpFromPile(self,drawPile):
        self.hand.append(drawPile.pop())


print(len(dominoPieces))