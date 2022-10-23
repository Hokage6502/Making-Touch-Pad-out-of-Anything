import subprocess   
import time
import pyautogui
import serial            #See Error Prone Codes[1] below if you could not import this module
from serial import SerialException
#uncomment it if you don't have chrome in your computer. If you have chrome, open the web page #'chrome://dino' and directly run the code
#subprocess.call([r'/Applications/safari.app',  '_blank', 'https://chromedino.com/'])  

time.sleep(6)                 	#give a short time to open and setup all.
print("All sett :)")

#Update with your arduino [port]
ser = serial.Serial(port='COM4', baudrate=9600, timeout=.1)		
#set Serial Baud Rate at the baud rate of your sensor (in my case it's 9600). 
ser.baudrate = '9600'			
# Baud rate roughly means the speed that data is transmitted, 
# and it is a derived value based on the number of symbols transmitted per second. 

while True:       # looping. 
    try:
        h1=ser.readline() 
        print(h1)#reading serial data.
        #decode and make it an int value. See Error prone codes[2] below
        ss = ord(h1.decode().strip()) 
        print(ss) # uncomment this line if you want to check the value of ss
        
        if ss == 49:   # true while obstacle.
            print("Oh :< Jump!! ")
            #print(ss)  uncomment this line if you want to check the value of ss
            pyautogui.press('space')         #Auto press [space] key
            
    except serial.SerialException:
        print(error)       # Maybe don't do this, or mess around with the interval
        continue