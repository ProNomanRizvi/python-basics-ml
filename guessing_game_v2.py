secert = 7

guess = int(input("Enter a number: "))

count = 0

if guess < 0:
    print("Please enter a positive number")
    exit()

while guess != secert:
    if guess < secert:
        print("Too low")
        count += 1
        if count == 3:
            print("You have exceeded the number of attempts")
            exit()
    else:
        print("Too high")
        count += 1
        if count == 3:
            print("You have exceeded the number of attempts")
            exit()
    guess = int(input("Enter a number: "))

print("Correct")
print(f"You guessed the number in {count} attempts")