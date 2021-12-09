from PIL import Image,ImageTk
import random as rand
import turtle as trtl
# import required module
import os
from playsound import playsound
import tkinter.messagebox


vroomVroom_wn = trtl.Screen()
#si = tk.Tk()
si = trtl.Turtle()
caller = trtl.Turtle()
st = trtl.Turtle()
rSt = trtl.Turtle()
user = trtl.Turtle()
score = trtl.Turtle()
count = 0
caller_list = ["abrupt stop", "speed bump","right","left","go"]
caller_txt = []
Message ="Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP"
tkinter.messagebox.showinfo('Directions','Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP')




#vroomVroom_wn = tk.Tk()
#vroomVroom_wn.screensize("400x400")
# --- Window Creator ---
vroomVroom_wn.title("Vroom Vroom: BTS Edition")
#vroomVroom_wn.window_height(150)
vroomVroom_wn.setup(height=500,width=500)

caller_img ="huh_resize.gif"
#user_label = Label(vroomVroom_wn,image=caller_img)

# ---IMages ---
as_img = "as_resize.gif"
vroomVroom_wn.addshape(as_img)
sb_img = "cooky_up.gif"
vroomVroom_wn.addshape(sb_img)
r_img = "right_chim.gif"
vroomVroom_wn.addshape(r_img)
l_img = "cooky_left.gif"
vroomVroom_wn.addshape(l_img)
go_img = "go_resize.gif"
vroomVroom_wn.addshape(go_img)

# --- Functions ---
def createCaller():
    caller_img = "huh_resize.gif"
    #caller_pic = "huh_resize.gif"
    vroomVroom_wn.addshape(caller_img)
    caller.shape(caller_img)
    #caller.shapesize(10)
    x = -191
    y = 180
    caller.pu()
    caller.goto(x,y)
    si.pu()
    si.goto(-120,200)
    score.pu()
    score.goto(187,200)
    score.write(count,font=("Arial",15))

def resetCaller():
    si.clear()
def createStart_btn():
    start_pic = "st_resize.gif"
    vroomVroom_wn.addshape(start_pic)
    st.shape(start_pic)
    st.pu()
    st.goto(0,180)

def createRestart_btn():
    restart_pic = "restart_resized.gif"
    vroomVroom_wn.addshape(restart_pic)
    rSt.shape(restart_pic)
    rSt.pu()
    rSt.goto(0,180)


def createUser():
    user_pic = "plyr_resize.gif"
    vroomVroom_wn.addshape(user_pic)
    user.shape(user_pic)
    user.pu()
    user.goto(0,-50)

def startPress():
    #playsound('vvv.wav')
    file = "vvvcopy.wav"
    #print('playing sound using native player')
    playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vvvcopy.wav')
    vroomVroom_wn.delay(5)
    rSt.st()
    gameMain()

def rStPress():
    #rSt.ht()
    si.clear()
    st.st()
    
def callerChoose():
    st.ht()
    si.ht()
    caller_txt = rand.choice(caller_list)
    si.write(caller_txt,font=("Arial",15))
    callerSound()
    vroomVroom_wn.delay(5)
    resetCaller()
    cScore()



def callerSound():
    #caller_pic = "huh_resize.gif"

    if caller_txt == caller_list[0]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vD_AS.wav')
        caller.shape(as_img)
    elif caller_txt == caller_list[1]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vS_sb.wav')
        caller.shape(sb_img)
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[2]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vR.wav')
        caller.shape(r_img)
    elif caller_txt == caller_list[3]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vL.wav')
        caller.shape(l_img)
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/vUp_go.wav')
        caller.shape(go_img)

def gameMain():
    callerChoose()

def main():
    createCaller()
    createRestart_btn()
    createUser()
    createStart_btn()
    gameMain()
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

def cScore():
    global count
    if user.shape() == caller.shape():
        count += 1
    else:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/error.wav')
        pass
    #gameMain()
def checkScore():
    global count
    if user.shape(as_img) == caller.shape(as_img): #or user.shape(sb_img) == caller.shape(sb_img) or user.shape(r_img) == caller.shape(r_img) or user.shape(l_img) == caller.shape(l_img) or user.shape(go_img) == caller.shape(go_img)
        count += 1
        gameMain()
    elif user.shape(sb_img) == caller.shape(sb_img):
        count += 1
        gameMain()
    elif user.shape(r_img) == caller.shape(r_img):
        count += 1
        gameMain()
    elif user.shape(l_img) == caller.shape(l_img):
        count += 1
        gameMain()
    elif user.shape(go_img) == caller.shape(go_img):
        count += 1
        gameMain()
    else:
        playsound('/Users/khaase/Desktop/AP CS Principles - Haase/Lesson 1.2 Abstraction/1.2.5 Shall we Play a Game/Vroom Vroom/error.wav')
        gameMain()
    print(count)
    



#vroomVroom_wn = trtl.Screen()
vroomVroom_wn.onkeypress(abruptStop(),"Down")
vroomVroom_wn.onkeypress(speedBump(),"Shift_R")
vroomVroom_wn.onkeypress(rightTurn(),"Right")
vroomVroom_wn.onkeypress(leftTurn(),"Left")
vroomVroom_wn.onkeypress(goFD(),"Up")
rSt.onclick(rStPress())
st.onclick(startPress())
createCaller()
createRestart_btn()
createUser()
createStart_btn()
#gameMain()

vroomVroom_wn.mainloop()