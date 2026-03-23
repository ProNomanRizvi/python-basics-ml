secret = 8
guess = int(input("Guess the number: "))

if guess < 0:
    print("Invalid input")
elif guess > secret:
    print("Too High")
elif guess < secret:
    print("Too Low")
else:
    print("Correct")