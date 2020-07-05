#!/usr/bin/python3
# ADDING FROM LIST SHOULD NEVER REQUIRE A LICENSE
# Turns out this also works well for QRadar Searches <3 
import time
import sys
try:
    import pyautogui as gui
except Exception as e:
    print ('[+] Please install pyautogui so that this script can function')
    sys.exit(1)


# The Array that entry data is written to 
dataArray = []
# Set so that loops can do their thing
x = 0

# Please have a file named dataList.txt in the same directory as the script
file = open('dataList.txt', 'r')
for line in file:
    dataArray.append(line.strip())
dataCount = len(dataArray)

#This section of the script is to calibrate the mouse so that values are defined at the beginning of the script
print ("[+] Please go to the \"Simple List\" options in BurpSuite")
print ('[+] Within 10 seconds place your cursor in the center of the blank text box of the \"Enter a new item\" field')
input('[*] Press ENTER when ready')
time.sleep(10)
valueBox = gui.position()
print ('[+] Calibrated mouse for \"Enter a new item\" field')
print ("Now within 5 seconds place your cursor on the \"Add\" button to the left of the \"Enter a new item\" field")
input('[*] Press ENTER when ready')
time.sleep(5)
plusSign = gui.position()
print ('[+] Calibrated mouse for \"Add\" button')
print ("[+] Starting...")

while x != dataCount:
    # Change this value for gui.position() if it doesnt work the first time (For Search Box)
    gui.click(valueBox)
    gui.typewrite(dataArray[x])
    time.sleep(.5)
    # Change this value for gui.position() if it doesnt work the first time (For Plus Sign)
    gui.click(plusSign)
    print ('[+] Added {0}'.format(dataArray[x]))
    x += 1

print ("[+] Done.... Cheers... <3")