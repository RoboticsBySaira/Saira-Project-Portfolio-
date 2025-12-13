import random
number = random.randint(1, 10)
attempts = 0
max_attempts = 3
print("Guess the number between 1 and 10! You have 3 attempts.")
while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == number:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < number:
        print("🔼 Higher! Try again.")
    else:
        print("🔽 Lower! Try again.")
if attempts == max_attempts and guess != number:
    print(f"❌ Game Over! The number was {number}")
