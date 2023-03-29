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



class Player:
    def __init__(self):
        self.hand = []

    def showHand(self):
        return self.hand
    def makeMove(self):
        return
    def pickUpFromPile(self,drawPile):
        self.hand.append(drawPile.pop())

def main():
    print("Welcome to Domino  Glory")
    print()
    play = input("Would you to play? Y or N").upper()
    if play == 'Y':
        player1 = Player()
        player2 = Player()
        while len(player1.hand) < 7:
            player1.hand.append(dominoPieces.pop())
        while len(player2.hand) < 7:
            player2.hand.append(dominoPieces.pop())
        player1.hand.sort()
        player2.hand.sort()
        print(player1.hand)
        print(player2.hand)

    else:
        return "Good bye!"

main()

print(len(dominoPieces))