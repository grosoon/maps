from graphics import *
import sys
import math

chars = {
    "b": Circle(Point(50, 50), 10)
    }

win = GraphWin("map", 1000, 600)


def main():

    graph()
    get_input()

    
def graph():


    img = Image(Point(500,300), "tavern.PNG")
    img.draw(win)
    # draw grid
    for x in range(math.floor(1000/50)):
        for y in range(math.floor(600/50)):
            win.plotPixel(x*50, y*50, "black")


def get_input():
    to_run = input("What would you like to run?\nChoices: Add, Move, Load, Exit\n"
)
    if to_run == "Add":
        add()
    elif to_run =="Move":
        move()
    elif to_run == "Load":
        win.close()
        graph()
    elif to_run == "Exit":
        win.close()
        sys.exit()
    else:
        print("Please enter a valid command\n")
    get_input()

def add():
    name = input("Enter name of character to add to map\n")
    x = int(input("Enter x of character location\n"))
    y = int(input("Enter y of character location\n"))
    chosen = 1
    while(chosen):
        choice = input("Do you want to use an image or circle for the character?\nPlease enter \"Circle\" or \"Image\"\n")
        if choice == "Image":
            chosen = 0
            img = input("What image do you want to use?\n")
            chars[name] = Image(Point(x, y), img)
            chars[name].draw(win)
        elif choice == "Circle":
            chosen = 0
            color = input("What color do you want the circle to be?\n")
            chars[name] = Circle(Point(x, y), 25)
            chars[name].setFill(color)
            chars[name].draw(win)
        else:
            print("Please enter a valid choice")
            

def move():
    print("Enter name of character to add to map\n Choices are:\n")
    for char in chars:
        print(char)
    name = input("")
    if name in chars:
        x = input("How far do you want to move in the x direction\n")
        y = input("How far do you want to move in the y direction\n")
        chars[name].move(int(x), int(y))
        chars[name].undraw()
        chars[name].draw(win)
    else:
        print("Please enter a valid name")
        input("")
        move()


main()
