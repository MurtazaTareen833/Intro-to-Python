import random

def game():
    choices = ['snake', 'water', 'gun']

    # Get user's choice
    user_choice = input("Enter your choice (snake/water/gun): ").lower()

    # Validate user's choice
    if user_choice not in choices:
        print("Invalid choice! Please choose either snake, water, or gun.")
        return

    # Generate computer's choice
    computer_choice = random.choice(choices)

    # Print the choices made by the user and computer
    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'snake':
        if computer_choice == 'water':
            print("You win! Snake drinks water.")
        else:
            print("You lose! Gun kills snake.")
    elif user_choice == 'water':
        if computer_choice == 'gun':
            print("You win! Water extinguishes the gun.")
        else:
            print("You lose! Snake drinks water.")
    elif user_choice == 'gun':
        if computer_choice == 'snake':
            print("You win! Gun kills snake.")
        else:
            print("You lose! Water extinguishes the gun.")

# Start the game
game()
