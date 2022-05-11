from lib2to3.pgen2.token import RPAR
import os
import subprocess
import sys
from tkinter import Pack
from variables import PATH
import platform

def RunScript(root_link, timeout):
    with open("data.txt", 'w') as outFILE:
        outFILE.write(root_link)
        outFILE.write('\n')
        outFILE.write(timeout)
    # subprocess.run('request_module.py', shell=True)
    os.system('python request_module.py')

def OpenFolder():
    if platform.system() == 'Windows':
        # subprocess.run('links.txt', shell=True)
        os.system('links.txt')
    if platform.system() == 'Linux':
        # subprocess.call('xdg-open links.txt', shell=False)
        os.system('xdg-open links.txt')

def GetLinksNumber():
    i = 0
    with open(PATH, 'r') as inFILE:
        for link in inFILE.readlines():
            i += 1
    return i