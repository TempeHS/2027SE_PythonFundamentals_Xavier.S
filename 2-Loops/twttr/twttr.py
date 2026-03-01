def main():
    userinput = input("What do you want to say")
    vowels(userinput)


def vowels(case):
    letters = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for i in case:
        if i in letters:
            print("", end="")
        else:

            print(i, end="")


main()
