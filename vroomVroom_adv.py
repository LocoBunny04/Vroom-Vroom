from PIL import Image,ImageTk
import random as rand
import turtle as trtl
# import required module
import os
from playsound import playsound
import tkinter.messagebox
from pynput.keyboard import Key, Listener
import arcade




wn = trtl.Screen()
#si = tk.Tk()
si = trtl.Turtle()
caller = trtl.Turtle()
st = trtl.Turtle()
rSt = trtl.Turtle()
user = trtl.Turtle()
point = trtl.Turtle()
direct = Key 
#score = trtl.Turtle()
count = 0
caller_list = ['abrupt stop', 'speed bump','right','left','go']
caller_txt = []
#Message ="Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP"
tkinter.messagebox.showinfo('Directions','Abrupt stop = DOWN speed bump = SHIFT right = RIGHT left = LEFT go =UP')

attempt = 0
user_txt = []
def usL():
    user_txt = 'left'



#wn = tk.Tk()
#wn.screensize("400x400")
# --- Window Creator ---
wn.title("Vroom Vroom: BTS Edition")
#wn.window_height(150)
wn.setup(height=500,width=500)

#caller_img ="huh_resize.gif"
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
caller_img = "huh_resize.gif"
wn.addshape(caller_img)
point.ht()
caller.ht()
# --- Functions ---
x = -191
y = 180
caller.pu()
caller.goto(x,y)
si.pu()
si.ht()
si.goto(-120,150)

start_pic = "st_resize.gif"
wn.addshape(start_pic)
st.shape(start_pic)
st.pu()
st.goto(0,180)

restart_pic = "restart_resized.gif"
wn.addshape(restart_pic)
rSt.shape(restart_pic)
rSt.pu()
rSt.goto(0,180)


user_pic = "plyr_resize.gif"
wn.addshape(user_pic)
user.shape(user_pic)
user.pu()
user.goto(0,-50)

def startPress(x, y):
    caller.shape(caller_img)
    user.shape(user_pic)
    caller.st()
    st.ht()
    point.st()
    rSt.st()
    #print('playing sound using native player')
    playsound('vvvcopy.wav')
    wn.delay(10)
    si.clear()
    callerChoose()
    # callerSoundOs()

def rStPress(x, y):
    rSt.ht()
    st.st()
    si.clear()
    caller.shape(caller_img)
    user.shape(user_pic)

point.pu()
point.goto(150,180)
point.write(count, font=("Arial",15))

#    gameMain()
    
def callerChoose():
    #st.ht()
    
    global point
    global caller_txt
    si.ht()
    caller_txt = rand.choice(caller_list)
    si.write(caller_txt,font=("Arial",15))
    print(caller_txt)
    callerSoundOs()
    whilePoint()
    #wn.delay(10)
    #si.ht()
    
def callerSound():
    #caller_pic = "huh_resize.gif"
    if caller_txt == caller_list[0]:
        print("Ab")
        playsound('vDa_AS.wav')
        cAs()
    elif caller_txt == caller_list[1]:
        print("sb")
        playsound('vS_sb.wav')
        cSb()
    elif caller_txt == caller_list[2]:
        print("right")
        playsound('vR.wav')
        cR()
    elif caller_txt == caller_list[3]:
        print("left")
        playsound('vL.wav')
        cL()
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        print('go')
        playsound('vUp_go.wav')
        cGo()

def callerSoundOs():
    global caller_txt
    print("cSOs")
    #caller_pic = "huh_resize.gif"
    if caller_txt == caller_list[0]:
        print("ab")
        cAs(),playsound('vDa_AS.wav')
        
    elif caller_txt == caller_list[1]:
        print("sb")
        cSb(),playsound('vS_sb.wav')
        
    elif caller_txt == caller_list[2]:
        print("r")
        cR(),playsound('vR.wav')
        
    elif caller_txt == caller_list[3]:
        print("l")
        cL(),playsound('vL.wav')
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        print("g")
        cGo(),playsound('vUp_go.wav')

def abruptStop():
   user.shape(as_img)
   usL()
def speedBump():
    user.shape(sb_img)
def rightTurn():
    user.shape(r_img)  
def leftTurn():
    user.shape(l_img)
def goFD():
    user.shape(go_img)
def cAs():
    caller.shape(as_img)
def cSb():
    caller.shape(sb_img)
def cR():
    caller.shape(r_img)
def cL():
    caller.shape(l_img)
def cGo():
    caller.shape(go_img)
def gameMain():
    #caller.shapesize(10)
    callerChoose()
    #callerSoundOs()
#callerSound()


def whilePoint():
    global count
    while caller_txt =='left':
        if user.shape != l_img:
            count = count - 1
        else:
            count +=1
    while caller_txt =='right':
        if user.shape != r_img:
            count = count -1
        else: count +=1
    while caller_txt =='abrupt stop':
        if user.shape != as_img:
            count = count - 1
        else: count +=1
    while caller_txt =='speed bump':
        if user.shape != sb_img:
            count = count -1 
        else: count +=1
    point.write(count,font=("Arial",15))

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