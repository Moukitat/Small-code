import random

def number_game():
    secret_number = random.randint(1, 10)
    attempts = 3
    print("Welcome! Please enter a number of your choice.")
    
    for attempt in range(attempts):
        try:
            user_choice = int(input(f"Attempt {attempt + 1}/{attempts}. Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_choice == secret_number:
            print("Congratulations! You found the secret number.")
            break
        elif user_choice < secret_number:
            print("This number is lower than the secret number.")
        else:
            print("This number is higher than the secret number.")
        
        if attempt == attempts - 1:
            print(f"Sorry, you've used all your attempts. The secret number was: {secret_number}.")
            
number_game()
