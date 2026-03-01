def main():
    userInput = input("What is the it ")
    snake(userInput)


def snake(case):
    for i in range(len(case)):
        if case[i].isupper():
            print("_" + case[i].lower(), end="")
        else:
            print(case[i], end="")
    print()


main()
