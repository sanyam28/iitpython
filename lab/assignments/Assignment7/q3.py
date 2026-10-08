# Rock, Paper, Scissor game
import random

dicty = {0: "R", 1: "P", 2: "S"}
comp_score = 0
user_score = 0

print("Welcome Player, Let's play rock, paper, scissor game")
max_points = 0
while True:
    points = int(input("Enter maximum points for this game for a indivisual player: \n"))
    if points>0:
        max_points=points
        break
    print('It should be a positive integer')

while True:
    user_input = input("Enter R, P, S or (Q to quit): ").capitalize()
    if user_input == "Q":
        break
    if user_input not in dicty.values():
        print("Invalid input. Please try again.")
        continue

    comp_choice = random.choice(list(dicty.values()))
    print(f"Computer chose: {comp_choice}")

    if user_input == comp_choice:
        print("It's a tie!")
    elif (user_input == "R" and comp_choice == "S") or \
         (user_input == "P" and comp_choice == "R") or \
         (user_input == "S" and comp_choice == "P"):
        print("You score!")
        user_score += 1
    else:
        print("Computer score!")
        comp_score += 1

    print(f"Current Score - You: {user_score}, Computer: {comp_score}")
    if comp_score == max_points or user_score == max_points:
        print("Game Over!")
        break

if user_score > comp_score:
    print("You win the game!")
elif user_score < comp_score:
    print("Computer wins the game!")
else:
    print("The game is a tie!")
print(f"Final Score - You: {user_score}, Computer: {comp_score}")