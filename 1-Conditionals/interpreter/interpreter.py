x = input("What is Your number")
y = input("What sign are you using")
z = input("What is Your second number")


x = int(x)
z = int(z)


if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z


print(result)
