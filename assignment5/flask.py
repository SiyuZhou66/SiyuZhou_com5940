############# Flask Modules Setup ##############

from flask import Flask, render_template, url_for, redirect, request, make_response, Response, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests

############ Initialize Flask App ##############

app = Flask(__name__)

#### MySQL SQLAlchemy Object Relations Mapping #####

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/hkphoto'
app.config['SECRET_KEY'] = "mysecret"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False,server_default='')
    active = db.Column(db.Boolean(),nullable=False,server_default='0')
    email = db.Column(db.String(255),nullable=False,unique=True)
    confirmed_at = db.Column(db.DateTime())




class hkphoto(db.Model):
    __tablename__ = 'hkphoto'
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Photo = db.Column(db.String)
    Address = db.Column(db.String)
    NearStation = db.Column(db.String)
    Unique = db.Column(db.String)
    Region = db.Column(db.Integer)
    # description = db.Column(db.Text)


############## Login Manager Setup ###############

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
def home():
    return render_template('home.html')

@app.route("/login")
@login_required
def login():
    message = 'Welcome to Hong Kong Photography'
    return render_template('home.html', message=message)

@app.route("/list_album")
@login_required
def list_album():
    dataset = []
    hkphoto_list = hkphoto.query.all()
    for hkphoto in hkphoto_list:
        dataset.append({'ID':hkphoto.ID, 'Name': hkphoto.name, 'Photo': hkphoto.Photo, 'Address': hkphoto.Address,
                       'NearStation': hkphoto.NearStation, 'Unique':hkphoto.Unique,'Region': hkphoto.Region})
    return render_template('list_album2.html', entries=dataset)

@app.route('/album')
@login_required
def album():
    page_num = 1
    hkphoto = hkphoto.query.paginate(per_page=9, page=page_num, error_out=True)
    return render_template('product_paging.html', hkphoto=hkphoto)

@app.route('/album/<int:page_num>')
@login_required
def album_paging(page_num):
    hkphoto = hkphoto.query.paginate(per_page=9, page=page_num, error_out=True)
    return render_template('product_paging.html', hkphoto=hkphoto)

@app.route("/add_hkphoto",methods=['POST'])
@login_required
def add_hkphoto():
    id = request.form [id]
    Name = request.form['Name']
    Photo = request.form['Photo']
    Address = request.form['Address']
    NearStation = request.form['NearStation']
    Unique = request.form['Unique']
    Region = request.form['Region']
    hkphoto = hkphoto(id=id,Name=Name,Photo=Photo,Address=Address,NearStation=NearStation,Unique=Unique,Region=Region)
    db.session.add(hkphoto)
    db.session.commit()
    dataset = []
    hkphoto_list = hkphoto.query.all()
    for hkphoto in hkphoto_list:
        dataset.append({'ID':hkphoto.ID,'Name': hkphoto.Name,'Photo':hkphoto.Photo,'Address': hkphoto.Address,
                       'NearStation': hkphoto.NearStation, 'Unique':hkphoto.Unique,'Region': hkphoto.Region})
    return render_template('list_album2.html', entries=dataset)

@app.route("/update_hkphoto",methods=['POST','PUT'])
@login_required
def update_hkphoto():
    record_id = request.form['record_id']
    hkphoto = hkphoto.query.filter_by(ID=record_id).first()
    hkphoto.name = request.form['Name']
    hkphoto.poster = request.form['Photo']
    hkphoto.cast = request.form['Address']
    hkphoto.types = request.form['NearStation']
    hkphoto.date = request.form['Unique']
    hkphoto.rating = request.form['Region']
    db.session.commit()
    dataset = []
    hkphoto_list = hkphoto.query.all()
    for hkphoto in hkphoto_list:
        dataset.append({'ID':hkphoto.ID,'Name': hkphoto.Name,'Photo':hkphoto.Photo,'Address': hkphoto.Address,
                       'NearStation': hkphoto.NearStation, 'Unique':hkphoto.Unique,'Region': hkphoto.Region})
    return render_template('list_album2.html', entries=dataset)

@app.route("/delete_hkphoto",methods=['POST','DELETE'])
@login_required
def delete_hkphoto():
    record_id = request.form['record_id']
    hkphoto = hkphoto.query.filter_by(ID=record_id).first()
    db.session.delete(hkphoto)
    db.session.commit()
    dataset = []
    hkphoto_list = hkphoto.query.all()
    for hkphoto in hkphoto_list:
        dataset.append({'ID':hkphoto.ID,'Name': hkphoto.Name,'Photo':hkphoto.Photo, 'Address': hkphoto.Address,
                       'NearStation': hkphoto.NearStation, 'Unique':hkphoto.Unique,'Region': hkphoto.Region})
    return render_template('list_album2.html', entries=dataset)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    message = 'You have successfully logged out。'
    return render_template('home.html', message=message)



######### API Endpoints ##########


######### Run Flask Web App at Port 9030 ##########

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9030, app)

