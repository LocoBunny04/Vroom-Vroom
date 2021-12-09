import pyautogui as p
import ctypes
import time
import threading

leftPos = (770,120)
downPos = (895, 120)
upPos = (1000,120)
rightPos = (1130,120)

leftHoldPos = (787,186)
downHoldPos = (894,193)
upHoldPos = (1005,200)
rightHoldPos = (1114,186)

leftCol = (194,75,153)
downCol = (0,255,255)
upCol = (18,250,5)
rightCol = (249,57,63)

leftColS = (226,118,255)
downColS = (61,202,255)
upColS = (133,227,0)
rightColS = (255,136,78)

upPressed = False
downPressed = False
rightPressed = False
leftPressed = False

average = 0
totalTime = 0

#SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseLeft():
    ReleaseKey(30)
def ReleaseDown():
    ReleaseKey(31)
def ReleaseUp():
    ReleaseKey(17)
def ReleaseRight():
    ReleaseKey(32)


while True:
    time1 = time.time()
    try:
        #left arrow
        leftPixel = p.pixel(leftPos[0],leftPos[1])
        if leftPixel == leftCol or leftPixel == leftColS:
            PressKey(30)
            leftPressed = True
        elif leftPressed == True:
            leftPixelHold = p.pixel(leftHoldPos[0],leftHoldPos[1])
            if (leftPixelHold[0] < 150 and leftPixelHold[2] < 150) or leftPixelHold == leftCol or leftPixelHold == leftColS:
                #leftDelay = threading.Timer(.05,ReleaseLeft)
                #leftDelay.start()
                ReleaseKey(30)
                leftPressed = False

        #down arrow
        downPixel = p.pixel(downPos[0],downPos[1])
        if downPixel == downCol or downPixel == downColS:
            PressKey(31)
            downPressed = True
        elif downPressed == True:
            downPixelHold = p.pixel(downHoldPos[0],downHoldPos[1])
            if downPixelHold[2] < 150 or downPixelHold == downCol or downPixelHold == downColS:
                #downDelay = threading.Timer(.05,ReleaseDown)
                #downDelay.start()
                ReleaseKey(31)
                downPressed = False

        #up arrow
        upPixel = p.pixel(upPos[0],upPos[1])
        if upPixel == upCol or upPixel == upColS:
            PressKey(17)
            upPressed = True
        elif upPressed == True:
            upPixelHold = p.pixel(upHoldPos[0],upHoldPos[1])
            if upPixelHold[1] < 150 or upPixelHold == upPixel or upPixelHold == upColS:
                #upDelay = threading.Timer(.05,ReleaseUp)
                #upDelay.start()
                ReleaseKey(17)
                upPressed = False

        #right arrow
        rightPixel = p.pixel(rightPos[0],rightPos[1])
        if rightPixel == rightCol or rightPixel == rightColS:
            PressKey(32)
            rightPressed = True
        elif rightPressed == True:
            rightPixelHold = p.pixel(rightHoldPos[0],rightHoldPos[1])
            if rightPixelHold[0] < 150 or rightPixelHold == rightCol or rightPixelHold == rightColS:
                #rightDelay = threading.Timer(.05,ReleaseRight)
                #rightDelay.start()
                ReleaseKey(32)
                rightPressed = False


    except OSError:
        print("OS Error")
        
    average += 1
    totalTime += time.time() - time1
    print("Average loops per second: " + str(1/(totalTime/average)))