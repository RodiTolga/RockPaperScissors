import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
game_strings = ['Rock', 'Paper', 'Scissors']
user_score = 0
comp_score = 0
game_state = True

while game_state is True:

    user_choice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    print(game_images[user_choice])

    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])

    print(f"The computer chose: {game_strings[comp_choice]}")

    if user_choice > 2 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        comp_score += 1
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
        user_score += 1
    elif user_choice == 2 and comp_choice == 0:
        print("You lose!")
        comp_score += 1 
    elif user_choice > comp_choice:
        print("You win!")
        user_score += 1
    elif user_choice == comp_choice:
        print("It's a draw!")
    else:
        print("You lose!")
        comp_score += 1
        
    if user_score == 5:
        print("You win, well done my guy.")
        game_state = False
    elif comp_score == 5:
        print("You lose. You suck nerd.")
        game_state = False
    else:
        print(f"Your score is {user_score}. The opponent's score is {comp_score}")