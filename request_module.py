from operator import mod
import requests
import re
from variables import POWERS, REGEX_PATTERN
import time
from multiprocessing import Pool

INDEX = 1
HASH_CODES = {}
MODULO = 2147483647


def CreateHash(link):
    hashCode = 0
    i = 0
    for chr in link:
        if chr != '/':
            hashCode += (ord(chr) * POWERS[i]) % MODULO
            hashCode = hashCode % MODULO
            i += 1
    return hashCode

def GetSessionLink(session, base_url):
    global INDEX
    page = session.get(base_url).text
    for link in re.finditer(REGEX_PATTERN, page):
        url = link.group()
        hash_code = CreateHash(url)
        HASH_CODES[hash_code] = INDEX
        INDEX += 1



if __name__ == '__main__':
    start_time = time.time()
    session = requests.Session()
    GetSessionLink(session, 'https://stirileprotv.ro/')
    print("--- %s seconds ---" % (time.time() - start_time))
    