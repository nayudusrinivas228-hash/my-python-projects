import random
import time
attempts = 0
max_attempts = 3
lock_time = 30
guess = random.randint(1, 10000)
print("Instructions")
print("You have only 3 attempts.")
print("After 3 wrong attempts, you must wait 30 secounds.")
print("After 30 minutes, you will get 3 new attempts.")
while True:
    user = int(input("\nGuess The Number: "))
    if user == guess:
        print("Yes Boss! You are correct.")
        print("Answer:", guess)
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print("Wrong Guess!")
        print("Remaining attempts:", remaining)
        if attempts == max_attempts:
            print("\nToo many wrong attempts!")
            print("Your game is locked for 30 secounds.")
            time.sleep(lock_time)
            print("30 secounds completed. Game Unlocked!")
            attempts = 0