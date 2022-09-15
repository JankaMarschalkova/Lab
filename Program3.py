print("Welcome to the Flarsheim Guesser!")

# guessing start and while loop will end when the player input n
answer = 'y'
while answer != 'n':
    if answer == 'y':
        print("\nPlease think of a number between and including 1 and 100.\n")

        divided_three = 0
        divided_five = 0
        divided_seven = 0

        # while loop will continue asking a question about remainder divided by 3 until there is valid input
        while True:
            divided_three = int(input("What is the remainder when your number is divided by 3 ?"))
            if divided_three < 0:
                print("The value entered must be 0 or greater")
            elif divided_three >= 3:
                print("The value entered must be less than 3")
            else:
                break
        print()

        # while loop will continue asking a question about remainder divided by 5 until there is valid input
        while True:
            divided_five = int(input("What is the remainder when your number is divided by 5 ?"))
            if divided_five < 0:
                print("The value entered must be 0 or greater")
            elif divided_five >= 5:
                print("The value entered must be less than 5")
            else:
                break
        print()

        # while loop will continue asking a question about remainder divided by 7 until there is valid input
        while True:
            divided_seven = int(input("What is the remainder when your number is divided by 7 ?"))
            if divided_seven < 0:
                print("The value entered must be 0 or greater")
            elif divided_seven >= 7:
                print("The value entered must be less than 7")
            else:
                break

        # for loop from 1 to 100 will check number by number if the remainders are the same as the player input before
        for number in range(1, 101):
            if number % 3 == divided_three and number % 5 == divided_five and number % 7 == divided_seven:
                result = number
                print(f"Your number was {number}")
                break

        print("How amazing is that?\n")
    answer = input('Do you want me to play again? Y to continue, N to quit ==> ')

