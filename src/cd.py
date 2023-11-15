##################################################
#                                                #
# File by 0Stormy                                #
# Github: https://github.com/Kinda-Stormy/tfm    #
#                                                #
##################################################

# Packages
import keyboard
import os
from colorama import Fore, Back, Style

# Change Directory
keyboard.send('backspace')
dirInput = input(f'Directory:')
print(Style.RESET_ALL)
try:
    with open('tfm', 'w') as f:
        f.write(dirInput)
except:
    print("Can't open tempfile")