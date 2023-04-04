#Primary colors
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

#Secondary colors
PURPLE = "purple"
ORANGE = "orange"
GREEN = "green"

def a_primary_color(color):
    return (color == RED) or (color == BLUE) or (color == YELLOW)


def different_colors(color1, color2):
    return color1 != color2


def print_secondary_color(color1, color2):
    if color1 == RED:
        if color2 == BLUE:
            print(PURPLE)
        else:
            print(ORANGE)

    elif color1 == BLUE:
        if color2 == RED:
            print(PURPLE)
        else:
            print(GREEN)

    else:
        if color2 == RED:
            print(ORANGE)
        else:
            print(GREEN)


#Main flow
primary_color1 = input("Enter the first primary color in lower case letters: ")
if not a_primary_color(primary_color1):
    print("Error: Invalid Color1")
    exit()

primary_color2 = input("Enter the second primary color in lower case letters: ")
if not a_primary_color(primary_color2):
    print("Error: Invalid Color2")
    exit()

if not different_colors(primary_color1, primary_color2):
    print("Error: The two colors you entered are same")
    exit()

print_secondary_color(primary_color1, primary_color2)