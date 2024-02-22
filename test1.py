from flask import Flask , request
import mysql.connector as conn
mydb = conn.connect(host='localhost',user= 'root' ,passwd= '@Gmgaurav7')
cursor = mydb.cursor()

app = Flask(__name__)

@app.route('/fetchdata')
def fetch_data():
    table = request.args.get("table_name")
    cursor.execute("select * from {}".format(table))
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return l

if __name__ == '__main__':
    app.run(port=5003)