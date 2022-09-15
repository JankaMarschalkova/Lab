print("Welcome to the Flarsheim Guesser!")

# guessing start and while loop will end when the player input n
# the first while loop will automatically run because answer value is defined as 'y'
answer = 'y'
while answer != 'n':
    if answer == 'y':
        print("\nPlease think of a number between and including 1 and 100.\n")

        remainder_three = 0
        remainder_five = 0
        remainder_seven = 0

        # while loop will continue asking a question about remainder divided by 3 until there is valid input
        while True:
            remainder_three = int(input("What is the remainder when your number is divided by 3 ?"))
            if remainder_three < 0:
                print("The value entered must be 0 or greater")
            elif remainder_three >= 3:
                print("The value entered must be less than 3")
            else:
                break
        print()

        # while loop will continue asking a question about remainder divided by 5 until there is valid input
        while True:
            remainder_five = int(input("What is the remainder when your number is divided by 5 ?"))
            if remainder_five < 0:
                print("The value entered must be 0 or greater")
            elif remainder_five >= 5:
                print("The value entered must be less than 5")
            else:
                break
        print()

        # while loop will continue asking a question about remainder divided by 7 until there is valid input
        while True:
            remainder_seven = int(input("What is the remainder when your number is divided by 7 ?"))
            if remainder_seven < 0:
                print("The value entered must be 0 or greater")
            elif remainder_seven >= 7:
                print("The value entered must be less than 7")
            else:
                break

        # for loop from 1 to 100 will check number by number if the remainders are the same as the player input before
        for number in range(1, 101):
            if number % 3 == remainder_three and number % 5 == remainder_five and number % 7 == remainder_seven:
                result = number
                print(f"Your number was {number}")
                break

        print("How amazing is that?\n")
    answer = input('Do you want me to play again? Y to continue, N to quit ==> ')

