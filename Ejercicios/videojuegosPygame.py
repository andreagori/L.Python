# from random import randint # libreria para generar numeros aleatorios.
"""
import pgzrun # libreria para crear videojuegos.

# Minigame 1: car racing

# variables
racing_car = Actor("car")
racing_car.pos = 150, 300 # x, y

# functions
def draw():
    screen.clear()
    screen.fill((128, 128, 128))
    draw_racing_line()
    racing_car.draw()

def draw_racing_line():
    racing_line = screen.draw.filled_rect(Rect((500, 100, 50, 400)), (125, 52, 65))  # x, y, width, height
    return racing_line

def racing_collision(racing_car, racing_line_x):
    if racing_car.x >= racing_line_x:
        print("You won!")
        quit()
    
def on_mouse_down(pos):
    if racing_car.collidepoint(pos):
        print("You are moving!")
        racing_car.x += 20  # This will move the car 10 pixels to the right
    else:
        print("You stopped!")

def update():
    racing_line_x = 500
    racing_collision(racing_car, racing_line_x)

pgzrun.go()
"""
# Minigame 2: two player game
import pgzrun
from pgzero.actor import Actor
from pgzero.rect import Rect
from pgzero.screen import Screen

# Variables
racing_car1 = Actor("car")
racing_car1.pos = 150, 300  # x, y

racing_car2 = Actor("car")
racing_car2.pos = 150, 350  # x, y

finish_line_x = 500
winner_declared = False


# Funciones
def draw():
    screen.clear()
    screen.fill((128, 128, 128))
    draw_racing_line()
    racing_car1.draw()
    racing_car2.draw()


def draw_racing_line():
    screen.draw.filled_rect(Rect((finish_line_x, 100, 50, 400)), (125, 52, 65))


def racing_collision(racing_car, racing_line_x):
    """Function to check collision with the finish racing line."""
    return racing_car.x >= racing_line_x


def on_key_down(key):
    global winner_declared
    if winner_declared:
        return

    if key == keys.UP:
        racing_car1.x += 20
        if racing_collision(racing_car1, finish_line_x):
            print("Player 1 won!")
            winner_declared = True
    elif key == keys.W:
        racing_car2.x += 20
        if racing_collision(racing_car2, finish_line_x):
            print("Player 2 won!")
            winner_declared = True


def update():
    pass


pgzrun.go()
