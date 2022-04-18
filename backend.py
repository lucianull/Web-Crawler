from lib2to3.pgen2.token import RPAR
import os
from tkinter import Pack
from variables import PATH

def RunScript(root_link, timeout):
    with open("data.txt", 'w') as outFILE:
        outFILE.write(root_link)
        outFILE.write('\n')
        outFILE.write(timeout)
    # subprocess.call('request_module.py', shell=False)
    os.system('python request_module.py')

def OpenFolder():
    os.chdir(r'Links')
    os.system(r'links.txt')

def GetLinksNumber():
    i = 0
    with open(PATH, 'r') as inFILE:
        for link in inFILE.readlines():
            i += 1
    return i