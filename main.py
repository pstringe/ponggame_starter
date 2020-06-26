from tkinter import *
import time

tk = Tk()

# change the game title
tk.title('GAME')

# create a canvas for the window
canvas = Canvas(tk, width=800, height=600)
canvas.pack()

################################
# Lesson 5 Objectives
## create boundries for the paddle
## define ball class
## make the ball move
################################

# Define Paddle class
class Paddle:
  #initialization funciton called when new paddle is created
  def __init__(self, i_canvas):
    self.x = 0
    self.canvas = i_canvas

    # 3. Define canvas_width
    self.canvas_width = 800
    self.id = canvas.create_rectangle(0, 0, 200, 10, fill='black')
    self.canvas.move(self.id, 200, 200)
    
    self.canvas.bind_all('<KeyPress-Left>', self.goLeft)
    self.canvas.bind_all('<KeyPress-Right>', self.goRight)

  def goLeft(self, e):
      self.x = -10

  def goRight(self, e):
      self.x = 10

  # define update_position function
  def update_position(self):
      self.canvas.move(self.id, self.x, 0)
      
      # 1. save the current position in a variable
      position = self.canvas.coords(self.id)

      # 2. add a condition for setting x to 0, stopping the paddle
      if position[0] < 0:
          self.x = 0
      elif position[2] > self.canvas_width:
          self.x = 0

# 5. Define the ball class

## Define the initialization function

## Define the update postition function

### add hit platform conditional to ball function.

## Define the collision function
paddle = Paddle(canvas) #create a paddle

while True:
    tk.update_idletasks()
    # 6. Update Ball Position

    paddle.update_position()
    tk.update()
