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
        self.name = ""
        self.hand = []

    def showHand(self):
        return self.hand
    
    def makeMove(self):
        # Pick up, Skip, Make a move
        print(gameboard)
        self.showHand()
        choice = input("What is your choice?: ") # Player chooses

        while choice not in "0123456789PS": # if choice invalid, ask again
            choice = input("What is your choice?: ")

        if choice == 'P': #If player decides to pick up
            self.pickUpFromPile()
            self.showHand() # Shows new hand
            choice = input("What is your choice?: ")
            while choice not in "0123456789S": # After picking up, they can make a choice to make a move or Skip
                choice = input("What is your choice?: ")
        if choice == "S": # Skip
            return     
        # We're making a move   
        choice = int(choice)    
        while int(choice) not in range(self.hand):
            choice = int(input(f"What is your choice?0-{str(len(self.hand)-1)}: "))
        if choice in range(len(self.hand)):
            dominoSide = input("which side? 0 or 1")
            loc = input(f"Where would you like to play {choice}?: N o S")
            while dominoSide not in "01":
                dominoSide = input("which side? 0 or 1")
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
        self.hand.append(drawPile.pop())


def main():
    print("Welcome to Domino  Glory")
    print()
    play = input("Would you to play? Y or N").upper()
    if play == 'Y':
        player1 = Player("Player1")
        player2 = Player("Player2")
        while len(player1.hand) < 7:
            player1.hand.append(dominoPieces.pop())
        while len(player2.hand) < 7:
            player2.hand.append(dominoPieces.pop())
        drawPile = dominoPieces
        player1.hand.sort()
        player2.hand.sort()
        if [6, 6] in player1.hand:
            first = player1
            second = player2
        elif [6, 6] in player2.hand:
            first = player2
            second = player1
        else:
            if sum(player1.hand[-1]) > sum(player2.hand[-1]):
                first = player1
                second = player2
            else:
                first = player2
                second = player1
        
        # while len(first.hand) > 0 and len(second.hand) > 0:
        #     break
        if len(first.hand) == 0:
            return first.name + "Wins"
        elif len(second.hand) == 0:
            return second.name + "Wins"
        print(first.hand)
        print(second.hand)
        print(drawPile)

    else:
        return "Good bye!"

main()

print(len(dominoPieces))