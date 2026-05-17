def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(tank(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x_text, y_text = fraction.split("/")
    x = int(x_text)
    y = int(y_text)

    if x > y:
        raise ValueError("Numerator cannot be greater than denominator.")

    percentage = round((x / y) * 100)
    return percentage


def tank(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()
