import os
from flask import redirect,session,render_template,Blueprint
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)

blue = Blueprint('myblue',__name__,template_folder=os.path.join(BASE_DIR,'templates'))

@blue.route('/firstblue')
def show():
    return '<h3>😄</h3>'

@blue.route('/')
def hello_world():
    return 'Hello World!'

@blue.route('/me')
def Imview():
    print('i an here')
    # time.sleep(10)
    return redirect('/')

@blue.route('/addsession')
def addsess():
    session['username'] = 'tom'
    session['password'] = '123456'
    return 'add successful'
@blue.route('/login')
def loginview():
    if session['username'] == 'tom' and session['password'] =='123456':
        return '恭喜登陆成功'
    else:
        return '用户名或密码不正确'
@blue.route('/inf')
def inf():
    user = {}
    user.update({'username':'tom','age':10,'sex':'male'})
    return render_template('other.html',user=user)

@blue.errorhandler(500)
def erro500(e):
    return render_template('erro505.html',e=e)
@blue.route('/error')
def errorview():
    return 5/0
