from operator import mod
import requests
import re
from variables import POWERS, REGEX_PATTERN, INDEX, FOLDER_INDEX
import time
from concurrent.futures import ThreadPoolExecutor
import os

HASH_CODES = set()
MODULO = 2147483647
PATH = "Links/"
nr = 0

def DeleteAllFiles():
    for file_name in os.listdir(PATH):
        file = PATH + file_name
        if os.path.isfile(file):
            os.remove(file)

def CreateHash(link):
    hashCode = 0
    i = 0
    for chr in link:
        if chr != '/':
            hashCode += (ord(chr) * POWERS[i]) % MODULO
            hashCode = hashCode % MODULO
            i += 1
    return hashCode

def GetSessionLinks(session, base_url):
    global nr
    global FOLDER_INDEX
    ok = 0
    with open(PATH + str(FOLDER_INDEX) + '.in', 'w') as outFILE:
        global INDEX
        page = session.get(base_url).text
        for link in re.finditer(REGEX_PATTERN, page):
            url = link.group()
            hash_code = CreateHash(url)
            if hash_code not in HASH_CODES:
                HASH_CODES.add(hash_code)
                outFILE.write(url)
                outFILE.write('\n')
                nr += 1
                ok = 1
    if ok:
        FOLDER_INDEX += 1

def StartNewCrawling(base_link, timeout):
    DeleteAllFiles()
    global INDEX
    global FOLDER_INDEX
    INDEX = 1
    FOLDER_INDEX = 1
    with open(PATH + str(FOLDER_INDEX) + '.in', 'w') as outFile:
        outFile.write(base_link)
    FOLDER_INDEX = 2
    Session = requests.Session()
    start_time = time.time()
    while(time.time() - start_time <= timeout):
        with open(PATH + str(INDEX) + '.in', 'r') as inFILE:
            for link in inFILE.readlines():
                #Session = requests.Session()
                GetSessionLinks(Session, link)
        INDEX += 1


    


if __name__ == '__main__':
    # DeleteAllFiles()
    start_time = time.time()

    StartNewCrawling('https://stirileprotv.ro/', 10)
    # # session = requests.Session()
    # # GetSessionLink(session, 'https://stirileprotv.ro/')
    print(nr)
    print("--- %s seconds ---" % (time.time() - start_time))
    