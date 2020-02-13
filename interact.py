from graphics import *
import sys
import math

chars = {
    "b": Circle(Point(50, 50), 10)
    }

HEIGHT = 10
WIDTH = 10
win = GraphWin("map", WIDTH, HEIGHT)


def main():

    graph()
    get_input()

    
def graph():
    imgpath = input("What picture do you want to use for the map\n")
    win.close()
    img = Image(Point(WIDTH/2, HEIGHT/2), imgpath)
    WIDTH = img.getWidth()
    HEIGHT = img.getHeight()
    win = GraphWin("map", WIDTH, HEIGHT)
    xsize = int(input("What is the width of the image in feet?\n"))
    ysize = int(input("What is the height of the image in feet?\n"))
    
    img.draw(win)
    for char in chars:
        chars[char].draw(win)
    # draw grid
    for x in range(math.floor(xsize/10)):
        for y in range(math.floor(ysize/10)):
            win.plotPixel(x*WIDTH/xsize, y*HEIGHT/ysize, "black")


def get_input():
    to_run = input("What would you like to run?\nChoices: Add, Move, Load, Exit, Remove\n"
)
    if to_run == "Add" or to_run == "A":
        add()
    elif to_run =="Move" or to_run == "M":
        move()
    elif to_run == "Load" or to_run == "L":
        win.close()
        graph()
    elif to_run == "R" or to_run == "Remove":
        remove()
    elif to_run == "Exit" or to_run == "E":
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
            num = int(input("How many do you want to create?\n"))
            for i in range(num):
                chars[name+str(i)] = Circle(Point(x, y), 25)
                chars[name+str(i)].setFill(color)
                chars[name+str(i)].draw(win)
        else:
            print("Please enter a valid choice")
            

def move():
    print("Enter name of character to add to map\n Choices are:")
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

def remove():
    print("Enter name of character to add to map\n Choices are:\n")
    for char in chars:
        print(char)
    name = input("")
    if name in chars:
        chars[name].undraw()
        chars.pop(name)
    else:
        print("Please enter a valid name")
        input("")
        remove()


main()
