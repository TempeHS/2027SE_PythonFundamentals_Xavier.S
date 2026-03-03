def main():

    user_input = input("What would you like your number plate to be? ")

    if (
        len_check(user_input)
        and letter_check(user_input)
        and valid_value_check(user_input)
        and number_check(user_input)
    ):
        print("Valid!")

    else:
        main()

    return


def len_check(string):

    if len(string) > 6:
        print("Error! Number plate is too long! ")
        return False
    elif len(string) < 2:
        print("Error! Number plate is too short! ")
        return False
    else:
        return True


def letter_check(string):
    string_check = 0
    for i in range(2):
        if string[i].isalpha():
            string_check += 1
        else:
            print("Error! Number plate does not start with two alphabetical values! ")
            return False

    if string_check >= 2:
        return True


def valid_value_check(string):
    value = len(string)
    for i in range(len(string)):
        if string[i].isnumeric or string[i].isascii():
            value -= 1
        else:
            print("Error! Only numbers and letters are allowed!")
            return False

    if value <= 0:
        return True


def number_check(string):
    for i in range(len(string)):
        if string[i].isnumeric():

            _, middle, right = string.partition(string[i])

            if right.isnumeric() == False and right != "":
                print("Error! Number plate has a number before a letter")

                return False

            elif middle == "0":
                print("Error! First number can't be 0!")
                return False

            else:
                return True
        else:
            return True


main()
