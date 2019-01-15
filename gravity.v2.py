import pygame
import sys
from math import sqrt
import time
"""
In this program, a vector upwards is considered to be positive, and a 
vector downwards is considered to be negative
"""
pygame.init()

# Gets values from the command line
args = []
for value in sys.argv:
    args.append(value)
if not len(args) == 4:
    print("Please include 3 initial and constant values!, "
          "[INITIAL DISTANCE] [ACCELERATION] [INITIAL VELOCITY]")
    sys.exit()
DISTANCE = float(args[1])
ACCELERATION = float(args[2]) * -1
INITIAL_VELOCITY = float(args[3]) * -1

pygame.display.set_caption("Gravity Simulator")

# Initializes CONSTANT values for the program
x_size = 200
y_size = round(DISTANCE + 50)
ball_radius = 10
clock = pygame.time.Clock()
size = (x_size, y_size)
screen = pygame.display.set_mode(size)

# Defining colors and numbers
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initial values for the physics equations
x = 100
yt = 0
y_pos = y_size - DISTANCE - ball_radius
y_vel = INITIAL_VELOCITY

print("Simulation beginning...")


def the_time():
    """
    Function Purpose:
        Calculates and return the time taken for the ball to reach the ground
        based on the quadratic equation

    Returns:
        time_taken (float): The time taken for the ball to reach the ground 
        based on physics formuals
    """
    if ACCELERATION > 0:
        time1 = ((-INITIAL_VELOCITY) + sqrt((INITIAL_VELOCITY**2)
                 + (2*ACCELERATION*DISTANCE)))/ACCELERATION
        time2 = ((-INITIAL_VELOCITY) - sqrt((INITIAL_VELOCITY**2)
                 + (2*ACCELERATION*DISTANCE)))/ACCELERATION
    else:
        return 0
    if time1 >= 0:
        time_taken = time1
    else:
        time_taken = time2
    return time_taken


def y_velocity(y_vel):
    """
    Function Purpose:
        Calculate the current velocity of the ball in the y (up and down) axis

    Arguments:
        y_vel (float): The current y velocity

    Returns:
        y_vel (float): The next y velocity
    """
    y_vel += (ACCELERATION/60)
    return y_vel


def y_position(y_pos, y_vel):
    """
    Function Purpose:
        Calculate the next position for the ball in the y (up and down) axis

    Arguments:
        y_pos (float): The current y position of the ball
        y_vel (float): The current y velocity of the ball

    Returns:
        y_pos (float): The next y position of the ball
    """
    y_pos += (y_vel/60)
    return y_pos

# Starts the timer to calculate the run time of the program. We then compare
# this measured time to the calculated time to test validity of the graphical
# representation
start = time.time()

flag = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time_taken = the_time()

    # Calculates and modifys the circles position
    # until it reaches the ground
    if flag:
        print("VELOCITY: ", -round(y_vel, 4))
        if y_pos < y_size - ball_radius:
            pygame.draw.circle(screen, BLUE, (x, round(y_pos)), ball_radius, 0)
            y_vel = y_velocity(y_vel)
            y_pos = y_position(y_pos, y_vel)

        else:
            # End the timer which was started on line 106 and prints calculated
            # data
            end = time.time()
            print("COMPUTER TIME: ", round(end-start, 4))
            print()
            print("Simulation finished...")
            print()
            print("Time taken for ball to travel",
                  DISTANCE, "meters", end=" ")
            print("with an initial velocity of", INITIAL_VELOCITY,
                  "meters per second", end=" ")
            print("and a downward acceleration of", ACCELERATION,
                  "meters per second sqaured is", end=" ")
            if ACCELERATION == 0:
                print("infinite")
            else:
                print(round(time_taken, 4), "seconds.")
            flag = False

    # Updates the screen with what we have drawn until the ball touches the
    # ground, where now the screen will remain static
    if flag:
        pygame.display.update()

        screen.fill(BLACK)

    if flag is False:
        pygame.quit()
        sys.exit()

    # Limits to 60 fps
    clock.tick(60)
