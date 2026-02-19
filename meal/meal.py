def main():
    time = input("What time is it? ")
    hours = convert(time)

    if hours >= 7.0 and hours <= 8.0:
        print("breakfast time")
    elif hours >= 12.0 and hours <= 13.0:
        print("lunch time")
    elif hours >= 18.0 and hours <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + (minutes / 60)


if __name__ == "__main__":
    main()
