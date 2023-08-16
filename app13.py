started = False
while True:
    command = input("> ")

    if command.upper() == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit the game")
    elif command.upper() == "QUIT":
        print("Until next time!")
        break
    elif command.upper() == "START":
        if started:
            print("Your car is already moving bruh")
        else:
            started = True
            print("Car go vroooooom!")
    elif command.upper() == "STOP":
        if not started:
            print("Your car is already stopped bruh")
        else:
            started = False
            print('Your car has stopped!')
    else:
        print("WHAT THE FUCK DO YOU MEAN BY THAT CABRÓN?")
