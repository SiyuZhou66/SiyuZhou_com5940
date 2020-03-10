from flask import Flask, render_template, url_for, redirect, request, make_response, Response, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

import MySQLdb

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id

############ Web Page Routes Setup ###############

@app.route("/")
@login_required
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    message = 'Please login in first.'
    return render_template('login.html', message=message)

@app.route('/query_auth')
def query_auth():
    username = request.args.get("username")
    password = request.args.get("password")
    if username == "1155131606@link.cuhk.edu.hk" and password == "1234":
        login_user(User(1))
        message = "Dear " + username + ", welcome to Siyu's pages. Your login has been granted."
        return make_response(message, 200, )
    else:
        message = 'Wrong password!'
        return make_response( message,401,{'WWW-Authenticate':'Basic realm="Login Required"'})

@app.route("/form_auth",methods=['POST'])
def form_auth():
    username = request.form['email']
    password = request.form['pwd']
    if username == "1155131606@link.cuhk.edu.hk" and password == "1234":
        login_user(User(1))
        message = "Dear " + username + ", welcome to Siyu's pages. Your login has been granted."
        return render_template('home.html', message=message)
    else:
        message = 'Wrong password!'
        return render_template('login.html',message=message)

@app.route('/album')
@login_required
def album():
    connection = MySQLdb.connect(host="SiyuZhou66.mysql.pythonanywhere-services.com",
                     user="SiyuZhou66",
                     passwd="Tim0606@",
                     db="SiyuZhou66$demo",
                     charset='utf8mb4')
    user = {"name":"Bernard"}
    with connection.cursor() as cursor:
        sql = "SELECT * FROM spots"
        cursor.execute(sql)
        result = cursor.fetchall()
    final_result = [list(i) for i in result]
    dataset=[]
    dict={}
    for i in final_result:
        dict['name'] = i[0]
        dict['Photo'] = i[1]
        dict['Address'] = i[2]
        dict['Region'] = i[6]
        dict['Photo_url'] = i[7]
        dataset.append(dict.copy()) #markers.append(fld.copy())
    cursor.close()
    connection.close()
    return render_template('product2.html',album_user=user, dataset=dataset)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    message = 'Thanks for logging out.'
    return render_template('login.html',message=message)

@app.errorhandler(500)
def internal_error(error):
    message = 'Wrong password!'
    return render_template('login.html',message=message),500

######### API Endpoints ##########

@app.route('/api_auth', methods=['POST'])
def api_auth():
    username = request.json['username']
    password = request.json['password']
    if username == "1155131606@link.cuhk.edu.hk" and password == "1234":
        login_user(User(1))
        message = "Dear " + username + ", welcome to Siyu's pages. Your login has been granted."
        return jsonify({'response':'ok!','message':message})
    else:
        message = 'Wrong password!'
        return jsonify({'response':'Invalid!','message':'Cannot authenticate.'})
@app.route('/api_album', methods=['POST'])
@login_required
def api_album():
    connection = MySQLdb.connect(host="SiyuZhou66.mysql.pythonanywhere-services.com",
                     user="SiyuZhou66",
                     passwd="Tim0606@",
                     db="SiyuZhou66$demo",
                     charset='utf8mb4')
    with connection.cursor() as cursor:
        sql = "SELECT * FROM spots"
        cursor.execute(sql)
        result = cursor.fetchall()
    final_result = [list(i) for i in result]
    dataset=[]
    dict={}
    for i in final_result:
        dict['name'] = i[0]
        dict['Photo'] = i[1]
        dict['Address'] = i[2]
        dict['Region'] = i[6]
        dict['Photo_url'] = i[7]

        dataset.append(dict.copy()) #markers.append(fld.copy())
    cursor.close()
    connection.close()
    return jsonify({'Album': dataset})

######### Run Flask Web App at Port 9030 ##########

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9030, app)