from base64 import decode
from lib2to3.pgen2.token import RPAR
import os
import subprocess
import sys
from tkinter import Pack
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
    inFILE = open('links.txt', 'r')
    return len(inFILE.readlines())

if __name__ == '__main__':
    print(GetLinksNumber())