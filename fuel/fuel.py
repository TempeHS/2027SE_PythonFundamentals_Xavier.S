def main():
    while True:
        fraction = input("Fraction: ")

        try:
            x_text, y_text = fraction.split("/")
            x = int(x_text)
            y = int(y_text)

            if x > y:
                continue

            percentage = (x / y) * 100
            percentage = round(percentage)

            if percentage == 0:
                print("E")
            elif percentage >= 100:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()
