"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

flag = False

while flag == False:

    player1 = input("Player 1: Enter rock, paper or scissors: ").lower()
    player2 = input("Player 2: Enter rock, paper or scissors: ").lower()
    if player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    if player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
        flag == True
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    if player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
        flag == True
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    if player2 == "rock" and player1 == "scissors":
        print("Player 2 wins!")
        flag == True
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    if player2 == "scissors" and player1 == "paper":
        print("Player 2 wins!")
        flag == True
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    if player2 == "paper" and player1 == "rock":
        print("Player 2 wins!")
        flag == True
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break

    else:
        print("The game is tied.")
        print("Do you want to play new game? ")
        game = input("y/n: ")
        if game == "y":
            flag == False
        if game == "n":
            flag == True
            break
        