##################################################
#                                                #
# File by 0Stormy                                #
# Github: https://github.com/Kinda-Stormy/tfm    #
#                                                #
##################################################

# Packages
import os
import platform
import keyboard
import time
import cursor
import subprocess
from multiprocessing import Process
from colorama import Fore, Back, Style

# Functions \/

# Draw the topbar
def drawTopBar():
    dirStringLen = len(currentDirectory + ' | Press H For help')
    print(f'{Back.CYAN}{currentDirectory} | Press H For help' + ' ' * (terminalX - dirStringLen) + Style.RESET_ALL)
    
# Create tempfile
def createTempfile():

    try:
        with open('tfm', 'w') as f:
            f.write(os.path.expanduser("~"))
    except:
        print("Can't open tempfile")
# Read tempfile
def readTempfile():
    try:
        with open('tfm', 'r') as f:
            global currentDirectory
            currentDirectory = f.read()
    except:
        print("Can't open tempfile")
        
# Clear the screen    
def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
# Check for key presses
def keyChecker():
    if keyboard.is_pressed("d"):
        subprocess.run(['python', 'cd.py'])
        
# Draw contents
def drawContents():
    folderContents = os.listdir(currentDirectory)
    listLength = len(folderContents)
    terminalX = os.get_terminal_size().columns
    int(terminalX)
    
    for i in range(listLength):
        if os.path.isfile(f'{currentDirectory}/{folderContents[i]}') == False:
            print(Fore.YELLOW, folderContents[i], Style.RESET_ALL)
        else:
            print(Fore.LIGHTBLUE_EX, folderContents[i], Style.RESET_ALL)
        
        if i == (terminalY - 4):
            break
        
# Main loop   
def mainLoop():
    while True:
        readTempfile()
        cursor.hide()
        global terminalX
        global terminalY
        terminalY = os.get_terminal_size().lines
        terminalX = os.get_terminal_size().columns
        int(terminalX)
        int(terminalY)
        drawTopBar()
        drawContents()
        keyChecker()      
        clearScreen()
        
# -------------------- #

createTempfile()

mainLoop()