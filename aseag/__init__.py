import requests
import re


def getStops():
    payload = {'ReturnList': 'StopPointName,StopID'}
    url = 'http://ivu.aseag.de/interfaces/ura/instant_V1'
    r = requests.get(url, params=payload)
    d = {}
    if not r.ok:
        return False
    content = r.content
    for line in content.splitlines():
        line = line.decode()  # deocode to text
        print(line)
        match = re.findall('\[0,\"(.*)\",\"([0-9]*)\"\]', line)
        if not match:
#            print("fail["+str(len(match))+"]: " + line)
            continue
        match = match[0]
        stopId = int(match[1])
        stopName = match[0]
        d[stopId] = stopName
    return d


def getRequest():
    payload = {'ReturnList': 'StopPointName,StopID'}
    url = 'http://ivu.aseag.de/interfaces/ura/instant_V1'
    return requests.get(url, params=payload)
