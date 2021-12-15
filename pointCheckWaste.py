def on_key_press(self, symbol,modifier):
    if symbol == arcade.key.LEFT:
        direct == symbol
    elif symbol == arcade.key.RIGHT:
        direct == symbol
    elif symbol == arcade.key.UP:
        direct == symbol
    elif symbol == arcade.key.DOWN:
        direct == symbol
    elif symbol == arcade.key.RSHIFT:
        direct == symbol
def pointSys():           
    global count
    global point
    point.st()
    print("po")
    if caller_txt =='left' and user.shape(l_img):
        count +=1
        point = int(count)
    elif caller_txt == 'right' and user.shape(r_img):
        count +=1
        point = int(count)
    elif caller_txt == 'abrupt stop' and user.shape(as_img):
        count +=1
        point =int(count)
    elif caller_txt == 'speed bump' and user.shape(sb_img):
        count +=1
        point =int(count)
    elif caller_txt == 'go' and user.shape(go_img):
        count += 1
        point =int(count)
    else:
        print("wrong")
        count = count - 1
    caller.shape(caller_img)
    si.clear()
    user.shape(user_pic)
    print(count)
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