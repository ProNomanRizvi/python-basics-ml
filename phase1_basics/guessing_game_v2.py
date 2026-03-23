secret = 7
count = 0
max_attempts = 3

while count < max_attempts:
    guess = int(input("Enter a number: "))

    if guess < 0:
        print("Invalid input")
        continue

    count += 1

    if guess == secret:
        print("Correct")
        print(f"You guessed the number in {count} attempts")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

else:
    print("You have exceeded the number of attempts")