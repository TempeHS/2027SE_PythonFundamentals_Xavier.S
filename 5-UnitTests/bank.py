def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    text = greeting.strip().lower()
    if text.startswith("hello"):
        return 0
    if text.startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
