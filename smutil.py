#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import psutil
import time
import requests
import subprocess
import re

parser = argparse.ArgumentParser()
parser.add_argument('--check', required=True)
args = parser.parse_args()

def lineNotify(message):
    payload = {'message': message}
    return _lineNotify(payload)


def notifyFile(filename):
    file = {'imageFile': open(filename, 'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload, file)


def notifyPicture(url):
    payload = {'message': " ", 'imageThumbnail': url, 'imageFullsize': url}
    return _lineNotify(payload)


def notifySticker(stickerID, stickerPackageID):
    payload = {'message': " ", 'stickerPackageId': stickerPackageID,
               'stickerId': stickerID}
    return _lineNotify(payload)


def _lineNotify(payload, file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 's6OAyTFWSSSWWS59FLM85xE8XAH7amHRezC7EjVDFoX'
    headers = {'Authorization': 'Bearer '+token}
    return requests.post(url, headers=headers, data=payload, files=file)

if (args.check == "1"):
    lineNotify('CPU :  \nRAM : ')
    notifySticker(40, 2)
    # notifyPicture("http://sirimedia.com/img/Logosiri.png")
    k = time.time() - psutil.boot_time()
    x = ( k / 60 ) / 60
    print('CPU : ',str(psutil.cpu_percent(interval=1)))
    print('Disk Usage : {}%'.format(psutil.disk_usage('/').percent))
    print('Memory Free : ', '{} MB'.format( int(psutil.virtual_memory().available / 1024 / 1024)))
    print('Uptime Hours : ', round( x,2 ) )
    #print('CPU : ',str(psutil.cpu_percent(interval=1)))
    #print('Disk Usage : {}%'.format(psutil.disk_usage('/').percent))
    #print('Memory Free : ', '{} MB'.format( int(psutil.virtual_memory().available / 1024 / 1024)))

if (args.check == "2"):
    service = 'nginx'
    p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
    (output, err) = p.communicate()
    output = output.decode('utf-8')
    print(output)
    g = re.search("^active",output)
    if (g):
        lineNotify('SERVICE WEB RUNNING')
    else:
        lineNotify('SERVICE WEB NOT RUNNING')
        subprocess.Popen(["sudo","systemctl","restart","nginx"], stdout=subprocess.PIPE)
