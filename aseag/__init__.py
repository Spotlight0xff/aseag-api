import requests
import re


def getStops():
    payload = {'ReturnList': 'StopPointName,StopID'}
    url = 'http://ivu.aseag.de/interfaces/ura/instant_V1'
    r = requests.get(url, params=payload)
    if not r.ok:
        return False
    content = r.content
    for line in content.splitlines():
        line = line.decode()  # deocode to text
        match = re.findall('\[(.*),(.*),(.*)\]', line)[0]
        stopId = match[2]
        stopId = int(stopId.split('"')[1])
        stopName = match[1]
        print(stopName+": "+stopId)


def getRequest():
    payload = {'ReturnList': 'StopPointName,StopID'}
    url = 'http://ivu.aseag.de/interfaces/ura/instant_V1'
    return requests.get(url, params=payload)
