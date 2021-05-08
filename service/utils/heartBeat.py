from requests import get
import threading
import time


def h():
    while 1:
        get('http://bilibili.danyi.cool/api/user/heartBeat')
        time.sleep(3600)


t = threading.Thread(target=h)

