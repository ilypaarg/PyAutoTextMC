# Im pretty sure I always start with this import but who cares.
import time
import colorama
from colorama import Fore, Style, init
import ctypes
import os
import sys
import pynput
from pynput import keyboard
import keyboard
from pynput.keyboard import Key, Controller, Listener
import linecache


# Name the controller for pynput
Alphabet = Controller()

# Create a typing simulation for text
def TEXT_TYPING_SIM(STRING):

    for Character in STRING:
        sys.stdout.write(Character)
        sys.stdout.flush()
        time.sleep(0.03)


        
# Create looping console title animation
# Please dont make fun of me.

os.system('cls')

print(Fore.LIGHTYELLOW_EX + "Look at the top of the window! :) ^^^")

for wtf in range(1):
    ctypes.windll.kernel32.SetConsoleTitleW("A")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Au")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Aut")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto L")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Lo")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Los")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Lose")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser -")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - C")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Co")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Cod")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Code")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded b")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by N")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nu")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nug")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nugs")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nugs ")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nugs <")
    time.sleep(0.02)
    ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nugs <3")
    time.sleep(1)

os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW("Auto Loser - Coded by Nugs | Multi-purpose Minecraft mod")

time.sleep(1)
print(Fore.LIGHTRED_EX + """
           _____   _____
          /     \ /     \ 
     ,   |       '       |
     I __L________       L__
O====IE__________/     ./___>
     I      \.       ./
     `        \.   ./
                \ /
                 '  Nugs Development <3
""" + "\n\n")
time.sleep(1)

TEXT_TYPING_SIM(Fore.LIGHTMAGENTA_EX + ">>> Welcome to the 'Auto Loser' mod.\n\n")
time.sleep(1)
TEXT_TYPING_SIM(Fore.LIGHTMAGENTA_EX + ">>> In this mod, you can bind a key and it will type anything of your choice in minecraft chat.\n\n")
time.sleep(1)
TEXT_TYPING_SIM(Fore.LIGHTMAGENTA_EX + ">>> Let's get started, shall we? :)")
time.sleep(1)

TEXT_TYPING_SIM(Fore.GREEN + "\n\n>>> Working :) ")


# Empty dictionary used to pass key binds into
KEY_BINDS_LIST = {}

with open('AutoLoserSettings.txt', 'r') as SETTINGS_FILE:
    
    READ_KEY_CHOICE = linecache.getline('AutoLoserSettings.txt', 1)
    READ_TEXT_CHOICE = linecache.getline('AutoLoserSettings.txt', 2)

    READ_KEY_CHOICE2 = linecache.getline('AutoLoserSettings.txt', 3)
    READ_TEXT_CHOICE2 = linecache.getline('AutoLoserSettings.txt', 4)

    READ_KEY_CHOICE3 = linecache.getline('AutoLoserSettings.txt', 5)
    READ_TEXT_CHOICE3 = linecache.getline('AutoLoserSettings.txt', 6)

    READ_KEY_CHOICE4 = linecache.getline('AutoLoserSettings.txt', 7)
    READ_TEXT_CHOICE4 = linecache.getline('AutoLoserSettings.txt', 8)

    READ_KEY_CHOICE5 = linecache.getline('AutoLoserSettings.txt', 9)
    READ_TEXT_CHOICE5 = linecache.getline('AutoLoserSettings.txt', 10)

    READ_KEY_CHOICE6 = linecache.getline('AutoLoserSettings.txt', 11)
    READ_TEXT_CHOICE6 = linecache.getline('AutoLoserSettings.txt', 12)

    READ_KEY_CHOICE7 = linecache.getline('AutoLoserSettings.txt', 13)
    READ_TEXT_CHOICE7 = linecache.getline('AutoLoserSettings.txt', 14)

    READ_KEY_CHOICE8 = linecache.getline('AutoLoserSettings.txt', 15)
    READ_TEXT_CHOICE8 = linecache.getline('AutoLoserSettings.txt', 16)

    READ_KEY_CHOICE9 = linecache.getline('AutoLoserSettings.txt', 17)
    READ_TEXT_CHOICE9 = linecache.getline('AutoLoserSettings.txt', 18)

    READ_KEY_CHOICE10 = linecache.getline('AutoLoserSettings.txt', 19)
    READ_TEXT_CHOICE10 = linecache.getline('AutoLoserSettings.txt', 20)


    KEY_CHOICE = READ_KEY_CHOICE[-2]
    TEXT_CHOICE = READ_TEXT_CHOICE[14:-1]

    KEY_CHOICE2 = READ_KEY_CHOICE2[-2]
    TEXT_CHOICE2 = READ_TEXT_CHOICE2[15:-1]

    KEY_CHOICE3 = READ_KEY_CHOICE3[-2]
    TEXT_CHOICE3 = READ_TEXT_CHOICE3[15:-1]

    KEY_CHOICE4 = READ_KEY_CHOICE4[-2]
    TEXT_CHOICE4 = READ_TEXT_CHOICE4[15:-1]

    KEY_CHOICE5 = READ_KEY_CHOICE5[-2]
    TEXT_CHOICE5 = READ_TEXT_CHOICE5[15:-1]

    KEY_CHOICE6 = READ_KEY_CHOICE6[-2]
    TEXT_CHOICE6 = READ_TEXT_CHOICE6[15:-1]

    KEY_CHOICE7 = READ_KEY_CHOICE7[-2]
    TEXT_CHOICE7 = READ_TEXT_CHOICE7[15:-1]

    KEY_CHOICE8 = READ_KEY_CHOICE8[-2]
    TEXT_CHOICE8 = READ_TEXT_CHOICE8[15:-1]

    KEY_CHOICE9 = READ_KEY_CHOICE9[-2]
    TEXT_CHOICE9 = READ_TEXT_CHOICE9[15:-1]

    KEY_CHOICE10 = READ_KEY_CHOICE10[-2]
    TEXT_CHOICE10 = READ_TEXT_CHOICE10[16:-1]
    
    KEY_BINDS_LIST[KEY_CHOICE] = TEXT_CHOICE
    KEY_BINDS_LIST[KEY_CHOICE2] = TEXT_CHOICE2
    KEY_BINDS_LIST[KEY_CHOICE3] = TEXT_CHOICE3
    KEY_BINDS_LIST[KEY_CHOICE4] = TEXT_CHOICE4
    KEY_BINDS_LIST[KEY_CHOICE5] = TEXT_CHOICE5
    KEY_BINDS_LIST[KEY_CHOICE6] = TEXT_CHOICE6
    KEY_BINDS_LIST[KEY_CHOICE7] = TEXT_CHOICE7
    KEY_BINDS_LIST[KEY_CHOICE8] = TEXT_CHOICE8
    KEY_BINDS_LIST[KEY_CHOICE9] = TEXT_CHOICE9
    KEY_BINDS_LIST[KEY_CHOICE10] = TEXT_CHOICE10

    SETTINGS_FILE.close()

while True:

    KEY = keyboard.read_key()

    if KEY in KEY_BINDS_LIST and KEY != None:
        Alphabet.press('t')
        time.sleep(0.08)
        Alphabet.release('t')
        Alphabet.type(KEY_BINDS_LIST.get(KEY))
        Alphabet.press(Key.enter)
        Alphabet.release(Key.enter)
        time.sleep(0.09)
