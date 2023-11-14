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
from colorama import Fore, Back, Style

# Variables
currentDirectory = os.path.expanduser("~")

# Functions \/

# Draw the topbar
def drawTopBar():
    dirStringLen = len(currentDirectory + ' | Press H For help')
    print(f'{Back.CYAN}{currentDirectory} | Press H For help' + ' ' * (terminalX - dirStringLen) + Style.RESET_ALL)

# Clear the screen    
def clearScreen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
        
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
while True:
    cursor.hide()
    terminalY = os.get_terminal_size().lines
    terminalX = os.get_terminal_size().columns
    int(terminalX)
    int(terminalY)
    drawTopBar()
    drawContents()
    time.sleep(0.1)
    clearScreen()