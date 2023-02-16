from tkinter import *
import random

# variables ng mga idol
g_width = 1280
g_height = 700
speed = 30
space_size = 10
body_parts = 5
snake_color = "#F5F5DC"
food_color = "#FFFF00"
background_color = "#40444B"

class Snake:

    def __init__(self):
        self.body_size = body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (g_width / space_size)-1) * space_size
        y = random.randint(0, (g_height / space_size) - 1) * space_size

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + space_size, y + space_size, fill=food_color, tag="food")



def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= space_size
    elif direction == "down":
        y += space_size
    elif direction == "left":
        x -= space_size
    elif direction == "right":
        x += space_size

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + space_size, y + space_size, fill=snake_color)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(speed, next_turn, snake, food)


def change_direction(new_direction):

  global direction

  if new_direction == 'left':
      if direction != 'right':
          direction = new_direction
  elif new_direction == 'right':
      if direction != 'left':
          direction = new_direction
  elif new_direction == 'up':
      if direction != 'down':
          direction = new_direction
  elif new_direction == 'down':
      if direction != 'up':
          direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= g_width:
        return True
    elif y < 0 or y >= g_height:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("Game Over")
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 3,font=('consolas',80), text="GAME OVER!", fill="#F5F5DC", tag="gameover!")
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 30),
                       text="Your Final Score:{}".format(score),
                       fill="#F5F5DC", tag="finalscore")

    leave = Button(window, text='EXIT', font='Avenir 15 bold', relief='flat', padx=20, pady=10, bg='#40444B', fg='#F5F5DC', bd=0,
                   command=main_menu)
    leave.place(x=600, y=450)
    leave.config(activebackground='#F5F5DC')


def main_menu():
    window.destroy()
    import main

window = Tk()
window.title("ANACONDA")
window.resizable(False, False)

score = 0
direction = "right"

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=background_color, height=g_height, width=g_width)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int ((screen_width/2) - (window_width/2))
y = int ((screen_height/10) - (window_height/10))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()