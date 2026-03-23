def get_user_input():
    while True:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Invalid input")
        else:
            return num


def check_guess(secret, guess):
    if guess == secret:
        return "correct"
    elif guess < secret:
        return "low"
    else:
        return "high"


def main():
    secret = 5
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        guess = get_user_input()
        attempts += 1

        result = check_guess(secret, guess)

        if result == "correct":
            print(f"Correct! Attempts: {attempts}")
            break
        elif result == "low":
            print("Too low")
        else:
            print("Too high")
    else:
        print("You ran out of attempts")


main()