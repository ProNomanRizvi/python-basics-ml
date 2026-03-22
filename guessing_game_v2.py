secert = 7

guess = int(input("Enter a number: "))

if guess < 0:
    print("Please enter a positive number")
    exit()

while guess != secert:
    if guess < secert:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Enter a number: "))

print("Correct")