import werkzeug
from flask import Blueprint
from utils.requestProperties import getFiles, getHeader, getBody, getArgs, getForm, getToken, errorWrapper, \
    getCurrentFormatTime, timeToHex, successWrapper
from db.connection import poor
from json import dumps

app = Blueprint(__name__, __name__)
# VIDEO_DIRECTORY = 'E:/VueProject/bilibili/public/static/video/'
from config.config import VIDEO_DIRECTORY, IMAGE_DIRECTORY


@app.route('/uploadVideo', methods=['post'])
def uploadVideo():
    cur = poor.getConnect()
    try:
        files = getFiles()['file']
        resource_url = saveVideo(files)
        data = getForm()
        father_video_id = data.get('series_id', '')
        up_id = data.get('up_id')
        print(up_id)

        cur.execute('select max(no) from video where father_video_id = %s', father_video_id)
        maxNo = cur.fetchOne()['max(no)']
        if maxNo:
            maxNo = maxNo + 1
        else:
            maxNo = 1
        createAt = getCurrentFormatTime()

        index_picture_url = data.get('index_picture_url')

        cur.execute(
            '''insert into video
                    (father_video_id, up_id,
                    up_time,
                    no,
                    index_picture_url,
                    resource_url, createAt
                    )
            values (%s,%s,%s,%s,%s,%s,%s);''',
            (father_video_id, up_id, createAt, maxNo, index_picture_url, resource_url, createAt)
        )

        cur.commit()
        return successWrapper()
    except Exception as e:

        print(e.args)
        cur.rollback()
        return errorWrapper()


@app.route('/uploadIndexImage', methods=['post'])
def uploadIndexImage():
    cur = poor.getConnect()
    try:
        token = getToken()
        cur.execute('select id from user where token = %s', (token,))
        up_id = cur.fetchOne()['id']
        createAt = getCurrentFormatTime()
        data = getForm()
        tags = dumps([data.get('type')])
        files = getFiles()['file']
        index_picture_url = saveBackground(files)
        title = data.get('title')
        # up_id = data.get('up_id')
        cur.execute('insert into series'
                    '(up_id,title, up_time, praise_num, index_picture_url, createAt, tags)'
                    ' values (%s,%s,%s,%s,%s,%s,%s);',
                    (up_id, title, createAt, 0, index_picture_url, createAt, tags))

        series_id = cur.lastId()
        cur.commit()
        return successWrapper(
            data={
                'series_id': series_id,
                'index_picture_url': index_picture_url,
                'up_id': up_id
            }
        )
    except:
        cur.rollback()
        return errorWrapper()

def saveBackground(f):
    name = timeToHex() + '.jpg'
    with open(IMAGE_DIRECTORY + name, 'wb') as file:
        file.write(f.stream.read())
    return name


def saveVideo(video):
    name = timeToHex() + '.mp4'
    with open(VIDEO_DIRECTORY + name, 'wb') as file:
        file.write(video.stream.read())
    return name
