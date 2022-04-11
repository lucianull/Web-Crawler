import re
import time
import ctypes
import requests

def CreateHash(link):
    g = 31
    modulo = 2147483647
    hashCode = 0
    for chr in link:
        if chr != '/':
            hashCode += (ord(chr) * g) % modulo
            hashCode = hashCode % modulo
            g *= 31
            g = g%modulo
    return hashCode


def getAllHTML(page):
    regex = r"(https:\/\/)[a-zA-Z0-9-]*(.ro)[a-zA-Z0-9-/.]*"
    matches = [x.group() for x in re.finditer(regex, page)]
    # print(matches)
    mx = 0
    for x in matches:
        mx = max(mx, len(x))
    print(mx)
    hashList = []
    # i = 0
    # for match in matches:
    #     aux = match.group()
    #     hashCode = CreateHash(aux)
    #     hashList.append(hashCode)
    #     i += 1
    #     print(hashCode)
    #     print(match)
    return hashList, matches

if __name__ == '__main__':
    # inFile = open("input.in", 'r')
    # page = inFile.read()
    req = requests.get("https://stirileprotv.ro/")
    start_time = time.time()
    hashList, mathces = getAllHTML(req.text)
    print("--- %s seconds ---" % (time.time() - start_time))