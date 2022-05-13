from logging import exception
import threading
import requests
import re
from variables import POWERS, REGEX_PATTERN
import time
from concurrent.futures import ThreadPoolExecutor
import os
from queue import Queue, Empty
import sys

HASH_CODES = set()
MODULO = 2147483647
LINKS_LIST = Queue()
outFILE = open('links.txt', 'w')
EXCEPTIONS = {'js', 'png', 'jpg', 'css', 'jpeg', 'webp', 'xml'}

def CreateHash(link: str) -> int:
    hashCode = 0
    i = 0
    for chr in link:
        if chr != '/':
            hashCode += (ord(chr) * POWERS[i]) % MODULO
            hashCode = hashCode % MODULO
            i += 1
    return hashCode

def GetSufix(string: str) -> str:
    aux = string[-5:]
    if aux[0] == '.':
        return aux[1:]
    if aux[1] == '.':
        return aux[2:]
    if aux[2] == '.':
        return aux[3:]
    return None

def GetSessionLinks(session, base_url: str):
    page = session.get(base_url).text
    for link in re.finditer(REGEX_PATTERN, page):
        url = link.group()
        hash_code = CreateHash(url)
        if hash_code not in HASH_CODES:
            sufix = GetSufix(url)
            if sufix not in EXCEPTIONS:
                LINKS_LIST.put(url)
            HASH_CODES.add(hash_code)
            outFILE.write(url)
            print(url)
            outFILE.write('\n')

def StartCrawler(base_link):
    Session = requests.Session()
    global LINKS_LIST
    LINKS_LIST.put(base_link)
    HASH_CODES.add(CreateHash(base_link))
    with ThreadPoolExecutor(max_workers=35) as executor:
        while True:
            try:
                target_url = LINKS_LIST.get()
                executor.submit(GetSessionLinks, Session, target_url)
            except:
                continue

if __name__ =='__main__':
    inFILE = open('data.txt', 'r')
    base_link = inFILE.readline().rstrip()
    timeout = int(inFILE.readline())
    new_thread = threading.Thread(target=StartCrawler, args=[base_link])
    new_thread.start()
    time.sleep(timeout)
    os._exit(0)
