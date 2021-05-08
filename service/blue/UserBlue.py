from db.connection import poor
from flask import Blueprint
import re
# print(poor.getConnect())
from utils.requestProperties import getBody, successWrapper, errorWrapper, getToken, createToken, getCurrentFormatTime

app = Blueprint(__name__, __name__)


# @app.route('/login')
# def login():
#     body = getBody()
#     account = body.get('account')
#     password = body.get('password')
#     cur = poor.getConnect()
#     cur.execute('select token from user where account = %s and password = %s limit 1',
#                 (account, password))
#     user = cur.fetchOne()
#     cur.commit()
#     if user:
#         resp = successWrapper('登录成功', token=user['token'])
#     else:
#         resp = errorWrapper(
#             '登录失败'
#         )
#     return resp

@app.route('/logout', methods=['post'])
def logout():
    token = getToken()
    cur = poor.getConnect()
    cur.execute("update user set token = '' where token = %s ",
                (token,))
    cur.commit()
    return successWrapper('退出成功')


@app.route('/findAllVideoByPage/<int:ID>')
def findAllVideoByPage(ID):
    cur = poor.getConnect()
    try:
        token = getToken()
        cur.execute('select id from user where token = %s', token)
        # up_id = cur.fetchOne()['id']
        cur.execute(f'select * from series where up_id = %s ', (ID,))
        li = cur.fetchAll()
        cur.commit()
        return successWrapper(data=li)
    except:
        cur.rollback()
        return errorWrapper()


@app.route('/heartBeat')
def heartBeat():
    cur = poor.getConnect()
    cur.execute(f'select * from praise ')
    li = cur.fetchAll()
    cur.commit()
    return successWrapper(data=li)


@app.route('/login', methods=['post'])
def login():
    cur = poor.getConnect()
    try:
        body = getBody()
        phoneOrEmail = body.get('phoneOrEmail')
        password = body.get('password')
        if '@' in phoneOrEmail:
            loginType = 'email'
        else:
            loginType = 'phone'
        cur.execute(f'select id,name from user where {loginType} = %s and password = %s limit 1',
                    (phoneOrEmail, password,))
        userInfo = cur.fetchOne()
        token = createToken()
        cur.execute('update user set token = %s where id=%s',
                    (token, userInfo.get('id'),))
        cur.commit()

        return successWrapper('登录成功', data={
            'token': token,
        })
    except Exception as e:
        print(e.args)
        cur.rollback()
        return errorWrapper('登录失败')


@app.route('/getInfo', methods=['post'])
def getInfo():
    cur = poor.getConnect()
    try:
        token = getToken()
        cur.execute('select name, birthday, phone , avatar ,id  from user where token = %s limit 1', (token,))
        userInfo = cur.fetchOne()
        # print(token)
        if userInfo:
            # print(userInfo)
            cur.commit()
            return successWrapper(data=userInfo)
        else:
            cur.rollback()
            return errorWrapper()
    except:
        cur.rollback()
        return errorWrapper()


@app.route('/register', methods=['post'])
def register():
    cur = poor.getConnect()
    try:
        body = getBody()
        name = body.get('name')
        phone = body.get('phone', '').strip()
        password: str = body.get('password')
        if (re.match('[0-9]{11}', phone).group()) != phone:
            cur.back()
            return errorWrapper('手机号有误')

        last_login_time = getCurrentFormatTime()
        createAt = last_login_time
        token = createToken()

        if len(name.replace(' ', '')) == 0:
            cur.back()
            return errorWrapper('请输入用户名')

        if len(password.strip()) <= 5:
            cur.back()
            return errorWrapper('该密码太短,不符合要求')

        cur.execute('select id from user where phone = %s', (phone,))

        if cur.fetchOne():
            cur.rollback()
            return errorWrapper('该手机号已注册')

        cur.execute('insert into user'
                    '(name, email, password, birthday, phone, createAt, token, last_login_time,avatar) '
                    'value (%s,null,%s,null,%s,%s,%s,%s,\'defaultAvatar.jpg\')',
                    (name, password, phone, createAt, token, last_login_time))
        cur.commit()
        return successWrapper('注册成功')
    except Exception as e:
        cur.rollback()
        print(e.args)
        return errorWrapper()
