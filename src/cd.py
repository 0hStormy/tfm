##################################################
#                                                #
# File by 0Stormy                                #
# Github: https://github.com/Kinda-Stormy/tfm    #
#                                                #
##################################################

# Packages
import os
import keyboard

for each in range(5):
    keyboard.send('backspace')
dirInput = input(f'Directory:')
try:
    with open('tfm', 'w') as f:
        f.write(dirInput)
except:
    print("Can't open tempfile")