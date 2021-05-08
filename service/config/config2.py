DEBUG = True

DATABASE_CONF = {
    'user': 'root',
    'password': 'root',
    'db': 'bilibili_v1'
} if DEBUG else {
    'user': '438577872',
    'password': '200102181277dy',
    'db': 'bilibili_v1'
}

VIDEO_DIRECTORY = 'static/video/' if DEBUG else '/www/wwwroot/bilibili.danyi.cool/static/video/'
IMAGE_DIRECTORY = 'static/image/' if DEBUG else '/www/wwwroot/bilibili.danyi.cool/static/image/'
