from flask import Blueprint

from db.connection import poor
from utils.requestProperties import getArgs, successWrapper, errorWrapper, getBody, getCurrentFormatTime

app = Blueprint(__name__, __name__)


@app.route('/getVideoUrlBySeriesIdAndNo')
def getVideoUrlBySeriesIdAndNo():
    cur = poor.getConnect()
    try:
        args = getArgs()
        series_id = args.get('series_id')
        no = args.get('no', 1)
        cur.execute('select title from series where id = %s limit 1', (series_id,))
        one = cur.fetchOne()
        title = one['title']
        cur.execute('select resource_url,createAt from video where father_video_id=%s and no=%s ', (series_id, no))
        one = cur.fetchOne()
        resource_url = one['resource_url']
        createAt = one['createAt']
        cur.commit()
        return successWrapper(data={
            'resource_url': resource_url,
            'title': title,
            'createAt': createAt
        })
    except:
        return errorWrapper()


@app.route('/sendBarrage', methods=['post'])
def sendBarrage():
    cur = poor.getConnect()
    try:
        body = getBody()
        msg = body.get('msg')
        video_id = body.get('series_id')
        video_time = body.get('time')
        no = body.get('no', 1)
        createAt = getCurrentFormatTime()
        cur.execute('insert into barrage (user_id, video_id,no, time, msg, createAt) values (%s,%s,%s,%s,%s,%s);',
                    (1, video_id, no, video_time, msg, createAt))
        cur.commit()
        return successWrapper()
    except Exception as e:
        cur.rollback()
        return errorWrapper()


@app.route('/fetchBarrageBySeriesId')
def fetchBarrageBySeriesId():
    cur = poor.getConnect()
    try:
        args = getArgs()
        series_id = args.get('series_id')
        no = args.get('no', 1)
        print(series_id, no)
        cur.execute('select * from barrage where video_id = %s and no = %s order by time', (series_id, no))
        li = cur.fetchAll()
        cur.commit()
        return successWrapper(data=li)
    except:
        cur.rollback()
        return errorWrapper()


@app.route('/fetchVideoNos')
def fetchVideoNos():
    cur = poor.getConnect()
    try:
        args = getArgs()
        series_id = args.get('series_id')
        cur.execute('select no from video where father_video_id = %s', (series_id,))
        li = cur.fetchAll()
        cur.commit()
        return successWrapper(data=li)
    except:
        cur.rollback()
        return errorWrapper()


@app.route('/fetchComments')
def fetchComments():
    return {
        "status": "成功",
        "code": 20000,
        "data": [
            {
                "id": "comment0001",
                "date": "2018-07-05 08:30",
                "ownerId": "talents100020",
                "fromId": "errhefe232213",
                "fromName": "Kar",
                "fromAvatar": "/static/avatar/kar.jpg",
                "likeNum": 3,
                "content": "这部电影真好看",
                "reply": [
                    {
                        "id": "34523244545",
                        "commentId": "comment0001",
                        "fromId": "observer223432",
                        "fromName": "Feipo",
                        "fromAvatar": "/static/img/mw690/69e273f8gy1ft1541dmb7j215o0qv7wh.jpg",
                        "toId": "errhefe232213",
                        "toName": "Kar",
                        "toAvatar": "/static/img/006DLFVFgy1ft0j2pddjuj30v90uvagf.jpg",
                        "content": "赞同",
                        "date": "2018-07-05 08:35"
                    },
                    {
                        "id": "34523244545",
                        "commentId": "comment0001",
                        "fromId": "observer567422",
                        "fromName": "路人甲",
                        "fromAvatar": "/static/avatar/kar.jpg",
                        "toId": "observer223432",
                        "toName": "路人乙",
                        "toAvatar": "/static/img/mw690/69e273f8gy1ft1541dmb7j215o0qv7wh.jpg",
                        "content": "赞同",
                        "date": "2018-07-05 08:50"
                    }
                ]
            },
            {
                "id": "comment0002",
                "date": "2018-07-05 08:30",
                "ownerId": "talents100020",
                "fromId": "errhefe232213",
                "fromName": "土匪丁",
                "fromAvatar": "/static/img/006DLFVFgy1ft0j2q2p8pj30v90uzmzz.jpg",
                "likeNum": 0,
                "content": "好看",
                "reply": []
            }
        ]
    }
