from random import sample
import time



def choose_4_digit_number():
    """Generate a random 4-digit number with unique digits,
    where the first digit is not zero.
    The result is returned as a string."""

    digits = sample(range(1, 10,), 1) + sample(range(10), 3)
    while True: 
        digits = sample(range(1, 10), 1) + sample(range(10), 3)
        if len(set(digits)) == 4:
            return ''.join(map(str, digits))

def ask_to_play_again() -> bool:
    """Ask the player if they want to play again. The answer must be: 'Y'/'yes' or 'N'/'no'."""
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in("no", "n"):
            return False
        else:
            print("Please answer with 'yes' or 'no'.")

digits = choose_4_digit_number()
#print(digits) #kontrola
print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
      """)

attempts = 0
start_time = time.time()
while True:
    number = input("Enter a number: ")
    attempts += 1
    if len(number) != 4:
        print("The number must have 4 digits. Please enter a different number.")
        continue
    elif number.isdigit() is False:
        print("You have to entry only digits. Please enter a different number.")
        continue
    elif number[0] == "0":
        print("The digit cannot start by 0. Please enter a different number.")
        continue
    elif len(number) != len(set(number)):
        print("Each digit may only appear once in a single guess. Please enter a different number.")
        continue

    bulls = 0
    cows = 0
    for i in range(4):
        if number[i] == digits[i]:
            bulls += 1
        elif number[i] in digits:
            cows += 1
    
    if bulls == 4:
        if attempts == 1:
            print("Correct, you've guessed the right number in 1 guess!")
        else:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            duration = time.time() - start_time
            print(f"Time taken: {duration:.2f} seconds.")
            if ask_to_play_again():
                digits = choose_4_digit_number()
                #print(digits)  # kontrola nového čísla
                attempts = 0
                start_time = time.time()
                continue
            else:
                print("Game over.")
                break
            

            

    if bulls == 1 and cows == 1:
        print("1 bull, 1 cow")
    else:
        print(f"{bulls} bulls, {cows} cows")
        