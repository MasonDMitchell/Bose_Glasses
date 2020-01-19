import pyautogui
import math
import keyboard
from read import angles 
pyautogui.FAILSAFE = False 
x, y = pyautogui.size()

mppi = (math.sqrt(x**2 + y**2))/13.3

distFromComp = 15*mppi #pixels 

while True:
    
    readLine = angles()
    
    horzAng = readLine[1]
    
    horzDelt = x//2 + distFromComp*math.tan(horzAng)

    vertAng = readLine[2]
     
    vertDelt = y//2 + distFromComp*math.tan(vertAng)


    pyautogui.moveTo(horzDelt, vertDelt)
    
    #COMBINATIONS = [
    #        {keyboard.Key.shift, keyboard.KeyCode(char = 'q')},
    #        {keyboard.Key.shift, keyboard.KeyCode (char = 'Q')}] 
    
    if keyboard.is_pressed('q') and keyboard.is_pressed('shift'):
        break 
