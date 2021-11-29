import random  # import random module
while(True):
    print("Rock paper scissors game! \n Rules:\n Rock beats Scissors\n Scissors beats Paper\n Paper beats Rock")
    # try except block for if the input is not convertible to integer
    try:
        choice = int(
            input("Choose input:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))
    except:
        print("Invalid choice")
        choice = int(
            input("Choose input:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))
    # choice has to be between 1 and 3
    while(choice > 3 or choice < 1):
        print("Invalid choice")
        choice = int(
            input("Choose input:\n 1. Rock\n 2. Paper\n 3. Scissors\n"))

    if(choice == 1):
        print("Your choice is Rock")
    elif(choice == 2):
        print("Your choice is Paper")
    elif(choice == 3):
        print("Your choice is Scissors")

    computerChoice = random.randint(1, 3)
    # don't allow machine to pick the same choice as user
    while(choice == computerChoice):
        computerChoice = random.randint(1, 3)
    if(computerChoice == 1):
        print("The computer picked Rock")
    elif(computerChoice == 2):
        print("The computer picked Paper")
    elif(computerChoice == 3):
        print("The computer picked Scissors")

    if(choice == 1 and computerChoice == 2):
        print("Paper wins\n You lose!")
    elif(choice == 2 and computerChoice == 1):
        print("Paper wins\n You win!")
    elif(choice == 1 and computerChoice == 3):
        print("Rocks wins!\n You win!")
    elif(choice == 3 and computerChoice == 1):
        print("Rocks wins!\n You lose!")
    elif(choice == 2 and computerChoice == 3):
        print("Scissors wins!\n You lose!")
    elif(choice == 3 and computerChoice == 2):
        print("Scissors wins!\n You win!")

    playAgain = input("\nPlay again? (y/n)")
    if(playAgain.lower() == "n"):
        break
