import serial
import pyautogui

arduino=serial.Serial('COM4', 9600)

while 1:
    incoming_Data=arduino.readline()
    if 'up' in incoming_Data.decode('utf-8'):  
        pyautogui.press('up')
    else:
        pyautogui.press('down')
    incoming_Data="" 