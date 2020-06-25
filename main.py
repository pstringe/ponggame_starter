from tkinter import *
import time
tk = Tk()

# change the game title
tk.title('GAME')

# create a canvas for the window
canvas = Canvas(tk, width=800, height=600)
canvas.pack()

################################
# Lesson 4 Objectives
## add go left and go_right methods
## add keybindings
## define update_postion funtion
################################

# Define Paddle class
class Paddle:
  #initialization funciton called when new paddle is created
  def __init__(self, i_canvas):
    self.x = 0
    self.canvas = i_canvas
    self.id = canvas.create_rectangle(0, 0, 200, 10, fill='black')
    self.canvas.move(self.id, 200, 200)
    
    # 2. add keybindings to initialization function
    self.canvas.bind_all('<KeyPress-Left>', self.goLeft)
    self.canvas.bind_all('<KeyPress-Right>', self.goRight)

  # 1. move goLeft and goRight methods into Paddle class
  def goLeft(self, e):
      self.x = -10

  def goRight(self, e):
      self.x = 10

  # define update_position function
  def update_position(self):
      self.canvas.move(self.id, self.x, 0)

paddle = Paddle(canvas) #create a paddle

while True:
    tk.update_idletasks()

    # 4. update the posisiton of the paddle object
    paddle.update_position()    
    tk.update()
