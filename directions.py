import turtle as trtl
import random
import time
import os

# --- create variables ---
speaker = trtl.Turtle()
count = 0
# direct = trtl.Turtle()
direct = " "
signal = ("left", "right", "abrupt stop", "go","speed bump")

# --- Functions ---

   
# --- do stuff ---
for count in range(0, 10):
    direct += random.choice(signal)
    for signal in direct:
        print("Vroom Vroom: "+ signal)
        #time .sleep(1.5)
        #os.system("cls")
    guess = input("Repeat: ")
    #os.system("cls")
    if guess != direct:
        break

print("Game Over! Your final score is: {count}!")






wn = trtl.Screen()
wn.mainloop()