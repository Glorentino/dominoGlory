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
    def __init__(self, name):
        self.name = name
        self.hand = []

    def showHand(self):
        return self.hand
    
    def makeMove(self): # makeMove(choice, loc, dominodSide)
        # Pick up, Skip, Make a move
        print(gameboard)
        self.showHand()
        if gameboard[0][0] not in self.hand and gameboard[-1][1] not in self.hand and drawPile == []: # We skip
            return f"No options. {self.name} skips"
        
        choice = input("What is your choice?: ") # Player chooses

        while choice not in "0123456789P": # if choice invalid, ask again
            choice = input("What is your choice?: ")

        if choice.upper() == 'P': #If player decides to pick up
            self.pickUpFromPile()
            self.showHand() # Shows new hand
            # Check to see if user has any playable pieces
            playable = False
            for start, end in self.hand: # O(n) will chance to binary search
                if (end == gameboard[0][0] or start == gameboard[0][0] or
                    start == gameboard[-1][1] or end == gameboard[-1][1]):
                    playable = True
            if playable == True:
                choice = input("What is your choice?: ")
                while choice not in "0123456789": # After picking up, they can make a choice to make a move or Skip
                    choice = input("What is your choice?: ")
            else:
                return f"No options. {self.name} skips"

        # We're making a move   
        choice = int(choice)    
        while not (choice in range(self.hand) or self.hand[choice][0] == gameboard[0][0] or self.hand[choice][1] == gameboard[0][0] or
            self.hand[choice][0] == gameboard[-1][1] or self.hand[choice][1] == gameboard[-1][1]):
            print("Invalid")
            choice = int(input("What is your choice?: "))
            
        dominoSide = input("which side? 0 or 1")
        while dominoSide not in "01":
            dominoSide = input("which side? 0 or 1")
        loc = input(f"Where would you like to play {choice}?: N o S")
        while loc not in "NS":
            loc = input(f"Where would you like to play {choice}?: N o S")
        
        if loc == "N":
            if dominoSide == "1":
                self.hand[choice] = self.hand[choice][::-1] 
            gameboard.insert(0, self.hand.pop(choice))
        elif loc == "S":
            if dominoSide == "1":
                self.hand[choice] = self.hand[choice][::-1] 
            gameboard.insert(0, self.hand.pop(choice))
        return 
    def pickUpFromPile(self,drawPile):
        if len(drawPile) > 0:
            self.hand.append(drawPile.pop())
            return "Dominino Piece picked up"
        else:
            return "No Dominos pieces to pick up"


def main():
    print("Welcome to Domino  Glory")
    print()
    play = input("Would you to play? Y or N").upper()
    if play == 'Y':
        player1 = Player(name="Player1")
        player2 = Player(name="Player2")
        while len(player1.hand) < 7:
            player1.hand.append(dominoPieces.pop())
        while len(player2.hand) < 7:
            player2.hand.append(dominoPieces.pop())
        drawPile = dominoPieces
        player1.hand.sort()
        player2.hand.sort()
        if [6, 6] in player1.hand:
            gameboard.append(player1.hand.pop())
            first = player1
            second = player2
        elif [6, 6] in player2.hand:
            gameboard.append(player2.hand.pop())
            first = player2
            second = player1
        else:
            if sum(player1.hand[-1]) > sum(player2.hand[-1]):
                gameboard.append(player1.hand.pop())
                first = player1
                second = player2
            else:
                gameboard.append(player2.hand.pop())
                first = player2
                second = player1
        print(f"Goes {first.name} goes first!")
        # while len(first.hand) > 0 and len(second.hand) > 0:
        #     break
        first.makeMove()
        if len(first.hand) == 0:
            return first.name + "Wins"
        elif len(second.hand) == 0:
            return second.name + "Wins"

        # print(first.hand)
        # print(second.hand)
        # print(drawPile)

    else:
        return "Good bye!"

main()

print(len(dominoPieces))