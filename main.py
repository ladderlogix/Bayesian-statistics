import pygame
from tkinter import *
import math
import random
import time
import json

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 208, 6)

with open("Settings.json", "r") as read_file:
            Settings = json.load(read_file) 

GuessX = Settings["GuessX"]
GuessY = Settings["GuessY"]
Guess = Settings["Guess"]
LockerX = Settings["LockerX"]
LockerY = Settings["LockerY"]
WIDTH = Settings["WIDTH"]
HEIGHT = Settings["HEIGHT"]
MARGIN = Settings["MARGIN"]
Debug = Settings["Debug"]

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(301): #X
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(201): #Y
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
XValue = random.randint(0,100)
YValue = random.randint(0,200)
print("Blue X is:")
print(XValue)
print("Blue Y is:")
print(YValue)
grid[XValue][YValue] = 3
#grid[XValue + 1][YValue - 1] = 3
#ErrorAreap = pygame.Rect(XValue - 5, YValue+ 10, 20, 10)
# Initialize pygame
pygame.init()

# Set the Height and WIDTH of the screen
WINDOW_SIZE = [1206, 606]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Baze Project")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Min and Max Program
def clampX(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def clampY(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (HEIGHT + MARGIN)
            row = pos[1] // (WIDTH + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(301):
        for column in range(201):
            color = WHITE
            if grid[row][column] == 1:
                color = YELLOW
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            if grid[row][column] == 2:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            if grid[row][column] == 3:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
 
    # Limit to 60 frames per second
    clock.tick(60)
    #Finding algrothmom
    if (Debug == 1 or Debug == 2):
        print("Guess X:")
        print(GuessX)
        print(GuessY)
    if (Debug == 1 or Debug == 3):
        grid[GuessY][GuessX] = 2
        
    if (GuessX == XValue and GuessY == YValue):
        print("Done")
        print(Guess)

    else:
        time.sleep(1)
        if XValue <= GuessX:
            GuessX = GuessX / 2
            GuessX = math.ceil(GuessX)
            GuessX = abs(GuessX)
            GuessX = clampX(GuessX, 0, 200)
            Guess += 1
            if (Debug == 1 or Debug == 2):
                print("X is True")
            

        else:
            GuessX = GuessX/2
            if Guess >= 2:
                LockerX -= 8
            GuessX = GuessX + GuessX + LockerX + LockerX
            GuessX = math.ceil(GuessX)
            GuessX = abs(GuessX)
            GuessX = clampX(GuessX, 0, 200)
            Guess += 1
            LockerX -= 1
            if (Debug == 1 or Debug == 2):
                print("X is Else")

        if YValue <= GuessY:
            GuessY = GuessY / 2
            GuessY = math.ceil(GuessY)
            GuessY = abs(GuessY)
            GuessY = clampY(GuessY, 0, 100)
            Guess += 1
            if (Debug == 1 or Debug == 2):
                print("Y is True")

        else:
            GuessY = GuessY/2
            if Guess >= 2:
                LockerY -= 8
            GuessY = GuessY + GuessY + LockerY + LockerY
            GuessY = math.ceil(GuessY)
            GuessY = abs(GuessY)
            GuessY = clampY(GuessY, 0, 100)
            Guess += 1
            LockerY -= 1
            if (Debug == 1 or Debug == 2):
                print("Y is Else")

    #pygame.draw.rect(screen, BLUE, ErrorAreap)
    pygame.display.flip()

pygame.quit()