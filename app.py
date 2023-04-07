from flask import Flask,render_template
from db import db
from visitor_vlog import visitor_blueprint
# THIS WILL NOT ALLOW UNAUNTHEITCATED BOTS TO USE THE SERVER
from flask_cors import CORS
from dashboard import dashboard_blueprint

app = Flask(__name__)
CORS(app)

#database configurations

username = "root"
password=""
userpass='mysql+pymysql://' + username + ':' + password + '@'
server = '127.0.0.1'
dbname = '/walmart_visitor'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

#register blueprint

app.register_blueprint(visitor_blueprint)
app.register_blueprint(dashboard_blueprint)

#API END POINT ROUTE

@app.route('/')
def serverstatus():
    return render_template('index1.html')
@app.route('/dashboard.html')
def server():
    return render_template('dashboard.html')

if __name__== "__main__":
    app.debug = True
    app.run()