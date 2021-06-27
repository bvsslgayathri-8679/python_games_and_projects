import pyautogui
import win32api,win32con
import keyboard
import time


import pyautogui
from pynput.mouse import Button , Controller
import keyboard

mouse = Controller()
 
# lets make the function to click the button 

def clickTile( x , y ):
    mouse.position = (x , y)
    mouse.click(Button.left , 1)

 

# X:  511 Y:  512 RGB: ( 59,  56,  63)
# X:  402 Y:  517 RGB: (235, 235, 236)
# X:  297 Y:  495 RGB: (235, 235, 236)
# X:  203 Y:  493 RGB: (235, 235, 236)

# y position can be constant


yPosition = 510 

while keyboard.is_pressed("q") == False:
    # check the button value

    try:
        if pyautogui.pixel( 511 , yPosition )[0] == 59:
            clickTile(511 , yPosition)
        if pyautogui.pixel( 402 , yPosition )[0] == 59:
            clickTile(402 , yPosition)
        if pyautogui.pixel( 297 , yPosition )[0] == 59:
            clickTile(297 , yPosition)
        if pyautogui.pixel( 203 , yPosition )[0] == 59:
            clickTile(203 , yPosition)

    except:
        print("could not find the button ")



def playClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(541,354)[0] == 0:
        playClick(541,364)
    if pyautogui.pixel(623,354)[0] == 0:
        playClick(623,364)
    if pyautogui.pixel(720,354)[0] == 0:
        playClick(720,364)
    if pyautogui.pixel(804,354)[0] == 0:
        playClick(804,364)
