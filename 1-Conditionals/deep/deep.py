x = input("What is the meaning of life? ").lower()

match x:
    case "42" | "forty-two" | "forty two":
        print("Yes")

    case _:
        print("NO")
