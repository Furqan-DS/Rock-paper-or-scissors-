import random
import time
time.sleep(1)
game = ("Welcome to rock, paper or sicsors")

for letter in game:
	print(letter, end="", flush=True)
	time.sleep(0.1)
print()

time.sleep(2)
choices = ["rock", "paper", "sicsors"]
computer = random.choice(choices)
player = input("Choose rock, paper or sicsors: ").lower()
print("You:", player)
time.sleep(1)
print("Computer:", computer)
time.sleep(1)
if player == computer:
	print("It a tie")
elif player == "rock" and computer == "sicsors":
	print("You win!🏅")
elif player == "paper" and computer == "rock":
	print("You win!🏅")
elif player == "sicsors" and computer == "paper":
	print("You win!🏅")
else:
	print("Computer wins! 🥀")