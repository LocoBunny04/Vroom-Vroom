from PIL import Image,ImageTk
import random as rand
import turtle as trtl
# import required module
import os
from playsound import playsound
import tkinter.messagebox


wn = trtl.Screen()
#si = tk.Tk()
si = trtl.Turtle()
caller = trtl.Turtle()
st = trtl.Turtle()
rSt = trtl.Turtle()
user = trtl.Turtle()
#score = trtl.Turtle()
count = 0
caller_list = ["abrupt stop", "speed bump","right","left","go"]
caller_txt = []
#Message ="Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP"
tkinter.messagebox.showinfo('Directions','Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP')




#wn = tk.Tk()
#wn.screensize("400x400")
# --- Window Creator ---
wn.title("Vroom Vroom: BTS Edition")
#wn.window_height(150)
wn.setup(height=500,width=500)

caller_img ="huh_resize.gif"
#user_label = Label(wn,image=caller_img)

# ---IMages ---
as_img = "vAb.gif"
wn.addshape(as_img)
sb_img = "vSb_resize.gif"
wn.addshape(sb_img)
r_img = "right_resize.gif"
wn.addshape(r_img)
l_img = "vL.gif"
wn.addshape(l_img)
go_img = "go_resize.gif"
wn.addshape(go_img)


# --- Functions ---


def startPress(x, y):
    st.ht()
    rSt.st()
    #print('playing sound using native player')
    playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vvvcopy.wav')
    wn.delay(10)
    si.clear()
    callerChoose()
    

def rStPress(x, y):
    st.st()
    si.clear()
#    gameMain()
    
def callerChoose():
    #st.ht()
    si.ht()
    caller_txt = rand.choice(caller_list)
    callerSound()
    si.write(caller_txt,font=("Arial",15))
    
    wn.delay(10)
    #si.ht()
    
def callerSound():
    #caller_pic = "huh_resize.gif"

    if caller_txt == caller_list[0]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vD_AS.wav')
        #caller.shape(as_img)
    elif caller_txt == caller_list[1]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vS_sb.wav')
        #caller.shape(sb_img)
    elif caller_txt == caller_list[2]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vR.wav')
        #caller.shape(r_img)
    elif caller_txt == caller_list[3]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vL.wav')
        #caller.shape(l_img)
        #wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vUp_go.wav')
        #caller.shape(go_img)
    else:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vvvcopy.wav')
    

def gameMain():
    caller_img = "huh_resize.gif"
#caller_pic = "huh_resize.gif"
wn.addshape(caller_img)
caller.shape(caller_img)
#caller.shapesize(10)
x = -191
y = 180
caller.pu()
caller.goto(x,y)
si.pu()
si.ht()
si.goto(-120,150)

'''def resetCaller():
si.clear()
callerChoose()'''

restart_pic = "restart_resized.gif"
wn.addshape(restart_pic)
rSt.shape(restart_pic)
rSt.pu()
rSt.goto(0,180)

start_pic = "st_resize.gif"
wn.addshape(start_pic)
st.shape(start_pic)
st.pu()
st.goto(0,180)

user_pic = "plyr_resize.gif"
wn.addshape(user_pic)
user.shape(user_pic)
user.pu()
user.goto(0,-50)


callerChoose()
callerSound()

def abruptStop():
   user.shape(as_img)
def speedBump():
    user.shape(sb_img)
def rightTurn():
    user.shape(r_img)  
def leftTurn():
    user.shape(l_img)
def goFD():
    user.shape(go_img)

gameMain()
st.onclick(startPress)
rSt.onclick(rStPress)

wn.onkeypress(abruptStop,'Down')
wn.onkeypress(speedBump,'Return')
wn.onkeypress(rightTurn,'Right')
wn.onkeypress(leftTurn,'Left')
wn.onkeypress(goFD,'Up')

# createCaller()
# createRestart_btn()
# createUser()
# createStart_btn()

wn.listen()
wn.mainloop()