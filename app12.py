secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    try:
        guess = int(input('Guess a number from 1 to 10: '))
    except ValueError:
        print("fuck you bitch")
        continue
    guess_count += 1
    if guess == secret_number:
        print("You guessed it correctly!")
        break
    else:
        print("Sorry, that's not it!")








