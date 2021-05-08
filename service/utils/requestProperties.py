from flask import request
import time


def getBody():
    data = request.json
    if data:
        return data
    else:
        return {}


def getArgs():
    args = request.args
    if args:
        return args
    else:
        return {

        }


def getFiles():
    files = request.files
    return files


def getHeader():
    return request.headers


def getForm():
    return request.form


def getToken():
    return getHeader().get('token')


def getCurrentFormatTime():
    return time.strftime('%Y/%m/%d %H:%M:%S')


def successWrapper(msg=None, data=None, code=20000, **kwargs):
    response = {
        'code': code,
    }
    if msg:
        response['msg'] = {
            'type': 'success',
            'message': msg
        }
    if data:
        response['data'] = data
    for key in kwargs:
        response[key] = kwargs[key]
    return response


def errorWrapper(msg=None, data=None, code=50000, **kwargs):
    response = {
        'code': code,
    }
    if msg:
        response['msg'] = {
            'type': 'error',
            'message': msg
        }
    if data:
        response['data'] = data

    for key in kwargs:
        response[key] = kwargs[key]
    return response


def timeToHex():
    timestamp = time.time()
    h = hex(int(timestamp * 100000))
    return h[2:]


def createToken():
    currentTime = time.time()
    return hex(int(currentTime * 1000000))[2:]
