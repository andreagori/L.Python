# from random import randint # libreria para generar numeros aleatorios.
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
    """Function to check collision with the finish racing line."""
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

# def draw():
#     screen.clear()
#     screen.draw.text("Hola Mundo", topleft=(10, 10), fontsize=60)

# pgzrun.go()
# manzana = Actor("manzanita")

# def draw():
#     """Function to draw the apple."""
#     screen.clear()
#     manzana.draw()

# def place_apple():
#     """Function random apple position."""
#     manzana.x = randint(10, 800)
#     manzana.y = randint(10, 600)

# def on_mouse_down(pos):
#     """Function to follow the mouse."""
#     if manzana.collidepoint(pos):
#         print("Good shot!")
#         place_apple()
#     else:
#         print("You missed!")
#         quit()

# place_apple()
# pgzrun.go()