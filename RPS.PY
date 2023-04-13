#written by Andrewpyrookie
import random

print("Play Rock,Paper,Scissors")

print('')
print('''A 3 time attempt play, a draw equals 1 point, a win equals 3 points and the program checks the winner and display's the results''')
print('')

name = input("Enter Your name : ").upper()
print('')

print("Welcome to Rock,Papers and Scissors game!!")
print('')

print(f"{name} vs COMPTER")

n = 0 
choices = ["R","P","S"]
winplayer1 = 0
winplayer2 = 0 

while n!=3:
    player1 = input("You get to choose R,P/S : ")
    computer = random.choice(choices)
    if player1.upper() == "R":
        if computer == "R":
            winplayer1=winplayer1+1
            winplayer2=winplayer2+1
        elif computer == "P":
            winplayer2=winplayer2+3
        else:
            winplayer1=winplayer1+3
    elif player1.upper() == "P":
        if computer == "P":
            winplayer1=winplayer1+1
            winplayer2=winplayer2+1
        elif computer == "S":
            winplayer1=winplayer1+3
        else:
            winplayer2=winplayer2+3
    else:
        if computer == "S":
            winplayer1=winplayer1+1
            winplayer2=winplayer2+1
        elif computer == "R":
            winplayer2=winplayer2+3
        else:
            winplayer1=winplayer1+3

    n=n+1
if winplayer1 > winplayer2:
    print(f"{name} Wins the game with {winplayer1} wins")
else:
    print(f"Computer Wins the game with {winplayer2} wins")

    


