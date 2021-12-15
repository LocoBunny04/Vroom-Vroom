from PIL import Image,ImageTk
import random as rand
import turtle as trtl
# import required module
from playsound import playsound
import tkinter.messagebox
from pynput.keyboard import Key, Listener




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
tkinter.messagebox.showinfo('Directions','Abrupt stop = DOWN speed bump = Return right = RIGHT left = LEFT go =UP \nPress Backspace to start')

attempt = 0
user_txt = ''
def usL():
    global user_txt
    user_txt = 'left'
def usR():
    global user_txt
    user_txt = 'right'
def usAS():
    global user_txt
    user_txt = 'abrupt stop'
def usSB():
    global user_txt
    user_txt = 'speed bump'
def usGo():
    global user_txt
    user_txt = 'go'



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
#caller.ht()
# --- Functions ---
x = -191
y = 180
caller.pu()
caller.goto(x,y)
si.pu()
si.ht()
si.goto(-120,150)



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

def startPress(x, y):
    global attempt
    caller.shape(caller_img)
    user.shape(user_pic)
    caller.st()
    st.ht()
    rSt.st()
    #print('playing sound using native player')
    playsound('vvvcopy.wav')
    attempt = 0
    wn.delay(10)
    si.clear()
    # callerChoose()
    gameMain()
    # callerSoundOs()

def rStPress(x, y):
    global point 
    global count
    global attempt
    rSt.ht()
    st.st()
    si.clear()
    caller.shape(caller_img)
    point.clear()
    count = 0
    user.shape(user_pic)
    attempt = 100

point.pu()
point.goto(150,180)

#    gameMain()
def callerChoose():
    global point
    global caller_txt
    si.ht()
    caller_txt = rand.choice(caller_list)
    si.write(caller_txt,font=("Arial",15))
    print(caller_txt)
    callerSoundOs()
    wn.delay(100)
    whilePoint()
    point.ht()
    print ('point: ', count)
    #wn.delay(10)
    #si.ht()

def callerSoundOs():
    global caller_txt
    #print("cSOs")
    #caller_pic = "huh_resize.gif"
    if caller_txt == caller_list[0]:
        #print("ab")
        cAs(),playsound('vDa_AS.wav')
        
    elif caller_txt == caller_list[1]:
        #print("sb")
        cSb(),playsound('vS_sb.wav')
        
    elif caller_txt == caller_list[2]:
        #print("r")
        cR(),playsound('vR.wav')
        
    elif caller_txt == caller_list[3]:
        #print("l")
        cL(),playsound('vL.wav')
        #vroomVroom_wn.addshape(caller_pic)
        #caller.shape(caller_pic)
    elif caller_txt == caller_list[4]:
        #print("g")
        cGo(),playsound('vUp_go.wav')

#user change
def abruptStop():
    global user_txt
    user.shape(as_img)
    print('user',user_txt)
    usL()
def speedBump():
    global user_txt
    user.shape(sb_img)
    print('user',user_txt)
    usSB()
def rightTurn():
    global user_txt
    user.shape(r_img)
    print('user',user_txt)
    usR() 
def leftTurn():
    global user_txt
    user.shape(l_img)
    print('user',user_txt)
    usL()
def goFD():
    global user_txt
    user.shape(go_img)
    print('user',user_txt)
    usGo()
#caller change
def cAs():
    caller.shape(as_img)
    print('caller',caller_txt)
def cSb():
    caller.shape(sb_img)
    print('caller',caller_txt)
def cR():
    caller.shape(r_img)
    print('caller',caller_txt)
def cL():
    caller.shape(l_img)
    print('caller',caller_txt)
def cGo():
    caller.shape(go_img)
    print('caller',caller_txt)

def gameMain():
    user.shape(user_pic)
    caller.st()
    si.st()
    point.st()
    #caller.shapesize(10)
    if attempt < 100:
        wn.delay(200)
        callerChoose()
    #callerSoundOs()
#callerSound()


def whilePoint():
    global count, attempt
    global  user_txt, caller_txt
    wn.delay(100)
    print(user_txt,"wP")
    print(caller_txt,"wP")
    point.ht()
    if user_txt == caller_txt:
        wn.delay(150)
        count = count + 1
        point.clear()
        point.write(str(count),font=("Arial",15))
        wn.delay(20)
        user.shape(user_pic)
    else:
        wn.delay(150)
        count = count - 1
        ah = str(count)
        point.clear()
        point.write(ah,font=("Arial",15))
        wn.delay(50)
        user.shape(user_pic)
    attempt +=1
    print('attempt',attempt)
    si.clear()
    point.ht()
    gameMain()


# gameMain()
st.onclick(startPress)
rSt.onclick(rStPress)

wn.onkeypress(abruptStop,'Down')
wn.onkeypress(speedBump,'Return')
wn.onkeypress(gameMain,'BackSpace')
wn.onkeypress(rightTurn,'Right')
wn.onkeypress(leftTurn,'Left')
wn.onkeypress(goFD,'Up')

# createCaller()
# createRestart_btn()
# createUser()
# createStart_btn()

wn.listen()
wn.mainloop()