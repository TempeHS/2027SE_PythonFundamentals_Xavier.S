import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3:
    if sys.argv[1] not in ("-f", "--font"):
        sys.exit("Invalid flag. Use -f or --font.")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid font name.")
    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Usage: python figlet.py [-f font]")

text = input("Input: ")
print(figlet.renderText(text))
