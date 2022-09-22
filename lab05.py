########################################################################
##
## CS 101 Lab
## Program #
## Name Janka Marschalkova
## Email jmmtb@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM :
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random


def play_again() -> bool:
    user_input = input("Do you want to play again? ==> ")
    # if user inputs incorrect input, there is this information ouput and it will promt user again
    while user_input.lower() not in ['y', 'yes', 'n', 'no']:
        print("You must enter Y/YES/N/NO to continue. Please try again")
        user_input = input("Do you want to play again? ==> ")
    return user_input.lower() in ['Y', 'YES', 'y', 'yes']


def get_wager(bank: int) -> int:
    chips = int(input("How many chips you want to wager? ==> "))
    # if user inputs incorrect input, there is this information ouput and it will promt user again
    while chips <= 0 or chips > bank:
        if chips <= 0:
            print("The wager amount must be greater than 0. Please enter again.")
        else:
            print("The wager amount cannot be greater than how much you have. ", bank)
        chips = int(input("How many chips you want to wager? ==> "))
    return chips


def get_slot_results() -> tuple:
    # return 3 random integers
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)


def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb:
        if reela == reelc:
            return 3
        else:
            return 2
    elif reelb == reelc:
        return 2
    elif reela == reelc:
        return 2
    return 0

def get_bank() -> int:
    chips = int(input("How many chips you want to start with? ==> "))
    # if user inputs incorrect input, there is this information ouput and it will promt user again
    while chips < 0 or chips > 101:
        if chips < 0:
            print("Too low a value, you can only choose 1 - 100 chips")
        else:
            print("Too high a value, you can only choose 1 - 100 chips")
        chips = int(input("How many chips you want to start with? ==> "))
    return chips


def get_payout(wager, matches):
    if matches == 3:
        payout = wager * 10 - wager
    elif matches == 2:
        payout = wager * 3 - wager
    else:
        payout = -1 * wager
    return payout


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        start_bank = bank
        spin = 0
        most_chip = 0
        while bank > 0:  # Replace with condition for if they still have money.

            wager = get_wager(bank)

            # controling if the currect wager is the maximum one
            if wager > most_chip:
                most_chip = wager
            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin += 1

        print("You lost all", start_bank, "in", spin, "spins")
        print("The most chips you had was", most_chip)
        playing = play_again()