#probably a better way to serialize the imports but im a loser chud so this works

import time
import colorama
from colorama import Fore, Style, init
import random
import os
import sys
import keyboard
import pynput
import pynput.keyboard
from pynput.keyboard import Key, Controller
import array
import pyautogui
from PIL import ImageGrab
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Grow a Garden AFK Tool for Roblox")

def aesthetics2(string):
    while True:
        for Character in string:
            sys.stdout.write(Character)
            sys.stdout.flush()
            time.sleep(0.05)
            os.system('cls')

# init colorama but its commented out for now cause its less important than func
init()

def aesthetics(string):
    for Character in string:
        sys.stdout.write(Character)
        sys.stdout.flush()
        time.sleep(0.03)

# make the antiafk first i guesss

def AntiAFK():
    interval = 0.8
    inputs = ['w', 'a', 's', 'd'] * 3
    
    while True:
        if keyboard.is_pressed('b'):
            print("AntiAFK terminated")
            break

        random_press = random.choice(inputs)
        keyboard.press(random_press)
        time.sleep(0.05)
        keyboard.release(random_press)
        time.sleep(interval)


aesthetics(Fore.LIGHTMAGENTA_EX + ">>> STARTING TOOL YOU CHUD...")
time.sleep(1)
os.system('cls')

start = input(Fore.GREEN + ">>> ENTER YOUR KEYBIND TO START: ") # for now keybinds are hardcoded
if start.lower() == "c":
    while True:
        aesthetics(Fore.LIGHTMAGENTA_EX + "\n\nWORKING! YOU MAY NOW MINIMZE THIS WINDOW! :)")
        AntiAFK()
else:
    exit()
