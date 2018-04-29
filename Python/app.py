from flask import Flask, render_template, json, request
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'a8l8e8x8'
app.config['MYSQL_DB'] = 'Galactikhackball'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '/var/lib/mysql/mysql.sock'
app.config['MYSQL_CONNECT_TIMEOUT'] = 10
app.config['MYSQL_USE_UNICODE'] = False
app.config['MYSQL_SQL_MODE'] = 'modes'
app.config['MYSQL_READ_DEFAULT_FILE'] = '/etc/my.cnf'
app.config['MYSQL_CHARSET'] = 'utf8'
app.config['MYSQL_CURSORCLASS'] = 'BaseCursor'



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def signup():

    global mysql
    # read the posted values from the UI
    _name = request.form['name']
    _email = request.form['email']
    _password = request.form['psw']
    _teamname = request.form['teamname']

    _hashed_password = generate_password_hash(_password)

    # MySQL configurations

    conn = mysql.connect()

    cursor = conn.cursor()

    cursor.callproc('sp_createUser',(_name,_email,_hashed_password, _teamname))

    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    mysql.init_app(app)

