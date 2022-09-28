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


def get_school(card):
    school = card[5]
    if school == '1':
        return "School of Computing and Engineering SCE"
    elif school == '2':
        return "School of Law"
    elif school == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"


def get_grade(card):
    grade = card[6]
    if grade == '1':
        return "Freshman"
    elif grade == '2':
        return "Sophomore"
    elif grade == '3':
        return "Junior"
    elif grade == '4':
        return "Senior"
    else:
        return "Invalid Grade"


def character_value(chr):
    return ord(chr) - 65


def get_check_digit(card):
    sum = 0
    for index in range(0, 9):
        sum += (index + 1) * character_value(card[index])
    return sum % 10


# functions return index of first not character
def get_index_of_not_character(str):
    for index in range(len(str)):
        if not str[index].isalpha():
            return index


# functions return index of first not digit
def get_index_of_not_digit(str):
    for index in range(len(str)):
        if not str[index].isdigit:
            return index


def verify_check_digit(card):
    if len(card) != 10:
        return False, "The length of the number given must be 10"
    elif not card[0:5].isalpha():
        index = get_index_of_not_character(card[0:5])
        return False, f"The first 5 characters must be A-Z, the invalid character is at {index} is {card[index]}"
    elif not card[7:10].isdigit():
        index = get_index_of_not_digit(card[7:10])
        return False, f"The last 3 characters must be 0-9, the invalid character is at {index} is {str[index]}"
    elif card[5] not in ['1', '2', '3']:
        return False, "The sixth character must be 1 2 or 3"
    elif card[6] not in ['1', '2', '3', '4']:
        return False, "The seventh character must be 1 2 3 or 4"
    elif card[9] != f'{get_check_digit(card)}':
        return False, f"Check Digit {card[9]} does not match calculated value {get_check_digit(card)}."
    else:
        return True, ""


if __name__ == "__main__":
    title = "Linda Hall"
    subtitle = "Library Card Check"
    plain = ""
    print(f"{title:^50}\n{subtitle:^50}\n{plain:=^50}\n")
    card = input("Enter Library Card. Hit Enter to Exit ==> ")
    while card != '':
        validation, error = verify_check_digit(card)
        if validation:
            print("Library card is valid.")
            print(f"The card belongs to a student in {get_school(card)}")
            print(f"The card belongs to a {get_grade(card)}\n")
            card = input("Enter Library Card. Hit Enter to Exit ==> ")
        else:
            print(f"Library card is invalid.\n{error}\n")
            card = input("Enter Library Card. Hit Enter to Exit ==> ")


