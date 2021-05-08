from flask import Flask
from blue import HomeBlue, UserBlue, FileBlue, VideoBlue
# from utils.heartBeat import t
from db.connection import poor

app = Flask('')


@app.before_request
def before():
    # for i in poor.connectPoor:
    #     print(i)
    # print(len(poor.connectPoor))
    pass


# a = f'{1}'

app.register_blueprint(HomeBlue.app, url_prefix='/home')
app.register_blueprint(UserBlue.app, url_prefix='/user')
app.register_blueprint(FileBlue.app, url_prefix='/file')
app.register_blueprint(VideoBlue.app, url_prefix='/video')

# t.start()
app.run(
    host='0.0.0.0',
    port=8082
)
