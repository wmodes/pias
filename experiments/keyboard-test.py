import keyboard

while True:  #making a loop
    try:  #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('up'): #if key 'up' is pressed.You can use right,left,up,down and others
            print('You Pressed A Key!')
            break #finishing the loop
        else:
            pass
    except:
        break  #if user pressed other than the given key the loop will break