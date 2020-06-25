from tkinter import *
import time
tk = Tk()

# change the game title
tk.title('GAME')

# create a canvas for the window
canvas = Canvas(tk, width=800, height=600)
canvas.pack()

##################################
# Lesson 3 Objectives
## Learn about OOP
## experiment with classes
## use the arrow keys to trigger movment
## define two funcitons for left and right movement

##################################

## Previous Lesson



# 1. Define Paddle class
class Paddle:
  def __init__(self, i_canvas):
    self.canvas = i_canvas
    self.id = canvas.create_rectangle(0, 0, 200, 10, fill='black')
    canvas.move(self.id, 200, 200)
  

'''
def goLeft(e):
    x = -10


def goRight(e):
    x = 10
'''
# 2. Instanciate the paddle object
paddle = Paddle(canvas)

while True:
    tk.update_idletasks()

    # 3. update the posisiton of the paddle object
    
    #tk.bind('<KeyPress-Down>', move)
    tk.update()
