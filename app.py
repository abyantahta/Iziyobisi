from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'iziyobisi'
mysql = MySQL(app)
api = Api(app)

app.secret_key = 'abcdefghijklmnopqrstuvwxyz'

###API###

@app.route('/')
@app.route('/start')
def start():
    return render_template('index.html')

@app.route('/iziyobisi')
def iziyobisi():
    return render_template('index2.html')

# class Recommendation():
#     def get(self):
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM recommendation')
#         rv = cur.fetchall()
#         return

# api.add_resource(prevDataUser, '/auth/prevDataUser')


@app.route('/recommendation', methods=['POST', 'GET'])
def recommendation():
    if request.method == 'POST':
        penyakit = request.form['penyakit']
        # username = request.form['username']
        cur = mysql.connection.cursor()
        cur.execute(('SELECT * FROM ' + str(penyakit) +' LIMIT 10'))
        ob = cur.fetchall()
        return render_template('index2.html', ob=ob)
    else:
        return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
