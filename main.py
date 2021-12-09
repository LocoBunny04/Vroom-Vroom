import turtle as trtl
import math
import random as rand
from pic_vari import right_pic
from pic_vari import left_pic
from pic_vari import stop_pic
from pic_vari import bump_pic
from pic_vari import go_pic

play = trtl.Turtle()
simon = trtl.Turtle()
#-----setup-----

# --- turn left ---
left_pic = "right.PNG" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(right_pic) # Make the screen aware of the new file

# --- turn right ---
right_pic = "left.PNG" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(left_pic) # Make the screen aware of the new file

#left = trtl.Turtle()

# --- abrupt stop ---
stop_pic = "forward.PNG" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(stop_pic) # Make the screen aware of the new file

#stop = trtl.Turtle()

# --- go ---
go_pic = "back.PNG" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(go_pic) # Make the screen aware of the new file

#go = trtl.Turtle()

# --- speed bump ---
bump_pic = "jump.PNG" # Store the file name of your shape

wn = trtl.Screen()
wn.addshape(bump_pic) # Make the screen aware of the new file

#jump = trtl.Turtle()
wn.addshape(bump_pic)


#function
def draw_user():
    play.shape(left_pic)
    wn.update()
